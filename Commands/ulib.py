# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#
# BY: Tonny-1001
#
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits.
#
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

from UsefulModules.help_msgs import help_ulib_msg
from UsefulModules.printing_in_frame import print_in_frame
from UsefulModules.styling import style

available_options = ["help"]


def ulib(options):
    for opt in options:
        if opt not in available_options:
            if len(opt) > 1:
                opt = f"--{opt}"
            elif len(opt) == 1:
                opt = f"-{opt}"
            return print(f"{style.RED}Unknown option was used: '{opt}'. "
                         f"\nUse 'ulib --help' to get list of available options.{style.RESET}")

    if "help" in options:
        return print_in_frame(help_ulib_msg)

    print_in_frame("""
Pygments            2.12.0
asttokens           2.0.5
commonmark          0.9.1
executing           0.8.3
importlib-metadata  4.11.3
ipython             8.3.0
lief                0.12.1
parso               0.8.3
pip                 21.3.1
prompt-toolkit      3.0.38
psutil              5.9.4
pure-eval           0.2.2
setuptools          60.2.0
six                 1.16.0
typing-extensions   4.2.0
wcwidth             0.2.5
wheel               0.37.1
zipp                3.8.0
    """, title="Libraries that were used to create Lindow:")
