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

from UsefulModules.styling import style
from UsefulModules.printing_in_frame import print_in_frame
from UsefulModules.help_msgs import help_cat_msg

available_options = ["f", "framed", "help"]


def cat(args, options, cur_path):
    for opt in options:
        if opt not in available_options:
            if len(opt) > 1:
                opt = f"--{opt}"
            elif len(opt) == 1:
                opt = f"-{opt}"
            return print(f"{style.RED}Unknown option was used: '{opt}'. "
                         f"\nUse 'cat --help' to get list of available options.{style.RESET}")

    if "help" in options:
        return print_in_frame(help_cat_msg)

    try:
        file = args[0]
    except IndexError:
        return print(f"{style.RED}You need to specify file name!{style.RESET}")

    if "f" in options or "framed" in options:
        try:
            os.chdir(cur_path)
            with open(file, "r", encoding="utf-8") as f:
                print_in_frame(f.read(), f"File: {file}")
        except FileNotFoundError:
            return print(f"{style.RED}File not found!{style.RESET}")
        except Exception:
            return print(f"{style.RED}Not a text file or bad encoding!{style.RESET}")
    else:
        try:
            os.chdir(cur_path)
            with open(file, "r", encoding="utf-8") as f:
                print(f.read())
        except FileNotFoundError:
            return print(f"{style.RED}File not found!{style.RESET}")
        except Exception:
            return print(f"{style.RED}Not a text file or bad encoding!{style.RESET}")