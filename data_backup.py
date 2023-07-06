
from server import app, db, get_data
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

def create_all():
    with app.app_context():
        db.create_all()

def update_data():
    with app.app_context():
        get_data()

if __name__ == "__main__":
    create_all()
    update_data()
# Setup
engine = create_engine('postgresql://xjqwxqivxhtrde:016c28bf31785c503e6e217bcf16f399cf7290128db7950ce366574462ddda26@ec2-3-232-218-211.compute-1.amazonaws.com:5432/dcfbgfq1ac0qdm')
Session = sessionmaker(bind=engine)

# New session
session = Session()

# Query data
data = session.execute(text('SELECT * FROM beachdata'))
for row in data:
    print(row)

# Close session
session.close()
