from flask import Flask, render_template, abort

app = Flask(__name__)

projects = [
    {
        "name": "Habit tracking app with Python and MongoDB",
        "thumb": "img/habit-tracking.png",
        "hero": "img/habit-tracking-hero.png",
        "categories": ["python", "web"],
        "slug": "habit-tracking",
        "prod": "https://habit-tracker-i9ml.onrender.com"
    },
    {
        "name": "Microblog app with Python and MongoDB",
        "thumb": "img/personal-finance.png",
        "hero": "img/personal-finance.png",
        "categories": ["python", "web"],
        "slug": "microblog",
        "prod": "https://microblog-5ivn.onrender.com"
    },
    {
        "name": "Portfolio app with Python",
        "thumb": "img/rest-api-docs.png",
        "hero": "img/rest-api-docs.png",
        "categories": ["python", "web"],
        "slug": "portfolio",
        "prod": "https://microblog-5ivn.onrender.com"
    },
]

slug_to_projects = {project["slug"]: project for project in projects}


@app.route("/")
def home():
    return render_template("home.html", projects=projects)


@app.route("/about")
def about():
    return render_template("about.html")
    s


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_projects:
        abort(494)
    return render_template(f"project_{slug}.html", project=slug_to_projects[slug])


@app.errorhandler(404)
def page_not_found(error):
    return render_template("error_page.html")