from flask import Flask, render_template, request
import os

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
    port = int(os.environ.get("PORT", 5000))  # ✅ Use PORT env if available
    app.run(debug=False, host="0.0.0.0", port=port)
