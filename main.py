import os
from datetime import datetime
import click
import json
from config.config import HISTORY
from utils.prompt import prompt
import pyperclip
import pyautogui



pyautogui.FAILSAFE = False

@click.group
def cli():
    pass

@click.command(help="Accepts a task and provides an output")
@click.argument("task", default="Hello")
def solve(task):
    try:
        timestamp = datetime.now().strftime("%d/%m/%Y:%f")
        HISTORY[f"{timestamp} [USER INPUT]"] = task
        click.secho("Vortex is thinking ...", fg="blue")
        command = prompt(task)

        HISTORY[f"{timestamp} [AI RUN]"]= command

        pyperclip.copy(command)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.hotkey('enter')

        # HISTORY[f"{timestamp} [OUTPUT]"]= result.stdout


        if not os.path.exists("logs.json"):
            with open("logs.json", "w") as f:
                json.dump({}, f, indent=4)

        with open("logs.json", "w") as f:
            json.dump(HISTORY, f, indent=4)


    except Exception as e:
        click.secho("Something went wrong please try again later!", fg="red")
        print(e)


if __name__ == "__main__":
    solve()