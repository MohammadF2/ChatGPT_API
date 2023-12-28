import flask

from Blueprints.GPT3 import GPT_3
from waitress import serve
from Config.config import RUN_AS, DEBUG, PORT, ip, PRODUCTION, PROJECT_NAME

__name__ = PROJECT_NAME
app = flask.Flask(__name__)

app.register_blueprint(GPT_3, url_prefix='/GPT_3')

if RUN_AS == PRODUCTION:
    serve(app, host=ip, port=PORT)
else:
    app.run(host=ip, port=PORT, debug=DEBUG)
