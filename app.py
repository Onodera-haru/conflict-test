from flask import flask, render_template

app = flask(__name__)

@app.route("/")
def top_page();
    return render_template("index.html")

    if __name__ =="__ main__";
        app.run(debug=True)

from flask import Flask, render_template, request

@app.route("/circle_input")
def circle_input();
    return render_template("circle_input.html")

@app.route("/circle_result")
def circle_result();
    radius = int(request.args.get("radius"))
	result = 3.14 * radius ** 2
	return render_template("circle_result.html", result=result)
