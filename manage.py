from flask_script import Manager, Server
from server import app, db, models
from sqlalchemy_utils import database_exists
from config import DEBUG, DATABASE_URI


manager = Manager(app)

manager.add_command("run", Server())


@manager.command
def createdb():
    db.reflect()
    db.drop_all()
    db.create_all()
    print(f"Database successfully created at: {DATABASE_URI}")


if __name__ == "__main__":
    manager.run()
