try:
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="wulan425")

    curs = conn.cursor()
    
    nama = "Restu"
    umur = 15
    query = f"insert into santri(nama, umur) values ('{nama}', {umur})"
   
    curs.execute(query)
    conn.commit()
    print("data masuk")
except Exception as e:
    print(e)