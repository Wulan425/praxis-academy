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
query = f"select * from santri"
curs.execute(query)
data = curs.fetchall()

for d in data:
    print("name:", d[0], "umur:", d[1])