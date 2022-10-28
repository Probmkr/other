import threading
from flask import Flask

class APIThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True

    def run(self):
        api_app = Flask(__name__)
        from api.views import api
        api_app.register_blueprint(api, url_prefix="")

