# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#
# BY: Tonny-1001
#
#
# This project can be used_ram freely for all uses, as long as they maintain the
# respective credits.
#
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

from psutil import virtual_memory, swap_memory
from UsefulModules.styling import style
from UsefulModules.printing_in_frame import print_in_frame
from UsefulModules.help_msgs import help_free_msg

available_options = ["help", "h", "human", "b", "bytes", "k", "kilo", "m", "mega", "g", "giga"]


def free(options):
    if options is None:
        options = []
    else:
        for opt in options:
            if opt not in available_options:
                if len(opt) > 1:
                    opt = f"--{opt}"
                elif len(opt) == 1:
                    opt = f"-{opt}"
                return print(f"{style.RED}Unknown option was used_ram: '{opt}'. "
                             f"\nUse 'free --help' to get list of available options.{style.RESET}")

    if "help" in options:
        return print_in_frame(help_free_msg)

    total_ram = virtual_memory()[0]
    used_ram = virtual_memory()[3]
    free_ram = virtual_memory()[4]

    total_swap = swap_memory()[0]
    used_swap = swap_memory()[1]
    free_swap = swap_memory()[2]

    if "h" in options or "human" in options:
        total_ram = f"{round(total_ram / 1073741824, 1)}GB"
        used_ram = f"{round(used_ram / 1073741824, 1)}GB"
        free_ram = f"{round(free_ram / 1073741824, 1)}GB"

        total_swap = f"{round(total_swap / 1073741824, 1)}GB"
        used_swap = f"{round(used_swap / 1073741824, 1)}GB"
        free_swap = f"{round(free_swap / 1073741824, 1)}GB"

        space1r = (13 - len(total_ram)) * " "
        space2r = (13 - len(used_ram)) * " "

        space1s = (13 - len(total_swap)) * " "
        space2s = (13 - len(used_swap)) * " "

        print("          total        used         free")
        print("          --------     --------     --------")
        print(f"Mem:      {total_ram}{space1r}{used_ram}{space2r}{free_ram}")
        print(f"Swap:     {total_swap}{space1s}{used_swap}{space2s}{free_swap}")
    elif "b" in options or "bytes" in options:
        space1 = (13 - len(str(total_ram))) * " "
        space2 = (13 - len(str(used_ram))) * " "

        space1s = (13 - len(str(total_swap))) * " "
        space2s = (13 - len(str(used_swap))) * " "

        print("          total        used         free")
        print("          --------     --------     --------")
        print(f"Mem:      {total_ram}{space1}{used_ram}{space2}{free_ram}")
        print(f"Swap:     {total_swap}{space1s}{used_swap}{space2s}{free_swap}")
    elif "m" in options or "mega" in options:
        total_ram = f"{int(total_ram / 1048576)}"
        used_ram = f"{int(used_ram / 1048576)}"
        free_ram = f"{int(free_ram / 1048576)}"

        total_swap = f"{int(total_swap / 1048576)}"
        used_swap = f"{int(used_swap / 1048576)}"
        free_swap = f"{int(free_swap / 1048576)}"

        space1r = (13 - len(total_ram)) * " "
        space2r = (13 - len(used_ram)) * " "

        space1s = (13 - len(total_swap)) * " "
        space2s = (13 - len(used_swap)) * " "

        print("          total        used         free")
        print("          --------     --------     --------")
        print(f"Mem:      {total_ram}{space1r}{used_ram}{space2r}{free_ram}")
        print(f"Swap:     {total_swap}{space1s}{used_swap}{space2s}{free_swap}")
    elif "g" in options or "giga" in options:
        total_ram = f"{int(total_ram / 1073741824)}"
        used_ram = f"{int(used_ram / 1073741824)}"
        free_ram = f"{int(free_ram / 1073741824)}"

        total_swap = f"{int(total_swap / 1073741824)}"
        used_swap = f"{int(used_swap / 1073741824)}"
        free_swap = f"{int(free_swap / 1073741824)}"

        space1r = (13 - len(total_ram)) * " "
        space2r = (13 - len(used_ram)) * " "

        space1s = (13 - len(total_swap)) * " "
        space2s = (13 - len(used_swap)) * " "

        print("          total        used         free")
        print("          --------     --------     --------")
        print(f"Mem:      {total_ram}{space1r}{used_ram}{space2r}{free_ram}")
        print(f"Swap:     {total_swap}{space1s}{used_swap}{space2s}{free_swap}")
    else:
        total_ram = f"{int(total_ram / 1024)}"
        used_ram = f"{int(used_ram / 1024)}"
        free_ram = f"{int(free_ram / 1024)}"

        total_swap = f"{int(total_swap / 1024)}"
        used_swap = f"{int(used_swap / 1024)}"
        free_swap = f"{int(free_swap / 1024)}"

        space1r = (13 - len(total_ram)) * " "
        space2r = (13 - len(used_ram)) * " "

        space1s = (13 - len(total_swap)) * " "
        space2s = (13 - len(used_swap)) * " "

        print("          total        used         free")
        print("          --------     --------     --------")
        print(f"Mem:      {total_ram}{space1r}{used_ram}{space2r}{free_ram}")
        print(f"Swap:     {total_swap}{space1s}{used_swap}{space2s}{free_swap}")
