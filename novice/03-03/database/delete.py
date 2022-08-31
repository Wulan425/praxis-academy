try:
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="wulan425")

    curs = conn.cursor()
    
    nama = "Rika"
    query = f"delete from santri where nama='{nama}' "
   
    curs.execute(query)
    conn.commit()
    print("data berhasil dihapus")
except Exception as e:
    print(e)