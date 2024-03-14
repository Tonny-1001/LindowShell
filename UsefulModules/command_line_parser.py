# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#
# BY: Tonny-1001
#
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits.
#
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

import json


def parse(text, python_script_path, user_path=None):
    """Parse command into smaller sections."""

    with open(f"{python_script_path}\\Config\\aliases.json", "r") as f:
        aliases = json.load(f)

    if text in aliases:
        text = aliases[text]

    if user_path:
        text = text.replace("~", user_path)

    if text.startswith('"') and text.endswith('"'):
        return {"cmd": text[1:-1], "arg": [], "options": []}

    string_active = False
    string = ""
    string_list = []

    options = []
    text2 = text.split(" ")
    to_remove = []
    for i in text2:
        if i.startswith("--") and not string_active:
            i_ = i.replace("--", "")
            options.append(i_)
            to_remove.append(i)
        elif i.startswith("-") and not string_active:
            i_ = i.replace("-", "")

            if len(i_) > 1:
                for _ in i_:
                    options.append(_)
            else:
                options.append(i_)
            to_remove.append(i)
        elif i.startswith('"') and not string_active:
            string_active = True
            string = string + i.replace('"', "") + " "
            to_remove.append(i)
        elif i.endswith('"') and string_active:
            string_active = False
            string += i.replace('"', "")
            string_list.append(string)
            to_remove.append(i)
            string = ""
        elif string_active:
            string = string + i + " "
            to_remove.append(i)

    for _ in to_remove:
        text2.remove(_)

    try:
        cmd = text2[0]
    except IndexError:
        return {"cmd": text[1:-1], "arg": [], "options": []}
    arg = text2[1:]
    for i in string_list:
        arg.append(i)
    arg = list(filter(None, arg))

    parsed = {"cmd": cmd.lower(), "arg": arg, "options": options}

    # if cmd.lower() == "mkdir":
    #     if text.count('"') % 2 == 0 and text.count('"') != 0:
    #         file_name = '"'+str(" ".join(arg))+'"'
    #     else:
    #         file_name = str(" ".join(arg))
    #     parsed = {"cmd": cmd.lower(), "arg": file_name, "options": options}
    # else:
    #     parsed = {"cmd": cmd.lower(), "arg": arg, "options": options}

    # It returns dict of data
    return parsed