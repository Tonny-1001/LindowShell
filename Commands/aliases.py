# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#
# BY: Tonny-1001
#
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits.
#
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

import json
from UsefulModules.styling import style
from UsefulModules.printing_in_frame import print_in_frame
from UsefulModules.help_msgs import help_aliases_msg

available_options = ["f", "framed", "help"]


def aliases(options):
    from LindowShell import python_script_path

    for opt in options:
        if opt not in available_options:
            if len(opt) > 1:
                opt = f"--{opt}"
            elif len(opt) == 1:
                opt = f"-{opt}"
            return print(f"{style.RED}Unknown option was used: '{opt}'. "
                         f"\nUse 'aliases --help' to get list of available options.{style.RESET}")

    if "help" in options:
        return print_in_frame(help_aliases_msg)

    if "f" in options or "framed" in options:
        with open(f"{python_script_path}\\Config\\aliases.json", "r") as f:
            aliases = json.load(f)

        text = ""
        for elem in aliases:
            text += f"{elem} -> {aliases[elem]}\n"

        if text == "":
            text = " "

        print_in_frame(text, "[alias] -> [command]")
    else:
        with open(f"{python_script_path}\\Config\\aliases.json", "r") as f:
            aliases = json.load(f)

        print("[alias] -> [command]")
        for elem in aliases:
            print(f"{elem} -> {aliases[elem]}")