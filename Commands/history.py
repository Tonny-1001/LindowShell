# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#
# BY: Tonny-1001
#
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits.
#
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

from UsefulModules.printing_in_frame import print_in_frame
from UsefulModules.styling import style
from UsefulModules.help_msgs import help_history_msg

available_options = ["help"]


def history(options):
    from LindowShell import python_script_path
    for opt in options:
        if opt not in available_options:
            if len(opt) > 1:
                opt = f"--{opt}"
            elif len(opt) == 1:
                opt = f"-{opt}"
            return print(f"{style.RED}Unknown option was used: '{opt}'. "
                         f"\nUse 'history --help' to get list of available options.{style.RESET}")

    if "help" in options:
        return print_in_frame(help_history_msg)

    history_file = f"{python_script_path}\\Config\\session-history"

    with open(history_file, "r") as f:
        lines = f.read()

    print_in_frame(lines)
