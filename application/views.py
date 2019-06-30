from flask import render_template, request, redirect, url_for, flash
from application import app

@app.route("/")
def index():
	return redirect(url_for("wishes_index"))
	# TODO: Add updates and other content to home page
	#return render_template("index.html")
