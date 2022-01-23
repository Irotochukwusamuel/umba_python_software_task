from flask import Flask, render_template
from modules.validations import Validation
from blueprints.api import API_bp
import logging

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(API_bp)
validate = Validation()


if __name__ == '__main__':
    app.run()
