from flask import Flask
from app.routes import main

app = Flask(
    __name__,
    template_folder='templates',
    static_folder='frontend',
    static_url_path='/static'
)

app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)