from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def table_generator():
    number = None
    table = []
    if request.method == "POST":
        try:
            number = int(request.form["number"])
            table = [(number, i, number * i) for i in range(1, 11)]
        except ValueError:
            pass
    return render_template("index.html", number=number, table=table)

if __name__ == "__main__":
    app.run(debug=True)
