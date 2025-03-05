from app import app, db
from core.models import User, History

with app.app_context():
    db.create_all()
    print("Baza de date a fost creată cu succes!")