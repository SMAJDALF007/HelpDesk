from flask import Flask, render_template, redirect, request
from config import get_db

app = Flask(__name__)


@app.route("/tickets", methods=["GET", "POST"])
def ticket():

        db = get_db()
        cursor = db.cursor(dictionary=True)

        cursor.execute("SELECT * FROM tickets")

        tickets = cursor.fetchall()

        if request.method == "POST":

            ticket = request.form["ticket"]
            typ_problemu = request.form["typ_problemu"]
            popis = request.form["popis"]
            urgentnost = request.form["urgentnost"]
            oddeleni = request.form["oddeleni"]
            datum = request.form["datum"]
            stav = "Neřešeno"

            cursor.execute(
                "INSERT INTO tickets (ticket, typ_problemu, popis, urgentnost, oddeleni, datum, stav) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (ticket, typ_problemu, popis, urgentnost, oddeleni, datum, stav)
            )
            db.commit()

            cursor.close()
            db.close()
            return redirect("/tickets")

        cursor.close()
        db.close()
        return render_template("index.html", tickets=tickets)


@app.route("/tickets/smaz/<int:index>", methods=["POST"])
def smazat(index):
        db = get_db()
        cursor = db.cursor()

        cursor.execute("DELETE FROM tickets WHERE id = %s", (index,))
        db.commit()

        cursor.close()
        db.close()
        return redirect("/tickets")


@app.route("/tickets/stav/<int:index>", methods=["POST"])
def stav(index):
        stav = request.form["stav"]
        db = get_db()
        cursor = db.cursor()

        cursor.execute("UPDATE tickets SET stav = %s WHERE id = %s", (stav, index))
        db.commit()

        cursor.close()
        db.close()
        return redirect("/tickets")


if __name__ == "__main__":
      app.run(debug=True)