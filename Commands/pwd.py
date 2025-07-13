# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#
# BY: Tonny-1001
#
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits.
#
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

from UsefulModules.help_msgs import help_pwd_msg
from UsefulModules.printing_in_frame import print_in_frame
from UsefulModules.styling import style

available_options = ["help"]


def pwd(options, current_directory):
    for opt in options:
        if opt not in available_options:
            if len(opt) > 1:
                opt = f"--{opt}"
            elif len(opt) == 1:
                opt = f"-{opt}"
            return print(f"{style.RED}Unknown option was used: '{opt}'. "
                         f"\nUse 'pwd --help' to get list of available options.{style.RESET}")

    if "help" in options:
        return print_in_frame(help_pwd_msg)

    print(current_directory)
