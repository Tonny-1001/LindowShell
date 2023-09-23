# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#
# BY: Tonny-1001
#
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits.
#
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

import subprocess
from UsefulModules.printing_in_frame import print_in_frame
from UsefulModules.help_msgs import *


def help_(cmd=None):
    from LindowShell import __version__
    if cmd is None:
        print_in_frame(help_msg.replace("__version__", __version__),
                       title="Welcome to Lindow shell!\n"
                             "Lindow allows you to use basic Linux commands in Windows terminal!\n"
                             "Also it adds other interesting functionalities to your terminal!")
    else:
        if cmd == "ls":
            print_in_frame(help_ls_msg)

        elif cmd == "cd":
            print_in_frame(help_cd_msg)

        elif cmd == "clear":
            print_in_frame(help_clear_msg)
        elif cmd == "cp":
            print_in_frame(help_cp_msg)

        elif cmd == "touch":
            print_in_frame(help_touch_msg)

        elif cmd == "cat":
            print_in_frame(help_cat_msg)

        elif cmd == "write":
            print_in_frame(help_write_msg)

        elif cmd == "alias":
            print_in_frame(help_alias_msg)

        elif cmd == "aliases":
            print_in_frame(help_aliases_msg)

        elif cmd == "rm":
            print_in_frame(help_rm_msg)

        elif cmd == "mv":
            print_in_frame(help_mv_msg)

        elif cmd == "pwd":
            print_in_frame(help_pwd_msg)

        elif cmd == "help":
            print_in_frame(help_help_msg)

        elif cmd == "history":
            print_in_frame(help_history_msg)

        elif cmd == "ulib":
            print_in_frame(help_ulib_msg)

        elif cmd == "mkdir":
            print_in_frame(help_mkdir_msg)

        elif cmd == "free":
            print_in_frame(help_free_msg)

        else:
            try:
                subprocess.run(['help', cmd])
            except Exception:
                print("Command not found!")
