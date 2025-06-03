import json
import os
import platform

from dotenv import load_dotenv
load_dotenv()


try:
    with open("logs.json", "r") as f:
        HISTORY = json.load(f)

    if len(HISTORY) > 8:
        oldest_key = next(iter(HISTORY))
        del HISTORY[oldest_key]

except Exception as e:
    HISTORY = {}
CURRENT_DIR=os.getcwd()
CURRENT_OS= platform.system()
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")


