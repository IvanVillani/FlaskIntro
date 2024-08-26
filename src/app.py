import os
from flask import Flask
from dotenv import load_dotenv

from config import create_app
from pilots.routes import register_routes

flaskHost = "127.0.0.1"

if os.getenv("FLASK_ENV") != "production":
    load_dotenv()
else:
    flaskHost = "0.0.0.0"

app: Flask = create_app(os.getenv("CONFIG_MODE"))

register_routes(app)


@app.route("/")
def index():
    return "Hi from Ivan!"


if __name__ == "__main__":
    app.run(host=flaskHost, debug=True)
