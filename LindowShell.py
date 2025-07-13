# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#
# BY: Tonny-1001
#
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits.
#
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

import os
import json
import subprocess
from sys import exit
import sys
import asyncio
import selectors
import atexit

from UsefulModules.styling import style
from UsefulModules.command_line_parser import parse
from UsefulModules.parse_prompt_style import parse_prompt_style

from Commands.ls import ls
from Commands.clear import clear
from Commands.touch import touch
from Commands.cat import cat
from Commands.write import write
from Commands.rm import rm
from Commands.help import help_
from Commands.cd import cd
from Commands.mkdir import mkdir
from Commands.pwd import pwd
from Commands.mv import mv
from Commands.cp import cp
from Commands.alias import alias
from Commands.aliases import aliases
from Commands.history import history
from Commands.ulib import ulib
from Commands.free import free
from Commands.env import env

from prompt_toolkit.completion import Completer, PathCompleter, Completion
from prompt_toolkit.document import Document
from prompt_toolkit.shortcuts import CompleteStyle
from prompt_toolkit.formatted_text import ANSI
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory

python_script_path = os.path.dirname(sys.argv[0])
__version__ = "v1.4.9"
selector = selectors.SelectSelector()
loop = asyncio.SelectorEventLoop(selector)
asyncio.set_event_loop(loop)


def clear_history():
    try:
        with open(f"{python_script_path}\\Config\\settings.json", "r") as f:
            settings = json.load(f)

        if settings["clear_history_on_close"]:
            with open(f"{python_script_path}\\Config\\session-history", "w") as f:
                f.write("")
    except Exception as e:
        print(e)


atexit.register(clear_history)


class UsefulTable:
    last_cmd = ""
    active_venv = [False, ""]


UsefulObject = UsefulTable()


class CommandCompleter(Completer):
    """
    Some magic stuff that is responsible for recursive file name completion.
    """

    def __init__(self, user_path=None):
        self.path_completer = PathCompleter()
        self.user_path = user_path

    def get_completions(self, document, complete_event):

        # replace ~ with user home dir
        document = Document(document.text.replace("~", self.user_path))
        document = Document(document.text.replace('"', ""))

        # do some other stuff...
        if document.text == "" or document.text.isspace():
            return
        else:
            if " " not in document.text:
                doc = document.text
            else:
                splitted = document.text.split(" ")
                splitted.remove(splitted[-1])
                joined = " ".join(splitted)
                pos = len(joined) + 1
                doc = document.text[pos:]
            sub_doc = Document(doc)
            yield from (Completion(completion.text, completion.start_position, display=completion.display)
                        for completion in self.path_completer.get_completions(sub_doc, complete_event, ))

def run_with_venv(venv_path, program, args=None):
    """
    Runs a python program using the specified virtual environment.
    """
    if args is None:
        args = []
    command = [venv_path+"\\Scripts\\python.exe", program] + args

    # Run the program using subprocess
    try:
        subprocess.run(command)
    except FileNotFoundError:
        print("Bad venv!\n(Make sure venv is up to date and it consists of correct path.)")
    except Exception as e:
        print("Unknown error occurred:", e)


def load_settings():
    try:
        with open(f"{python_script_path}\\Config\\settings.json", "r") as f:
            settings = json.load(f)
        assert type(settings["clear_history_on_close"]) == bool, "clear_history_on_close - accepted values true/false"
        assert type(settings["anonymous_mode"]) == bool, "anonymous_mode - accepted values true/false"
        return settings
    except Exception as e:
        print("Error in settings file:")
        print(e)
        print()
        input("Press enter to exit...")
        exit()


def shell():
    """
    When function is called it executes one command.
    """

    # open files that are important
    try:
        with open(f"{python_script_path}\\Config\\aliases.json", "r") as f:
            aliases_json = json.load(f)
    except FileNotFoundError:
        pass

    settings = load_settings()

    current_directory = os.getcwd()

    # just chilling here
    parsed_prompt = ""

    # try to parse and use style from prompt style file. If there's error return and don't start shell.
    try:
        login = os.getlogin()
        if settings["anonymous_mode"]:
            login = "Anon"

        parsed_prompt = parse_prompt_style(f"{python_script_path}\\Config\\prompt_style")
        if UsefulObject.active_venv[0]:
            parsed_prompt = parsed_prompt.format(login=login, style=style, cdir=current_directory, nline="\n",
                                                 mname=os.environ['COMPUTERNAME'], venv="(venv) ")
        else:
            parsed_prompt = parsed_prompt.format(login=login, style=style, cdir=current_directory, nline="\n",
                                                 mname=os.environ['COMPUTERNAME'], venv="")
    except Exception as e:
        print("Error in prompt_style file:")
        print(e)
        print()
        input("Press enter to exit...")
        exit()

    # cmd input prompt wow
    cmd_in = session.prompt(ANSI(f"\n{parsed_prompt} "),
                            completer=CommandCompleter(user_path=f"C:\\Users\\{os.getlogin()}"),
                            complete_style=CompleteStyle.READLINE_LIKE, auto_suggest=AutoSuggestFromHistory())

    # replace !! with last command
    # (maybe its stupid to use var but im lazy and i dont want to change it)
    cmd_in = cmd_in.replace("!!", UsefulTable.last_cmd)

    UsefulTable.last_cmd = cmd_in

    print()

    # parse entered text
    cmd = parse(cmd_in, python_script_path, user_path=f"C:\\Users\\{os.getlogin()}")

    # now check what we got from parse func
    if cmd["cmd"] == "ls":
        if len(cmd["arg"]) == 0:
            ls(current_directory, options=cmd["options"])
        else:
            if "\\" in cmd["arg"][0]:
                ls(cmd["arg"][0], options=cmd["options"])
            else:
                ls(current_directory, directory=cmd["arg"][0], options=cmd["options"])

    elif cmd["cmd"] == "clear":
        clear(cmd["options"])

    elif cmd["cmd"] == "touch":
        touch(cmd["arg"], cmd["options"], current_directory)

    elif cmd["cmd"] == "cat":
        cat(cmd["arg"], cmd["options"], current_directory)

    elif cmd["cmd"] == "write":
        write(cmd["arg"], cmd["options"], current_directory)

    elif cmd["cmd"] == "rm":
        rm(cmd["arg"], cmd["options"], current_directory)

    elif cmd["cmd"] == "mv":
        mv(cmd["arg"], cmd["options"], current_directory)

    elif cmd["cmd"] == "cp":
        cp(cmd["arg"], cmd["options"], current_directory)

    elif cmd["cmd"] == "help":
        if len(cmd["arg"]) == 0:
            help_()
        else:
            help_(cmd["arg"][0])

    elif cmd["cmd"] == "pwd":
        pwd(cmd["options"], current_directory)

    elif cmd["cmd"] == "exit":
        if UsefulObject.active_venv[0]:
            # Deleting venv from enviroment vars
            venv_path = UsefulObject.active_venv[1]
            scripts_path = os.path.join(venv_path, "Scripts")
            path_parts = os.environ["PATH"].split(os.pathsep)
            filtered_paths = []

            for p in path_parts:
                if scripts_path not in p:
                    filtered_paths.append(p)

            os.environ["PATH"] = os.pathsep.join(filtered_paths)
            os.environ.pop("VIRTUAL_ENV", None)
            UsefulObject.active_venv = [False, ""]
            print("(venv) Exited.")
        else:
            exit("Exited.")

    elif cmd["cmd"] == "cd":
        cd(cmd['arg'], cmd['options'], current_directory, os)

    elif cmd["cmd"] == "mkdir":
        mkdir(cmd["arg"], cmd["options"])

    elif cmd["cmd"] == "alias":
        alias(cmd["arg"], cmd["options"])

    elif cmd["cmd"] == "aliases":
        aliases(cmd["options"])

    elif cmd["cmd"] == "history":
        history(cmd["options"])

    elif cmd["cmd"] == "ulib":
        ulib(cmd["options"])

    elif cmd["cmd"] == "free":
        free(cmd["options"])

    elif cmd["cmd"] == "env":
        env(cmd["arg"], cmd["options"], current_directory, UsefulObject)

    else:
        if cmd["cmd"] != "dir" and cmd["cmd"] != "cls" and cmd["cmd"] != "help" and cmd["cmd"] != "cmd":
            if not cmd["arg"] and not cmd["options"]:
                if UsefulObject.active_venv[0]:
                    if cmd_in.endswith(".py"):
                        run_with_venv(UsefulObject.active_venv[1], cmd_in)
                    else:
                        os.system(cmd_in)
                else:
                    os.system(cmd_in)
            else:
                if UsefulObject.active_venv[0]:
                    if cmd["cmd"].endswith(".py"):
                        run_with_venv(UsefulObject.active_venv[1], cmd["cmd"], cmd["arg"])
                    else:
                        if cmd_in in aliases_json:
                            os.system(aliases_json[cmd_in])
                        else:
                            os.system(cmd_in)
                else:
                    if cmd_in in aliases_json:
                        os.system(aliases_json[cmd_in])
                    else:
                        os.system(cmd_in)

        else:
            print(f"'{cmd['cmd']}' is not recognized as an internal or external command,\n"
                  "operable program or batch file.")


if __name__ == "__main__":
    # program entry

    if not os.path.isdir(f"{python_script_path}\\Config"):
        print("Config folder not found.")
        input("Press enter to close...")
        exit()

    history_file = FileHistory(f"{python_script_path}\\Config\\session-history")
    session = PromptSession(history=history_file)

    print(f"Welcome to LindowShell. [{__version__}]\n")

    # main loop
    while True:
        try:
            shell()
        except KeyboardInterrupt:
            print("^C")
        except PermissionError:
            print(style.RED + "Access denied. You have no permission." + style.RESET)
        # except Exception as e:
        #     print(e)
