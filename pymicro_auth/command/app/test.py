import click

from pymicro_auth import app_cli, db


@app_cli.command('test', help="Test Application Connection")
def app_cli_test():
    status = True
    status = status and test_database()
    if status:
        exit(0)

    exit(1)


def test_database():
    click.echo("Test DB Connection .... ", nl=False)
    try:
        if db.engine.execute("SELECT 1;").first() == 1:
            click.secho('SUCCESS', bold=True, fg='green')
            return True
        else:
            click.secho('WARNING', bold=True, fg='yellow')
            return True
    except:
        click.secho('FAILED', bold=True, fg='red')
        return False
