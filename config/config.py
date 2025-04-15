import json
import os
import platform

from dotenv import load_dotenv
load_dotenv()


try:
    with open("logs.json", "r") as f:
        HISTORY=json.load(f)
except:
    HISTORY={}
CURRENT_DIR=os.getcwd()
CURRENT_OS= platform.system()
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")