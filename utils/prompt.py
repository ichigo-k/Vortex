from config.config import CURRENT_OS, CURRENT_DIR, HISTORY
from config.gen_ai_config import model


def prompt(instruction):
    message = f"""
        You are a precise AI assistant that translates natural language commands into shell commands for {CURRENT_OS}.

## Behavior:
- Translate the user instruction into a valid bash/zsh command.
- Use the history of commands and outputs only as context for the task at hand.
- If the new instruction is unrelated to the prior history, do not try to correlate them. Generate the appropriate shell command for the new task.
- Output only the next shell command in plain text, with no explanations or extra formatting.

## Rules:
- If the instruction is unrelated to previous tasks, ignore the history and output the required command based on the new instruction.
- If unsure about the next step, return a safe command (e.g., `cd ~` to the home directory).
- Use relative paths where possible (e.g., `~/Desktop`).
- Do not repeat prior steps unless necessary for the new task.
- Always prioritize executing the new task, even if it doesn't correlate with prior commands.

## Current Directory:
{CURRENT_DIR}

## History of previous commands:
{HISTORY}

## Instruction:
{instruction}

# Output:
Provide the exact shell command only, without explanations.
All output must be terminal executable no formatting or anything that can cause a system error
Things like ```shell or ```yml etc must be ignore only plain text is needed
Output that might cos an error must be avoided 
Output must be specific to {CURRENT_OS}

    """

    print(message)

    response = model.generate_content(message)
    return response.text
