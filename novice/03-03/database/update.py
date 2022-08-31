try:
    import psycopg2
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="wulan425")

    curs = conn.cursor()
    
    namaLama = "Rifka"
    namaBaru = "Rika"
    umurBaru = 20
    query = f"update santri set nama='{namaBaru}', umur={umurBaru} where nama='{namaLama}' "
   
    curs.execute(query)
    conn.commit()
    print("data berhasil diupdate")
except Exception as e:
    print(e)