import json
import click
from utils.process_task import process_task

@click.group()
def cli():
    pass



@click.command(help="Accepts a task and provides an output")
@click.argument("task", default="Hello")
def solve(task):
   process_task(task,False, True)


@click.command(help="Accepts a task and provides an output")
def flush():
    with open("logs.json", "w") as f:
        json.dump({}, f, indent=4)

cli.add_command(solve)
cli.add_command(flush)

if __name__ == "__main__":
    cli()
