@app.route("/movie30", methods=["GET", "POST"])
def movie30():

    if request.method == "POST":

        movie = request.form.get("movie")
        year = request.form.get("year")

        return render_template(
            "result30.html",
            movie=movie,
            year=year
        )

    return render_template("index30.html")
