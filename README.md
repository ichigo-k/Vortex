# ⚡ Vortex — Bringing AI to Your Terminal

Vortex is your AI-powered command-line assistant. Just describe what you want to do in plain English, and Vortex will turn it into a real terminal command — Bash, CMD, or PowerShell. It’s like having ChatGPT in your terminal.

> 🧠 `vortex "create 10 folders named from Project1 to Project10"`  
> 💥 Done.

---

## ✨ Features

- 🤖 Natural Language to Terminal Command Conversion
- 🧠 Powered by Google Gemini Pro
- ⚙️ Works with Bash, CMD, and PowerShell
- 🪶 Lightweight and easy to use
- 🧪 Great for learning, scripting, and automation

---

## 🔧 Installation

```bash
git clone https://github.com/ichigo-k/Vortex
cd vortex
pip install -r requirements.txt
pip install . 
```

## 🔐 **NB**: Gemini API Key Required

To use Vortex, you'll need to provide a valid **Gemini API key**. This key is required for the AI processing to work.

### Steps to Set It Up:
1. **Get your Gemini API Key**:
   - Visit [Google's Gemini page](https://makersuite.google.com/app/apikey) to get your API key.

2. **Configure the Key**:
   - In the project folder, locate the `config/config.py` file.
   - Open it and add your API key as follows:

   ```python
   GEMINI_API_KEY = "your-gemini-api-key-here"
