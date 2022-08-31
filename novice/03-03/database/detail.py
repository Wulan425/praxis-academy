try:
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="wulan425")

except Exception as e:
    print(e)

curs = conn.cursor()
query = f"select * from santri where nama='Rifa'"
curs.execute(query)
data = curs.fetchone()

print("name:", data[0], "umur:", data[1])