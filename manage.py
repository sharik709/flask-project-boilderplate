from flask.cli import FlaskGroup

from app import create_app


def create_flask_app():
    return create_app()


def create_cli():
    return FlaskGroup(create_app=create_flask_app)


cli = create_cli()


@cli.command('key:gen')
def createSharedKey():
    """Generate a shared key for the application"""
    import secrets
    key = secrets.token_urlsafe(32)

    with open('.env', 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        f.truncate()
        for line in lines:
            if line.startswith('SECRET_KEY'):
                line = f'SECRET_KEY={key}\n'
            f.write(line)
            break

    print(f'Generated key: {key} and saved to .env')

if __name__ == '__main__':
    cli()
