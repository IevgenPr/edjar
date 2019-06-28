import os

from edjar import create_app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('EDJAR_ENV') or 'dev')
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def insert_data():
  user = User(username='User1', email='user1@example.com')
  db.session.add(user)

@manager.command
def initdb():
  db.create_all()
  db.session.add(User())
  db.session.commit()
  print('Initialized DB')


@manager.command
def dropdb():
  if prompt_bool("Are you sure you want to drop database?"):
    db.drop_all()
    print('Dropped DB')

if __name__ == "__main__":
  manager.run()
