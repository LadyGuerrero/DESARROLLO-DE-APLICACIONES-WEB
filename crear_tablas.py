import psycopg2

conn = psycopg2.connect("postgresql://render_com_zmpz_user:a6hBQBZG5Dd3lvZKAqclKlu81PUA5ho9@dpg-db3nojtg1s2s73b6p0tg-a.ohio-postgres.render.com/render_com_zmpz")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS categorias (
    id_categoria SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS herramientas (
    id_herramienta SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(300) NOT NULL,
    disponible SMALLINT DEFAULT 1,
    id_categoria INT,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS recursos (
    id_recurso SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    tipo VARCHAR(100) NOT NULL,
    url VARCHAR(300),
    gratuito SMALLINT DEFAULT 1,
    id_categoria INT,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    usuario VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
)''')

cursor.execute("""INSERT INTO categorias (nombre)
    SELECT nombre FROM (VALUES 
        ('Asistente Virtual'),
        ('Investigacion'),
        ('Productividad'),
        ('Diseno'),
        ('Educacion')
    ) AS v(nombre)
    WHERE NOT EXISTS (SELECT 1 FROM categorias)""")

conn.commit()
cursor.close()
conn.close()
print('Tablas creadas exitosamente!')