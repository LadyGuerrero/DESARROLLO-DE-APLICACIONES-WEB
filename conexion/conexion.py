import psycopg2

def get_connection():
    return psycopg2.connect(
        "postgresql://render_com_zmpz_user:a6hBQBZG5Dd3lvZKAqclKlu81PUA5ho9@dpg-db3nojtg1s2s73b6p0tg-a.ohio-postgres.render.com/render_com_zmpz"
    )