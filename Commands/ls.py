# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#
# BY: Tonny-1001
#
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits.
#
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

import datetime
import os
import stat

from UsefulModules.styling import style
from UsefulModules.printing_in_frame import print_in_frame
from UsefulModules.help_msgs import help_ls_msg

available_options = ["a", "all", "l", "listing", "help"]


def has_hidden_attribute(filepath):
    return bool(os.stat(filepath).st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN)


def ls(path, directory=None, options=None):
    if directory:
        path = path + "\\" + directory

    if options is None:
        options = []
    else:
        for opt in options:
            if opt not in available_options:
                if len(opt) > 1:
                    opt = f"--{opt}"
                elif len(opt) == 1:
                    opt = f"-{opt}"
                return print(f"{style.RED}Unknown option was used: '{opt}'. "
                             f"\nUse 'ls --help' to get list of available options.{style.RESET}")

    if "help" in options:
        return print_in_frame(help_ls_msg)

    if os.path.exists(path + "\\"):
        if "l" in options or "listing" in options:
            print("Type      Size          Mod. Date       Name")
            print("--------  ----------    --------------  --------")
            if len(path) == 2:
                for i in os.listdir(path + "\\"):
                    if i.startswith("NTUSER.DAT{") or i == "NTUSER.DAT" or i == "ntuser.ini" or i.startswith("ntuser.dat."):
                        continue
                    if os.path.isdir(path+"\\"+i):
                        size = os.path.getsize(path+'\\'+i)
                        space = ' '*(14 - len(str(size)))

                        mod_timestamp = os.path.getctime(path + "\\" + i)
                        mod_time = datetime.datetime.fromtimestamp(mod_timestamp).strftime("%b %d %H:%M")
                        space2 = " " * (16 - len(mod_time))
                        if has_hidden_attribute(path+"\\"+i):
                            if "a" in options or "all" in options:
                                print(
                                    f"{style.YELLOW}[DIR]{style.RESET}     {size}{space}{mod_time}{space2}{style.LIGHT}{i}{style.RESET}{style.BLACK}‍{style.RESET}")
                            else:
                                continue
                        else:
                            print(f"{style.YELLOW}[DIR]{style.RESET}     {size}{space}{mod_time}{space2}{i}")
                    elif i.endswith(".lnk"):
                        size = os.path.getsize(path + '\\' + i)
                        space = ' ' * (14 - len(str(size)))

                        mod_timestamp = os.path.getctime(path + "\\" + i)
                        mod_time = datetime.datetime.fromtimestamp(mod_timestamp).strftime("%b %d %H:%M")
                        space2 = " " * (16 - len(mod_time))
                        if has_hidden_attribute(path + "\\" + i):
                            if "a" in options or "all" in options:
                                print(
                                    f"{style.BLUE}[LINK]{style.RESET}    {size}{space}{mod_time}{space2}{style.LIGHT}{i}{style.RESET}{style.BLACK}‍{style.RESET}")
                            else:
                                continue
                        else:
                            print(f"{style.BLUE}[LINK]{style.RESET}    {size}{space}{mod_time}{space2}{i}")
                    elif os.path.isfile(path+"\\"+i):
                        size = os.path.getsize(path + '\\' + i)
                        space = ' ' * (14 - len(str(size)))

                        mod_timestamp = os.path.getctime(path + "\\" + i)
                        mod_time = datetime.datetime.fromtimestamp(mod_timestamp).strftime("%b %d %H:%M")
                        space2 = " " * (16 - len(mod_time))
                        if has_hidden_attribute(path + "\\" + i):
                            if "a" in options or "all" in options:
                                print(
                                    f"{style.CYAN}[FILE]{style.RESET}    {size}{space}{mod_time}{space2}{style.LIGHT}{i}{style.RESET}{style.BLACK}‍{style.RESET}")
                            else:
                                continue
                        else:
                            print(f"{style.CYAN}[FILE]{style.RESET}    {size}{space}{mod_time}{space2}{i}")

            else:
                for i in os.listdir(path):
                    if i.startswith("NTUSER.DAT{") or i == "NTUSER.DAT" or i == "ntuser.ini" or i.startswith("ntuser.dat."):
                        continue
                    if os.path.isdir(path+"\\"+i):
                        size = os.path.getsize(path + '\\' + i)
                        space = ' ' * (14 - len(str(size)))

                        mod_timestamp = os.path.getctime(path+"\\"+i)
                        mod_time = datetime.datetime.fromtimestamp(mod_timestamp).strftime("%b %d %H:%M")
                        space2 = " " * (16 - len(mod_time))
                        if has_hidden_attribute(path + "\\" + i):
                            if "a" in options or "all" in options:
                                print(f"{style.YELLOW}[DIR]{style.RESET}     {size}{space}{mod_time}{space2}{style.LIGHT}{i}{style.RESET}{style.BLACK}‍{style.RESET}")
                            else:
                                continue
                        else:
                            print(f"{style.YELLOW}[DIR]{style.RESET}     {size}{space}{mod_time}{space2}{i}")
                    elif i.endswith(".lnk"):
                        size = os.path.getsize(path + '\\' + i)
                        space = ' ' * (14 - len(str(size)))

                        mod_timestamp = os.path.getctime(path + "\\" + i)
                        mod_time = datetime.datetime.fromtimestamp(mod_timestamp).strftime("%b %d %H:%M")
                        space2 = " " * (16 - len(mod_time))
                        if has_hidden_attribute(path + "\\" + i):
                            if "a" in options or "all" in options:
                                print(
                                    f"{style.BLUE}[LINK]{style.RESET}    {size}{space}{mod_time}{space2}{style.LIGHT}{i}{style.RESET}{style.BLACK}‍{style.RESET}")
                            else:
                                continue
                        else:
                            print(f"{style.BLUE}[LINK]{style.RESET}    {size}{space}{mod_time}{space2}{i}")
                    elif os.path.isfile(path+"\\"+i):
                        size = os.path.getsize(path + '\\' + i)
                        space = ' ' * (14 - len(str(size)))

                        mod_timestamp = os.path.getctime(path + "\\" + i)
                        mod_time = datetime.datetime.fromtimestamp(mod_timestamp).strftime("%b %d %H:%M")
                        space2 = " " * (16 - len(mod_time))
                        if has_hidden_attribute(path + "\\" + i):
                            if "a" in options or "all" in options:
                                print(f"{style.CYAN}[FILE]{style.RESET}    {size}{space}{mod_time}{space2}{style.LIGHT}{i}{style.RESET}{style.BLACK}‍{style.RESET}")
                            else:
                                continue
                        else:
                            print(f"{style.CYAN}[FILE]{style.RESET}    {size}{space}{mod_time}{space2}{i}")

        else:
            if len(path) == 2:
                normal_data = os.listdir(path+"\\")
                for elem in normal_data:
                    if elem.startswith("NTUSER.DAT{"):
                        normal_data.remove(elem)
                data_list_tmp = os.listdir(path+"\\")
                data_list = []
                for elem in data_list_tmp:
                    if elem.startswith("NTUSER.DAT{"):
                        pass
                    else:
                        if has_hidden_attribute(path + "\\" + elem):
                            if "a" in options or "all" in options:
                                data_list.append(elem)
                            else:
                                continue
                        else:
                            data_list.append(elem)

                data = [data_list[x:x + 3] for x in range(0, len(data_list), 3)]

            else:
                normal_data = os.listdir(path)
                #print(normal_data)
                for elem in normal_data:
                    if elem.startswith("NTUSER.DAT{"):
                        normal_data.remove(elem)
                data_list_tmp = os.listdir(path)
                data_list = []
                for elem in data_list_tmp:
                    if elem.startswith("NTUSER.DAT{"):
                        pass
                    else:
                        if has_hidden_attribute(path + "\\" + elem):
                            if "a" in options or "all" in options:
                                data_list.append(elem)
                            else:
                                continue
                        else:
                            data_list.append(elem)

            # data_list = sorted(data_list, key=len)
            data = [data_list[x:x+3] for x in range(0, len(data_list), 3)]

            if len(data_list) == 0:
                return
            elif len(data_list) == 1:
                num_columns = 1
                num_rows = 1
            elif len(data_list) == 2:
                num_columns = 2
                num_rows = 2
            elif len(data_list) == 3:
                num_columns = 3
                num_rows = 3
            else:
                num_columns = round(len(data_list) / 3)
                num_rows = 3

            padded_lst = data_list + [''] * (num_rows * num_columns - len(data_list))
            if num_rows-1 == 0:
                step = 1
            else:
                step = num_rows
            columns = [padded_lst[i::step] for i in range(num_rows)]

            for elem in normal_data:
                if elem.startswith("NTUSER.DAT{"):
                    normal_data.remove(elem)

            for row in data:
                text = ""
                column_number = 0
                for i in row:
                    if has_hidden_attribute(path + "\\" + i):
                        if "a" in options or "all" in options:
                            if os.path.isdir(path + "\\" + i):
                                text = text + style.WHITE + "{: <%d}" % (len(max(columns[column_number], key=len))+2) + style.RESET

                        else:
                            break
                    else:
                        if os.path.isdir(path + "\\" + i):
                            text = text + style.YELLOW + "{: <%d}" % (len(max(columns[column_number], key=len)) + 2) + style.RESET
                        else:
                            text = text + style.CYAN + "{: <%d}" % (len(max(columns[column_number], key=len)) + 2) + style.RESET
                    column_number += 1
                    if column_number > 3:
                        column_number = 0

                print(text.format(*row))

    else:
        print(f"{style.RED}File does not exists!{style.RESET}")
