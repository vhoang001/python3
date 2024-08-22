@app.route('/facts/new')
def new_fact():
    return render_template('new_fact.html')
