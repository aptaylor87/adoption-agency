from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

"""This seeds the db with 2 cats."""

Pet.query.delete()
p1 = Pet(name='Thor', species='Cat', photo_url='https://styles.redditmedia.com/t5_2qnlf/styles/communityIcon_bckbrah432281.jpg?width=256&s=4bb6ea857139ce6a5e1bd7e71fe238387839758a', age=12, notes='Test test test', available=True)
p2 = Pet(name='Loki', species='Cat', photo_url='https://styles.redditmedia.com/t5_2yb9w/styles/communityIcon_lqalsz65mlf51.jpg?width=256&s=1d128b09291e6a56cb9a8c770006e2ed7440daec', age=5, notes='Test test test', available=False)

db.session.add_all([p1, p2])
db.session.commit()
