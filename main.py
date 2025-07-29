import click
import commands


@click.group()
def cli_commands():
    pass


cli_commands.add_command(commands.video)
cli_commands.add_command(commands.playlist)
if __name__ == "__main__":
    cli_commands()
