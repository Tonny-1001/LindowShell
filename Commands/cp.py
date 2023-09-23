# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#
# BY: Tonny-1001
#
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits.
#
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

import shutil
from UsefulModules.styling import style
from UsefulModules.printing_in_frame import print_in_frame
from UsefulModules.help_msgs import help_cp_msg
import re

available_options = ["help"]


def cp(args, options, cur_path):
    for opt in options:
        if opt not in available_options:
            if len(opt) > 1:
                opt = f"--{opt}"
            elif len(opt) == 1:
                opt = f"-{opt}"
            return print(f"{style.RED}Unknown option was used: '{opt}'. "
                         f"\nUse 'cp --help' to get list of available options.{style.RESET}")

    if "help" in options:
        return print_in_frame(help_cp_msg)

    try:
        src_path = args[0]
        dest_path = args[1]
    except IndexError:
        return print(f"{style.RED}You need to specify source and destination!{style.RESET}")

    if src_path.count("/") == 0 or src_path.count("\\") == 0:
        src_path = cur_path + "\\" + src_path

    if dest_path.count(":") == 0:
        if dest_path.count("/") == 0 or dest_path.count("\\") == 0:
            dest_path = cur_path + "\\" + dest_path
    elif re.match("^[a-zA-Z]:$", dest_path) is not None:
        dest_path = dest_path + "\\"

    try:
        shutil.copy(src_path, dest_path)
        print("Success!")
    except FileNotFoundError:
        print(f"{style.RED}File not found: `{src_path}`{style.RESET}")
    except Exception as e:
        print(e)
