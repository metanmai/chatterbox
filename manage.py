from flask.cli import FlaskGroup

from app import app, db


def create_app():
    return app

cli = FlaskGroup(create_app=create_app)


@cli.command('initdb')
def initdb_command():
    db.create_all()
    print('Initialized the database.')

if __name__ == '__main__':
    cli()
