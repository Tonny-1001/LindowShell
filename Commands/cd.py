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
from UsefulModules.help_msgs import help_cd_msg
import re

available_options = ["help"]


def cd(args, options, current_directory, os):
    for opt in options:
        if opt not in available_options:
            if len(opt) > 1:
                opt = f"--{opt}"
            elif len(opt) == 1:
                opt = f"-{opt}"
            return print(f"{style.RED}Unknown option was used: '{opt}'. "
                         f"\nUse 'cd --help' to get list of available options.{style.RESET}")

    if "help" in options:
        return print_in_frame(help_cd_msg)

    try:
        path = args[0]
    except IndexError:
        return print(f"{style.RED}You need to specify destination!{style.RESET}")

    path = os.path.normpath(path.replace("/", "\\"))
    if os.path.exists(current_directory + f"\\{path}") and os.path.isdir(current_directory + f"\\{path}"):
        if len(current_directory) == 2:
            pass
        else:
            if ".." in path:
                tmp = list(filter(None, current_directory.split("\\")))
                num = path.count("..")
                if len(tmp) > num:
                    tmp_path = list(filter(None, current_directory.split("\\")))
                    for i in range(num):
                        tmp_path.pop(-1)

                    os.chdir(os.path.normpath("\\".join(tmp_path)+"\\"))

        if ".." not in path:
            if not current_directory.endswith("\\"):
                os.chdir(current_directory+os.path.normpath("\\"+path))
            else:
                os.chdir(current_directory+os.path.normpath(path))
    else:
        if re.match("^[A-Z]:\\.*", path) is not None:
            if os.path.exists(path):
                if "\\" not in path:
                    path = path + "\\"
                os.chdir(os.path.normpath(path))

            else:
                print(f"{style.RED}Directory does not exists.{style.RESET}")
        else:
            print(f"{style.RED}Directory does not exists.{style.RESET}")
