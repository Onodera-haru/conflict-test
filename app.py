from flask import flask, render_template, request

app = flask(__name__)

@app.route("/")
def top_page();
    return render_template("index.html")
    
    if __name__ =="__ main__";
        app.run(debug=True)

@app.route("/square_input")
def square_input();
    return render_template("square_input.html")

@app.route("/square_result")
def square_result();
    height = int(request.args.get("height"))
    bottom = int(request.args.get("bottom"))
    result = height * bottom
    return render_template("square_result.html" , result=result)
        
        