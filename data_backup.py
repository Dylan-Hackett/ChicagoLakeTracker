from server import  app,db, get_data

def create_all():
    with app.app_context():
        db.create_all()

def update_data():
    with app.app_context():
        get_data()

if __name__ == "__main__":
    create_all()
    update_data()
