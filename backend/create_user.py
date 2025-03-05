from app import app, db
from core.models import User
from werkzeug.security import generate_password_hash

# Datele utilizatorului pe care vrei să-l creezi
email = "test@example.com"
first_name = "Test"
password = "password123"

with app.app_context():
    # Verifică dacă utilizatorul există deja
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        print(f"Utilizatorul cu email-ul {email} există deja.")
    else:
        # Creează un nou utilizator
        new_user = User(
            email=email,
            first_name=first_name,
            password=generate_password_hash(password, method="pbkdf2:sha256"),
        )
        # Adaugă utilizatorul în baza de date
        db.session.add(new_user)
        db.session.commit()
        print(f"Utilizatorul {email} a fost creat cu succes!")