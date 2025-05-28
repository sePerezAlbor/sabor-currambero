document.addEventListener("DOMContentLoaded", function () {
    const map = L.map('map').setView([10.96854, -74.78132], 13);

    // Mapa base
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; OpenStreetMap contributors'
    }).addTo(map);

    let marcadores = [];
    let marcadorPorId = {}; // Para vincular cada restaurante por ID


    function limpiarMarcadores() {
        marcadores.forEach(m => map.removeLayer(m));
        marcadores = [];
    }

    function agregarMarcadores(data) {
        marcadorPorId = {}; // Reiniciar el mapa de marcadores
        data.forEach(restaurante => {
            const marker = L.marker([restaurante.latitud, restaurante.longitud]).addTo(map);
            marker.bindPopup(`
                <strong>${restaurante.nombre}</strong><br>
                Tipo: ${restaurante.tipo_comida}<br>
                Precio: $${restaurante.precio_promedio}<br>
                Calificación: ${restaurante.calificacion_prom} ⭐<br>
                <a href="https://instagram.com/${restaurante.instagram.replace('@','')}" target="_blank">${restaurante.instagram}</a>
            `);
            marcadores.push(marker);
            marcadorPorId[restaurante.id] = marker;
        });
    }


    function actualizarRanking(restaurantes) {
        const rankingDiv = document.getElementById('rankingRestaurantes');
        rankingDiv.innerHTML = "";

        const top = [...restaurantes]
            .sort((a, b) => b.calificacion_prom - a.calificacion_prom)
            .slice(0, 5);

        top.forEach(r => {
            const item = document.createElement("li");
            item.className = "list-group-item";
            item.innerHTML = `
                <strong>${r.nombre}</strong><br>
                ⭐ ${r.calificacion_prom}
            `;
            item.setAttribute('data-id', r.id);
            item.style.cursor = 'pointer';

            item.addEventListener('click', () => {
                const marcador = marcadorPorId[r.id];
                if (marcador) {
                    map.setView(marcador.getLatLng(), 16);
                    marcador.openPopup();
                }
            });

            rankingDiv.appendChild(item);
        });

    }

    function aplicarFiltros(restaurantes) {
        const tipos = [
            document.getElementById('filtroComida').value,
            document.getElementById('tipoComplementario1').value,
            document.getElementById('tipoComplementario2').value
        ].filter(t => t !== ""); // Eliminar vacíos

        const maxPresupuesto = parseInt(document.getElementById('filtroPresupuesto').value);
        const textoBusqueda = document.getElementById('filtroBusqueda').value.toLowerCase();

        const filtrados = restaurantes.filter(r =>
            (tipos.length === 0 || tipos.includes(r.tipo_comida)) &&
            (isNaN(maxPresupuesto) || r.precio_promedio <= maxPresupuesto) &&
            r.nombre.toLowerCase().includes(textoBusqueda)
        );


        limpiarMarcadores();

        // Mostrar contador
        document.getElementById('contadorRestaurantes').textContent = `Mostrando ${filtrados.length} restaurante(s)`;

        agregarMarcadores(filtrados);
        actualizarRanking(filtrados);
    }

    // Cargar datos iniciales
    fetch('/api/restaurantes')
        .then(response => response.json())
        .then(data => {
            agregarMarcadores(data);
            actualizarRanking(data);

            // Filtro por tipo de comida
            document.getElementById('filtroComida').addEventListener('change', () => aplicarFiltros(data));
            document.getElementById('tipoComplementario1').addEventListener('change', () => {
                aplicarFiltros(data);
                mostrarTiposComplementarios();
            });
            document.getElementById('tipoComplementario2').addEventListener('change', () => {
                aplicarFiltros(data);
                mostrarTiposComplementarios();
            });
            // Filtro por búsqueda de nombre
            document.getElementById('filtroBusqueda').addEventListener('input', () => aplicarFiltros(data));

            // Filtro por presupuesto + mostrar valor
            const presupuestoInput = document.getElementById('filtroPresupuesto');
            const presupuestoValor = document.getElementById('valorPresupuesto');

            presupuestoInput.addEventListener('input', () => {
                presupuestoValor.textContent = `$${presupuestoInput.value}`;
                aplicarFiltros(data);
            });

            // Mostrar contador inicial
            document.getElementById('contadorRestaurantes').textContent = `Mostrando ${data.length} restaurante(s)`;
        })
        .catch(error => {
            console.error("Error al cargar restaurantes:", error);
        });
});
