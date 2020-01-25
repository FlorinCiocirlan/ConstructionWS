from flask import Flask, render_template, url_for

app = Flask(__name__, static_folder="static", template_folder="template")


@app.route("/")
def home_route():
    return render_template("homepage.html")


if __name__ == "__main__":
    app.run(debug=True,
            port=5000)