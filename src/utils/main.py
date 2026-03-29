import os
import logging
from flask import Flask, render_template
from user_dashboard.config import Config
from user_dashboard.views import main_blueprint
from user_dashboard.models import db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

app.register_blueprint(main_blueprint)

@app.errorhandler(404)
def not_found_error(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)