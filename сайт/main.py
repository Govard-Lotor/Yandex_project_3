from flask import Flask
from flask import render_template
import sqlite3


app = Flask(__name__)


class Data:
    def get(self):
        con = sqlite3.connect("data/main.db")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM commands""").fetchall()
        con.close()
        return result


@app.route('/')
@app.route('/index')
def index():
    return render_template('main.html')


@app.route('/commands')
def commands():
    d = Data()
    main_list = d.get()
    return render_template('commands.html', commands=main_list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
