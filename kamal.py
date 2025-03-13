from flask import*
import sqlite3

app=Flask(__name__)
app.secret_key='123'

con=sqlite3.connect("login.db")
con.execute("create table if not exists details(EMAIL varchar(50), USER varchar(30), PASSWORD varchar(20))")
con.commit()
con.close()

@app.route("/",methods=['GET','POST'])
def register():
    if request.method=='POST':
        e=request.form.get("email")
        n=request.form.get("name")
        p=request.form.get("password")
        con=sqlite3.connect("login.db")
        cur=con.cursor()
        cur.execute("insert into details(EMAIL,USER,PASSWORD)values(?,?,?)",(e,n,p))
        con.commit()
        con.close()
        flash(" submited for successfully","primary")
    return render_template("kamalregister.html")


@app.route("/login",methods=['GET','POST'])
def login():
    if request.method=='POST':
        n=request.form.get("name")
        p=request.form.get("password")
        con=sqlite3.connect("login.db")
        con.row_factory=sqlite3.Row
        cur=con.cursor()
        cur.execute("select * from details where user=? and password=?",(n,p))
        data=cur.fetchone()
        if data:
            session["name"]=data["user"]
            session["pass"]=data["password"]
            return redirect("result")
        else:
            flash("error : ","danger")

    return render_template("kamallogin.html")

@app.route("/result")
def result():
    return render_template("kamalresult.html")

if __name__=='__main__':
    app.run(debug=True)