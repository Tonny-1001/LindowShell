# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#
# BY: Tonny-1001
#
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits.
#
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

from UsefulModules.help_msgs import help_touch_msg
from UsefulModules.printing_in_frame import print_in_frame
from UsefulModules.styling import style

available_options = ["help"]


def touch(args, options, path):
    for opt in options:
        if opt not in available_options:
            if len(opt) > 1:
                opt = f"--{opt}"
            elif len(opt) == 1:
                opt = f"-{opt}"
            return print(f"{style.RED}Unknown option was used: '{opt}'. "
                         f"\nUse 'touch --help' to get list of available options.{style.RESET}")

    if "help" in options:
        return print_in_frame(help_touch_msg)

    try:
        file_name = args[0]
    except IndexError:
        return print(f"{style.RED}You need to specify file name!{style.RESET}")

    with open(path + "\\" + file_name, "w", encoding="utf-8") as f:
        f.close()
