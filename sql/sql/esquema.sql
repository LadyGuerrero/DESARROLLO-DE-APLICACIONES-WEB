CREATE DATABASE IF NOT EXISTS ia_universidad;
USE ia_universidad;

CREATE TABLE IF NOT EXISTS categorias (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS herramientas (
    id_herramienta INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(300) NOT NULL,
    disponible TINYINT DEFAULT 1,
    id_categoria INT,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)
);

INSERT INTO categorias (nombre) VALUES
('Asistente Virtual'),
('Investigación'),
('Productividad'),
('Diseño'),
('Educación');