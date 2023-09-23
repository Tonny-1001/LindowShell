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


def cd(args, options):
    from LindowShell import python_script_path

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

    with open(f"{python_script_path}\\path", "r") as f:
        cur_path = f.read()
    path = os.path.normpath(path.replace("/", "\\"))
    if os.path.exists(cur_path + f"\\{path}") and os.path.isdir(cur_path + f"\\{path}"):
        if len(cur_path) == 2:
            pass
        else:
            if ".." in path:
                tmp = list(filter(None, cur_path.split("\\")))
                num = path.count("..")
                if len(tmp) > num:
                    with open(f"{python_script_path}\\path", "r") as f:
                        tmp_path = list(filter(None, f.read().split("\\")))
                        for i in range(num):
                            tmp_path.pop(-1)

                    with open(f"{python_script_path}\\path", "w") as f:
                        f.write(os.path.normpath("\\".join(tmp_path)+"\\"))

        if ".." not in path:
            if not cur_path.endswith("\\"):
                with open(f"{python_script_path}\\path", "a") as f:
                    f.write(os.path.normpath("\\"+path))
            else:
                with open(f"{python_script_path}\\path", "a") as f:
                    f.write(os.path.normpath(path))
    else:
        if re.match("^[A-Z]:\\.*", path) is not None:
            if os.path.exists(path):
                if "\\" not in path:
                    path = path + "\\"
                with open(f"{python_script_path}\\path", "w") as f:
                    f.write(os.path.normpath(path))

            else:
                print(f"{style.RED}Directory does not exists.{style.RESET}")
        else:
            print(f"{style.RED}Directory does not exists.{style.RESET}")
