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
from UsefulModules.help_msgs import help_env_msg
from UsefulModules.styling import style
from UsefulModules.printing_in_frame import print_in_frame

available_options = ["help"]


def env(args, options, path, instance):
    for opt in options:
        if opt not in available_options:
            if len(opt) > 1:
                opt = f"--{opt}"
            elif len(opt) == 1:
                opt = f"-{opt}"
            return print(f"{style.RED}Unknown option was used: '{opt}'. "
                         f"\nUse 'env --help' to get list of available options.{style.RESET}")

    if "help" in options:
        return print_in_frame(help_env_msg)

    if len(args) == 0:
        if instance.active_venv[0]:
            print(f"Is active?   : {style.GREEN}Yes{style.RESET}")
            print(f"Active venv  : {instance.active_venv[1]}")
        else:
            print(f"Is active?   : {style.RED}No{style.RESET}")
            print(f"Active venv  : -")

    elif len(args) == 1:
        path = os.path.join(path, args[0]).replace("/", "\\")
        # path = "\\".join(path.split("\\")[:-1])
        try:
            with open(path, "r") as f:
                file_lines = f.readlines()
            for line in file_lines:
                if "VIRTUAL_ENV=" in line:
                    path = line.split("=")[1].replace("'", "").replace('"', "").replace("\n", "")
                    break

            instance.active_venv = [True, path]

            print("Activated.")
        except FileNotFoundError:
            return print(f"{style.RED}File not found!{style.RESET}")
        except Exception:
            return print(f"{style.RED}Not a text file or bad encoding!{style.RESET}")
    else:
        return print(f"{style.RED}Bad arguments!{style.RESET}")


