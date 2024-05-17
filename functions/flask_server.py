import sys
import os

# Ensure the app's directory is in the sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from app import app

from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix
from werkzeug.wrappers import Request, Response

app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1)

def handler(event, context):
    @Request.application
    def application(request):
        return Response('Hello from Flask!', mimetype='text/plain')

    return app
