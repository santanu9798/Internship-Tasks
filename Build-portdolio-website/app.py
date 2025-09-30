from flask import Flask,render_template,request, redirect,url_for,flash
import csv
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key="replace-this-with-a-secure-random-key" # change for production

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(DATA_DIR, exist_ok=True)
CONTACTS_FILE = os.path.join(DATA_DIR, "contacts.csv")

#Ensure csv header exists
if not os.path.exists(CONTACTS_FILE):
    with open(CONTACTS_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "name", "email", "subject", "massage"])
    
@app.route("/")
def index():
    #Example dynamic data passed to the templte
    personal = {
        "name": "Santanu",
        "title": "Software Developer",
        "bio": "Short bio about yourself. Replace this with something meaningful",
        "skills": ["python", "Flask", "HTML", "CSS", "Git"],
    }
    
    projects =[
        {"title": "Project A", "desc": "A small web app", "link": "#"},
        {"title": "project B", "desc": "Another project", "link": "#"},
    ]
    return render_template("index.html", personal=personal, projects=projects)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # Get form data
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        subject = request.form.get("subject", "").strip()
        message = request.form.get("message", "").strip()

        # Basic validation
        if not name or not email or not message:
            flash("Please fill in name, email, and message.", "error")
            return redirect(url_for("contact"))

        # Save to CSV (simple persistence for internship task)
        timestamp = datetime.utcnow().isoformat()
        with open(CONTACTS_FILE, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, name, email, subject, message])

        flash("Thanks! Your message has been received.", "success")
        return redirect(url_for("contact"))

    return render_template("contact.html")

# Static files (Flask serves /static automatically), error handlers optional
@app.errorhandler(404)
def not_found(e):
    return render_template("base.html", content="<h2>Page not found</h2>"), 404

if __name__ == "__main__":
    app.run(debug=True)