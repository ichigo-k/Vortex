import subprocess
from datetime import datetime
import json
import click

from config.config import CURRENT_OS, HISTORY
from utils.prompt import prompt
import pyperclip
import pyautogui

pyautogui.FAILSAFE = False
def process_task(task, second_time, success):
    try:
        timestamp = datetime.now().strftime("%d/%m/%Y:%H:%M:%S:%f")
        key_prefix = f"{timestamp}"

        command = prompt(task)

        if "done" in command:
            return

        HISTORY[f"{key_prefix} [USER INPUT]"] = task
        if not second_time:
            click.secho("Vortex is thinking ...", fg="blue")
        else:
            if not success:
                 click.secho("Vortex is reevaluating  ...", fg="yellow")
            else:
                click.secho("Vortex is continuing execution ...", fg="magenta")


        HISTORY[f"{key_prefix} [AI RUN]"] = command

        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = result.stdout.strip() if result.stdout else result.stderr.strip()

        HISTORY[f"{key_prefix} [OUTPUT]"] = output


        if "cd" in command or "CD" in command:
            pyperclip.copy(command)
            if CURRENT_OS == "Windows":
                pyautogui.hotkey('ctrl', 'v')
            else:
                pyautogui.hotkey('ctrl', 'shift', 'v')
            pyautogui.hotkey('enter')
        else:
            click.secho(output)

        if len(HISTORY) > 9:
            last_keys = list(HISTORY.keys())[-3:]
            for key in last_keys:
                del HISTORY[key]

        with open("logs.json", "w") as f:
            json.dump(HISTORY, f, indent=4)

        if result.stderr:
            process_task("execute shell command to fix this", True, False)

        if result.stdout:
                process_task("continue this execution", True, True)

    except Exception as e:
        click.secho("Something went wrong, please try again later!", fg="red")
        print(e)