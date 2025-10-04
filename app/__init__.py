from flask import Flask


def init_app(config=None) -> Flask:
    app = Flask(__name__, static_url_path="", static_folder='static')
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app
