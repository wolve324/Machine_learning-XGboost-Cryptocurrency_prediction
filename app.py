from flask import Flask, render_template
from prediction_agent import get_prediction

app = Flask(__name__)

@app.route("/")
def index():
    price = get_prediction()
    return render_template("index.html", predicted_price=f"{price:.2f}")

if __name__ == "__main__":
    app.run(debug=True)
