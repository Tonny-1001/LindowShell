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
from UsefulModules.help_msgs import help_alias_msg

available_options = ["r", "remove", "help"]


def alias(args, options):
    from LindowShell import python_script_path
    with open(f"{python_script_path}\\Config\\aliases.json", "r") as f:
        aliases = json.load(f)

    for opt in options:
        if opt not in available_options:
            if len(opt) > 1:
                opt = f"--{opt}"
            elif len(opt) == 1:
                opt = f"-{opt}"
            return print(f"{style.RED}Unknown option was used: '{opt}'. "
                         f"\nUse 'alias --help' to get list of available options.{style.RESET}")

    if "help" in options:
        return print_in_frame(help_alias_msg)

    try:
        cmd = ""
        alias_ = args[0]
        if "r" not in options:
            cmd = args[1]
    except IndexError:
        return print(f"{style.RED}You need to specify all arguments!{style.RESET}")

    if "alias" in alias_.lower():
        print(f"{style.RED}You cannot use this alias!{style.RESET}")
        return

    if options:
        if "r" in options or "remove" in options:
            try:
                aliases.pop(alias_)
            except KeyError:
                return print(f"{style.RED}This alias does not exist!{style.RESET}")

            with open(f"{python_script_path}\\Config\\aliases.json", "w") as f:
                json.dump(aliases, f, indent=4)

            print("Removed!")
            return
        else:
            if alias_ in aliases:
                acceptation = input("Alias already exists!\nSelect option: [o]-Overwrite/[c]-Cancel: ")
                if acceptation.lower() == "o":

                    aliases[alias_] = cmd

                    with open(f"{python_script_path}\\Config\\aliases.json", "w") as f:
                        json.dump(aliases, f, indent=4)

                    print("Saved!")
                    return

                else:
                    print("Action canceled.")
                    return

            else:
                aliases[alias_] = cmd

                with open(f"{python_script_path}\\Config\\aliases.json", "w") as f:
                    json.dump(aliases, f, indent=4)

                print("Saved!")
                return
    else:
        if alias_ in aliases:
            acceptation = input("Alias already exists!\nSelect option: [o]-Overwrite/[c]-Cancel: ")
            if acceptation.lower() == "o":

                aliases[alias_] = cmd

                with open(f"{python_script_path}\\Config\\aliases.json", "w") as f:
                    json.dump(aliases, f, indent=4)

                print("Saved!")
                return

            else:
                print("Action canceled.")
                return

        else:
            aliases[alias_] = cmd

            with open(f"{python_script_path}\\Config\\aliases.json", "w") as f:
                json.dump(aliases, f, indent=4)

            print("Saved!")
            return
