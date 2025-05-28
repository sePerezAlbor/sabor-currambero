USE sabor_currambero;

INSERT INTO `Usuario` (
    `primer_nombre`, 
    `segundo_nombre`, 
    `primer_apellido`, 
    `segundo_apellido`, 
    `correo`, 
    `contrasenia`, 
    `fecha_registro`, 
    `rol`
) VALUES (
    'Admin',          -- primer nombre genérico
    NULL,             -- segundo nombre nulo
    'Usuario',        -- primer apellido genérico
    NULL,             -- segundo apellido nulo
    'admin@ejemplo.com', -- correo genérico
    '123',            -- contraseña simple 123
    NOW(),            -- fecha actual de registro
    'admin'           -- rol admin
);


INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Rincón Currambero', 'Cra 50 #76-32, Barranquilla', 'Típica', 50000, 10.9966243, -74.8028719, 4.1, 1, '@rincóncurrambero');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Rincón Currambero', 'Calle 70 #41-20, Barranquilla', 'Mexicana', 30000, 10.9875109, -74.806518, 4.7, 1, '@rincóncurrambero');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Restaurante Currambero', 'Av. Murillo #45-10, Barranquilla', 'Árabe', 50000, 10.9278115, -74.799055, 3.7, 1, '@restaurantecurrambero');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Comidas Currambero', 'Calle 84 #45-25, Barranquilla', 'Mexicana', 20000, 11.0252006, -74.8035357, 4.5, 1, '@comidascurrambero');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Delicias Currambero', 'Carrera 43 #85-15, Barranquilla', 'Típica', 40000, 10.9904763, -74.8050295, 4.6, 1, '@deliciascurrambero');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Rincón Barranquilla', 'Calle 72 #38-29, Barranquilla', 'Rápida', 15000, 11.0030184, -74.7960035, 4.1, 1, '@rincónbarranquilla');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Comidas Express', 'Calle 76 #54-11, Barranquilla', 'Italiana', 20000, 11.0000746, -74.8083693, 4.5, 1, '@comidasexpress');

-- Nuevos registros
INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Sazón Caribeño', 'Cra 46 #74-29, Barranquilla', 'Caribeña', 35000, 10.993214, -74.796894, 4.3, 1, '@sazoncaribeno');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Sabores del Río', 'Calle 75 #43-12, Barranquilla', 'Mariscos', 45000, 10.998112, -74.790450, 4.6, 1, '@saboresdelrio');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Fogón Currambero', 'Cra 52 #80-14, Barranquilla', 'Típica', 30000, 10.989401, -74.808612, 4.0, 1, '@fogoncurrambero');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('La Guaracha del Sabor', 'Calle 82 #41-33, Barranquilla', 'Fusión', 55000, 10.999786, -74.801238, 4.8, 1, '@laguarachadelsabor');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Tierra y Mar', 'Carrera 44 #72-18, Barranquilla', 'Internacional', 60000, 10.987322, -74.793211, 4.2, 1, '@tierraymarbaq');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('El Rincón del Ají', 'Calle 77 #49B-22, Barranquilla', 'Peruana', 42000, 10.994802, -74.798631, 4.7, 1, '@rincondelaji');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Sabrosura Urbana', 'Cra 41 #85-05, Barranquilla', 'Comida Urbana', 25000, 10.991517, -74.799445, 4.4, 1, '@sabrosuraurbana');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('La Arepita Loca', 'Calle 85 #50-21, Barranquilla', 'Típica', 18000, 10.993912, -74.811234, 4.3, 1, '@larepitaloca');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Barranquilla Burger House', 'Cra 53 #76-44, Barranquilla', 'Rápida', 28000, 10.995178, -74.807111, 4.6, 1, '@burgerhousebaq');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Casa del Ajíaco', 'Calle 79 #41-17, Barranquilla', 'Colombiana', 32000, 10.991000, -74.802900, 4.2, 1, '@casadelajiaco');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('La Paila Currambera', 'Cra 47 #84-02, Barranquilla', 'Criolla', 37000, 11.002143, -74.809650, 4.5, 1, '@lapailacurrambera');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Sabor del Pacífico', 'Carrera 40 #76-18, Barranquilla', 'Pacífica', 39000, 10.990701, -74.794521, 4.4, 1, '@sabordelpacifico');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Maíz y Maíz', 'Calle 86 #42-90, Barranquilla', 'Mexicana', 31000, 10.988643, -74.803284, 4.1, 1, '@maiz_y_maiz');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Viento y Fuego', 'Cra 49 #79-33, Barranquilla', 'Parrilla', 48000, 10.997422, -74.795113, 4.7, 1, '@vientoyfuego');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Sabor Hindú', 'Calle 72 #43-40, Barranquilla', 'India', 52000, 10.985712, -74.800933, 4.3, 1, '@saborhindu');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Chuzo Express', 'Cra 42 #80-55, Barranquilla', 'Rápida', 22000, 10.999013, -74.804115, 4.0, 1, '@chuzoexpress');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('La Esquina del Ceviche', 'Calle 83 #44-10, Barranquilla', 'Mariscos', 46000, 10.996781, -74.798200, 4.6, 1, '@laesquinadelceviche');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('El Fogón Caribeño', 'Carrera 38 #45-12, Soledad', 'Caribeña', 34000, 10.916211, -74.782421, 4.2, 1, '@elfogoncaribeno');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Punto Mex', 'Calle 30 #20-15, Soledad', 'Mexicana', 29000, 10.910822, -74.777110, 4.1, 1, '@puntomex');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('La Casa Árabe', 'Av. Cordialidad #10-50, Malambo', 'Árabe', 53000, 10.883101, -74.767001, 4.3, 1, '@lacasaarabe');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('La Rápida del Sur', 'Carrera 4 #15-60, Soledad', 'Rápida', 17000, 10.896222, -74.777881, 3.9, 1, '@larapidadelsur');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Trattoria Costeña', 'Via al Mar #Km 5, Barranquilla', 'Italiana', 47000, 10.944531, -74.837652, 4.5, 1, '@trattoriacostena');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Mar y Tierra Fusión', 'Carrera 65 #98-30, Barranquilla', 'Fusión', 56000, 11.020112, -74.834212, 4.7, 1, '@marytierrafusion');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Cevicheando', 'Calle 106 #53-29, Barranquilla', 'Mariscos', 41000, 11.032999, -74.829411, 4.4, 1, '@cevicheando_baq');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Rincón Criollo', 'Carrera 8 #42-90, Galapa', 'Criolla', 32000, 10.913450, -74.891234, 4.0, 1, '@rinconcriollo');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Barranquilla Urbana', 'Calle 110 #50-15, Barranquilla', 'Comida Urbana', 26000, 11.036745, -74.817633, 4.5, 1, '@bquillaurbana');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Sabores del Atlántico', 'Calle 35 #22-10, Puerto Colombia', 'Típica', 36000, 10.959301, -74.955234, 4.1, 1, '@saboresdelatlantico');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('El Patio del Sabor', 'Cra 21 #44-30, Barranquilla', 'Típica', 37000, 10.975212, -74.790113, 4.4, 1, '@elpatiosabor');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Fonda Mexicana', 'Calle 45 #35-60, Barranquilla', 'Mexicana', 33000, 10.977324, -74.785761, 4.2, 1, '@fondamexicana');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Sabores del Medio Oriente', 'Carrera 43 #62-15, Barranquilla', 'Árabe', 55000, 10.987110, -74.794728, 4.5, 1, '@saboresmediooriente');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Barranquilla Express', 'Calle 76 #30-20, Barranquilla', 'Rápida', 19000, 11.002817, -74.778564, 4.0, 1, '@bqexpress');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Trattoria Barranquilla', 'Carrera 59 #85-11, Barranquilla', 'Italiana', 47000, 11.017521, -74.805133, 4.6, 1, '@trattoriabq');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Ají y Mar', 'Carrera 41 #94-20, Barranquilla', 'Mariscos', 45000, 11.024721, -74.794901, 4.3, 1, '@ajiymar');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Delicias Criollas', 'Calle 65 #27-45, Barranquilla', 'Criolla', 31000, 10.994381, -74.773922, 4.1, 1, '@deliciascriollas');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Rincón Pacífico', 'Carrera 54 #68-20, Barranquilla', 'Pacífica', 42000, 10.999340, -74.788201, 4.5, 1, '@rinconpacifico');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Casa Hindú', 'Calle 55 #22-10, Barranquilla', 'India', 52000, 10.983212, -74.775440, 4.3, 1, '@casahindu');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Sazón Parrillero', 'Calle 91 #52-15, Barranquilla', 'Parrilla', 49000, 11.028521, -74.814701, 4.7, 1, '@sazonparrillero');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('La Cazuela del Pueblo', 'Cra 9G #98A-21, El Pueblo, Barranquilla', 'Típica', 32000, 10.947221, -74.841329, 4.2, 1, '@lacazueladelpueblo');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Tacos del Bosque', 'Cra 6B #97-12, El Bosque, Barranquilla', 'Mexicana', 28000, 10.951003, -74.834189, 4.1, 1, '@tacosdelbosque');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Shawarma Robles', 'Cra 9C #106-30, Los Robles, Barranquilla', 'Árabe', 49000, 10.956700, -74.843100, 4.4, 1, '@shawarmarobles');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Rápido Siete', 'Calle 98A #7B-11, Siete de Abril, Barranquilla', 'Rápida', 18000, 10.944812, -74.851611, 4.0, 1, '@rapidosiete');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Pizza Malvinas', 'Calle 110 #6B-30, Las Malvinas, Barranquilla', 'Italiana', 23000, 10.958114, -74.852114, 4.3, 1, '@pizzamalvinas');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Mariscos del Sur', 'Calle 96 #8B-25, La Sierrita, Barranquilla', 'Mariscos', 43000, 10.942910, -74.839370, 4.2, 1, '@mariscosdelsur');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Criollo y Punto', 'Cra 8G #103B-50, Evaristo Sourdis, Barranquilla', 'Criolla', 30000, 10.954114, -74.840904, 4.1, 1, '@criolloypunto');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Sabores Pacíficos', 'Calle 105 #6D-12, La Pradera, Barranquilla', 'Pacífica', 42000, 10.956001, -74.847210, 4.5, 1, '@saborespacificos');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('Sazón de Carrizal', 'Calle 98 #6B-75, Carrizal, Barranquilla', 'Colombiana', 36000, 10.946329, -74.847112, 4.3, 1, '@sazoncarrizal');

INSERT INTO Restaurante (nombre, direccion, tipo_comida, precio_promedio, latitud, longitud, calificacion_prom, estado, instagram)
VALUES ('La Parrilla del Suroccidente', 'Cra 7C #99-40, Los Ángeles II, Barranquilla', 'Parrilla', 48000, 10.949712, -74.837814, 4.6, 1, '@parrillasuroccidente');
