from flask import Flask

from config import Config
from extensions import db, bcrypt

# Import Models
from models.user import User
from models.transaction import Transaction

# Import Blueprints
from routes.main import main
from routes.auth import auth
from routes.detect import detect
from routes.history import history

app = Flask(__name__)

app.config.from_object(Config)

# Initialize Extensions
db.init_app(app)
bcrypt.init_app(app)

# Register Blueprints
app.register_blueprint(main)
app.register_blueprint(auth)
app.register_blueprint(detect)
app.register_blueprint(history)

# Create Database Tables
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)