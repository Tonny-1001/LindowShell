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
from UsefulModules.help_msgs import help_mkdir_msg
from UsefulModules.styling import style
from UsefulModules.printing_in_frame import print_in_frame

available_options = ["help"]


def mkdir(args, options):
    for opt in options:
        if opt not in available_options:
            if len(opt) > 1:
                opt = f"--{opt}"
            elif len(opt) == 1:
                opt = f"-{opt}"
            return print(f"{style.RED}Unknown option was used: '{opt}'. "
                         f"\nUse 'mkdir --help' to get list of available options.{style.RESET}")

    if "help" in options:
        return print_in_frame(help_mkdir_msg)

    if len(args) == 0:
        return print(f"{style.RED}You need to specify directory name!{style.RESET}")

    if len(args) > 1:
        for dir_name in args:
            dir_name = dir_name.replace("/", "\\")
            os.system(f"mkdir {dir_name}")
    else:
        dir_name = args[0]
        dir_name = dir_name.replace("/", "\\")
        os.system(f'mkdir "{dir_name}"')


