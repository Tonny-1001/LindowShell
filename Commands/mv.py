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
from UsefulModules.help_msgs import help_mv_msg
from UsefulModules.printing_in_frame import print_in_frame
import re

available_options = ["help"]


def mv(args, options, current_directory):
    for opt in options:
        if opt not in available_options:
            if len(opt) > 1:
                opt = f"--{opt}"
            elif len(opt) == 1:
                opt = f"-{opt}"
            return print(f"{style.RED}Unknown option was used: '{opt}'. "
                         f"\nUse 'mv --help' to get list of available options.{style.RESET}")

    if "help" in options:
        return print_in_frame(help_mv_msg)

    try:
        src_path = args[0]
        dest_path = args[1]
    except IndexError:
        return print(f"{style.RED}You need to specify source and destination!{style.RESET}")

    if src_path.count("/") == 0 or src_path.count("\\") == 0:
        src_path = current_directory + "\\" + src_path

    if dest_path.count(":") == 0:
        if dest_path.count("/") == 0 or dest_path.count("\\") == 0:
            dest_path = current_directory + "\\" + dest_path
    elif re.match("^[a-zA-Z]:$", dest_path) is not None:
        dest_path = dest_path + "\\"

    try:
        shutil.move(src_path, dest_path)
    except FileNotFoundError:
        print(f"{style.RED}File not found: `{src_path}`{style.RESET}")
