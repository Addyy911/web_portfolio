from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # Needed for flash messages

# Store form submissions in memory (can be replaced with DB later)
messages = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    projects = [
        {"title": "Flask Portfolio", "desc": "Portfolio built with Flask & Bootstrap"},
        {"title": "Info System", "desc": "Online ordering and management system"}
    ]
    return render_template('projects.html', projects=projects)

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        if name and email and message:
            messages.append({"name": name, "email": email, "message": message})
            flash("✅ Your message has been sent successfully!", "success")
            return redirect(url_for("contact"))
        else:
            flash("⚠️ Please fill in all fields.", "danger")

    return render_template("contact.html", messages=messages)

@app.route('/projects/menuli')
def project_menuli():
    return render_template('project_menuli.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
