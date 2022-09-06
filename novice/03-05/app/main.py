from flask import Flask, render_template, request, redirect
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

        print(request.method)
    query = f"select * from buah"
    curs.execute(query)
    data = curs.fetchall()
    # data = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Ahad"]
    return render_template("index.html", context=data)

@app.route("/detail/<buah_id>")
def detail (buah_id):
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="wulan425" 
    )

    curs = conn.cursor()
    query = f"select * from buah where id = {buah_id}"
    curs.execute(query)
    data = curs.fetchone()
    curs.close()
    conn.close()
    print(data)
    return render_template("detail.html", context=data)


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
@app.route("/delete/<buah_id>")
def delete(buah_id):
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="wulan425" 
    )

    curs = conn.cursor()
    query = f"delete from buah where id = {buah_id}"
    curs.execute(query)
    conn.commit()
    curs.close()
    conn.close()
    return redirect ("/")

@app.route("/update/<buah_id>", methods=["GET", "POST"])
def update (buah_id):
    conn = psycopg2.connect(
        host="localhost",
        database="contoh",
        user="postgres",
        password="wulan425" 
    )

    curs = conn.cursor()
    if request.method == "POST":
        nama = request.form.get("nama")
        detail = request.form.get("detail")
        query = f"update buah set nama = '{nama}', detail = '{detail}' where id = {buah_id}"
        curs.execute(query)
        conn.commit()
        return redirect("/")
        # print("data masuk")
    query = f"select * from buah where id = {buah_id}"
    curs.execute(query)
    data = curs.fetchone()
    curs.close()
    conn.close()
    return render_template("update.html", context = data)

if __name__ == "__main__":
    app.run()