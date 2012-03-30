import flask
app = flask.Flask(__name__)

@app.route("/")
def home():
    """ View for the home page for trustitlabs project """
    return flask.render_template("index.html", title="bienvenue", page_name="home")

@app.route("/vision")
def vision():
    """ View for page with description of the trustitlabs project """
    return flask.render_template("vision.html", title="vision", page_name="vision")

@app.route("/people")
def people():
    """ View for page with description of trustitlabs' team members """
    return flask.render_template("people.html", title="people", page_name="people")

@app.route("/research")
def research():
    """ View for page with research publications and materials """
    return flask.render_template("research.html", title="research", page_name="research")

@app.route("/progress")
def progress():
    """ Information about the progress of software development for trustit labs """
    return flask.render_template("progress.html", title="progress", page_name="progress")

@app.route("/news")
def news():
    """ View for the news page/feed for trustitlabs project """
    return flask.render_template("news.html", title="news", page_name="news")

if __name__ == "__main__":
    app.run()
