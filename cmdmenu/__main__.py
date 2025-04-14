import json
import subprocess
import os
from pathlib import Path
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.formatted_text import HTML

COMMANDS_FILE = Path.home() / ".cmdmenu_commands.json"


def load_commands():
    if not COMMANDS_FILE.exists():
        return []
    with open(COMMANDS_FILE, "r") as f:
        return json.load(f)


def save_commands(commands):
    with open(COMMANDS_FILE, "w") as f:
        json.dump(commands, f, indent=2)


def add_command():
    cmd = input("Command: ")
    desc = input("Description: ")
    usage = input("Usage: ")
    data = load_commands()
    data.append({"command": cmd, "description": desc, "usage": usage})
    save_commands(data)
    print("Command added!")

def list_commands():
    if os.path.exists(COMMANDS_FILE):
        with open(COMMANDS_FILE, "r") as f:
            commands = json.load(f)
            if not commands:
                print("No commands found.")
                return
            print(f"{'Command':<30} {'Description'}")
            print("-" * 50)
            for cmd in commands:
                print(f"{cmd['command']:<30} {cmd['description']}")
    else:
        print("No commands found.")


def copy_to_clipboard(command):
    escaped_command = command.replace('"', '\\"')

    script = f'''
    set the clipboard to "{escaped_command}"
    '''

    subprocess.run(["osascript", "-e", script])


class CommandCompleter(Completer):
    def __init__(self, commands):
        self.commands = commands

    def get_completions(self, document, complete_event):
        text = document.text.lower()
        for cmd in self.commands:
            if text in cmd["command"].lower() or text in cmd["description"].lower():
                display = f"{cmd['command']}  —  {cmd['description']}"
                yield Completion(cmd["command"], start_position=-len(text), display=display)


def run_cli():
    commands = load_commands()
    if not commands:
        print("No commands found. Use --add to add a command.")
        return

    session = PromptSession()
    completer = CommandCompleter(commands)
    bindings = KeyBindings()

    @bindings.add("enter")
    def _(event):
        text = event.app.current_buffer.text
        match = next((cmd for cmd in commands if cmd["command"] == text), None)
        if match:
            copy_to_clipboard(match["usage"])
            event.app.exit()

    print("\n🔍 Type to search. Press Enter to select.")
    try:
        session.prompt(HTML("<b>Search:</b> "), completer=completer, key_bindings=bindings)
    except KeyboardInterrupt:
        print("\nExiting...")


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--add", action="store_true", help="Add a new command")
    parser.add_argument("--list", action="store_true", help="List all saved commands")
    args = parser.parse_args()

    if args.add:
        add_command()
    elif args.list:
        list_commands()
    else:
        run_cli()


if __name__ == "__main__":
    main()

