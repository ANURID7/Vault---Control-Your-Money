from flask import Flask, render_template

app = Flask(__name__)

# Landing Page (Login)
@app.route("/")
def login():
    return render_template("login.html", active_page="")

# Home Dashboard
@app.route("/home")
def home():
    return render_template("home.html", active_page="home")

# Insights
@app.route("/insights")
def insights():
    return render_template("insights.html", active_page="insights")

# Transactions
@app.route("/transactions")
def transactions():
    return render_template("transactions.html", active_page="transactions")

# Profile
@app.route("/profile")
def profile():
    return render_template("profile.html", active_page="profile")

# Chatbot
@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html", active_page="")

if __name__ == "__main__":
    app.run(debug=True)
