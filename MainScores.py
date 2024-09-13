from flask import Flask
from flask import render_template

# creates a Flask application
app = Flask(__name__, template_folder='templates/')


@app.route("/")
def score_server():
    file = open('Utils.py', "r")
    read = file.read()
    for line in read.splitlines():
        if 'SCORES_FILE_NAME' in line:
            scoresfile = line.split('=',1)[1]
    try:
        with open(scoresfile, 'r') as file:
            read = file.read()
            return render_template('score.html', SCORE=read)
            file.close()
    except FileNotFoundError:
        return render_template('error.html', ERROR="No Score file found")




# run the application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
