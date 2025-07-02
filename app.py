from flask import Flask, render_template, request

app = Flask(__name__)
feedback_list = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        feedback = request.form.get("feedback")
        feedback_list.append((name, feedback))
    return render_template("index.html", feedbacks=feedback_list)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
