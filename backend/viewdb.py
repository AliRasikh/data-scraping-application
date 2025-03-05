
from config import app, db
from core.models import User, History

def view_data():
    with app.app_context():
        print("\n=== USERS ===")
        users = User.query.all()
        if not users:
            print("No users found in database.")
        for user in users:
            print(f"ID: {user.id}, Email: {user.email}, Name: {user.first_name}")
        
        print("\n=== HISTORY ===")
        history = History.query.all()
        if not history:
            print("No history records found in database.")
        for record in history:
            print(f"ID: {record.id}, User ID: {record.user_id}, URL: {record.url}")
            print(f"  Date: {record.date.strftime('%Y-%m-%d %H:%M:%S') if record.date else 'None'}")
            print(f"  Content preview: {record.content[:50]}..." if record.content else "  No content")
            print()

if __name__ == "__main__":
    view_data()