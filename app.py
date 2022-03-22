from flask import flask, render_template

app = flask(__name__)

@app.route("/")
def top_page();
    return render_template("index.html")

    if __name__ =="__ main__";
        app.run(debug=True)