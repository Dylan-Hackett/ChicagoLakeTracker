from server import app, db, get_data

with app.app_context():
    db.create_all()
    get_data()