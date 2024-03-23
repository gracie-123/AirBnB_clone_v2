#!/usr/bin/python3
"""script that starts a Flask web application"""
from models import storage
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.teardown_appcontext
def appcontext_teardown(exc=None):
    """script that starts a Flask web application"""
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def conditional_templating(id=None):
    """script that starts a Flask web application"""
    states = storage.all("State")
    if id is None:
        return render_template('9-states.html',
                               states=states)
    state = states.get('State.' + id)
    return render_template('9-states.html',
                           state=state)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
