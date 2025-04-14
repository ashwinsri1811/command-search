# 📉 cmdmenu

A fast and simple CLI tool to search, copy, and manage frequently used terminal commands by their description or usage.  
Built for productivity—never forget or retype your go-to shell commands again!

---

## 🚀 Features

- 🔍 **Fuzzy Search** through saved commands by description or command text
- 🎯 **Keyboard Navigation** with numbered selection
- 📋 **Copy to Clipboard** on selection (no auto-execution for safety)
- ➕ **Add New Commands** interactively
- 📃 **List All Commands** with descriptions
- 💾 Commands stored in a local JSON file at `~/.cmdmenu_commands.json`

---

## 💠 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR_USERNAME/cmdmenu.git
   cd cmdmenu
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python3 -m venv ~/.venvs/cmdmenu
   source ~/.venvs/cmdmenu/bin/activate
   ```

3. Install the CLI tool locally:

   ```bash
   pip install -e .
   ```

4. (Optional) Add to your `PATH` (if not using virtualenv directly):

   ```bash
   echo 'export PATH="$PATH:$HOME/.venvs/cmdmenu/bin"' >> ~/.zshrc
   source ~/.zshrc
   ```

---

## 💡 Usage

### 📥 Add a new command:

```bash
cmdmenu --add
```

You’ll be prompted to enter:
- The command
- A description
- Optional usage info

---

### 🔍 Search and copy:

```bash
cmdmenu
```

Type a few keywords and select from the results using the number shown. The command is copied to your clipboard (not executed).

---

### 📃 List all saved commands:

```bash
cmdmenu --list
```

Displays all stored commands with their descriptions.

---

## 📁 Command Storage Format

Commands are saved in this JSON file:

```bash
~/.cmdmenu_commands.json
```

Example structure:

```json
[
  {
    "command": "git log --oneline",
    "description": "Show commit history in a single line",
    "usage": "Useful for quick summaries"
  }
]
```

---

