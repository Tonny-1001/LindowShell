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
import shutil
from UsefulModules.help_msgs import help_rm_msg
from UsefulModules.printing_in_frame import print_in_frame
from UsefulModules.styling import style

available_options = ["r", "recursive", "help"]


def rm(args, options, path):
    for opt in options:
        if opt not in available_options:
            if len(opt) > 1:
                opt = f"--{opt}"
            elif len(opt) == 1:
                opt = f"-{opt}"
            return print(f"{style.RED}Unknown option was used: '{opt}'. "
                         f"\nUse 'rm --help' to get list of available options.{style.RESET}")

    if "help" in options:
        return print_in_frame(help_rm_msg)

    if len(args) == 0:
        return print(f"{style.RED}You need to specify file name!{style.RESET}")

    if len(args) > 1:
        for file in args:
            try:
                try:
                    os.remove(path + "\\" + file)
                except PermissionError:
                    try:
                        os.rmdir(path + "\\" + file)
                    except OSError:
                        if "r" in options or "recursive" in options:
                            shutil.rmtree(path + "\\" + file)
                        else:
                            print(style.RED + f"The directory is not empty: `{file}`" + style.RESET)
            except FileNotFoundError:
                print(style.RED + f"File not found: `{file}`" + style.RESET)
    else:
        file = args[0]
        try:
            try:
                os.remove(path + "\\" + file)
            except PermissionError:
                try:
                    os.rmdir(path + "\\" + file)
                except OSError:
                    if "r" in options or "recursive" in options:
                        shutil.rmtree(path + "\\" + file)
                    else:
                        print(style.RED + f"The directory is not empty: `{file}`" + style.RESET)
            except OSError:
                print(style.RED + f"File not found: `{file}`" + style.RESET)
        except FileNotFoundError:
            print(style.RED + f"File not found: `{file}`" + style.RESET)