from flask import Flask, render_template, request
import psycopg2 

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="wulan425")
    curs = conn.cursor()

    
    if request.method == "POST":
        nama = request.form.get("nama")
        detail = request.form.get("detail")
        query = f"insert into buah(nama, detail) values('{nama}', '{detail}')"
        curs.execute(query)
        conn.commit()
        curs.close()
        conn.close()

        print(request.method)
    query = f"select * from buah"
    curs.execute(query)
    data = curs.fetchall()
    # data = ["pisang", "mangga", "salak"]
        
        # print(30*"=")
        # print(nama)
        # print(detail)
        # print(30*"=")

    # print(request.method)
    # print(30*"=")
    # print(request.form)
    # print(request.form.get("nama"))
    # print(request.form.get("detail"))
    # print(30*"=")
    # data = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Ahad"]
    return render_template("index.html", context=data)

if __name__ == "__main__":
    app.run()