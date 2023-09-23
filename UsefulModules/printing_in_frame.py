# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#
# BY: Tonny-1001
#
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits.
#
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def print_in_frame(text, title=None, characters=None):
    if characters is None:
        characters = ["║", "═", "╔", "╗", "╚", "╝", "╠", "╣"]
    splitted_text = text.split("\n")
    try:
        splitted_text.remove("")
    except ValueError:
        pass
    counter = 0
    for elem in splitted_text:
        splitted_text[counter] = elem.replace("\t", "    ")
        counter += 1

    splitted_title = title
    if splitted_title:
        if "\n" in splitted_title:
            splitted_title = splitted_title.split("\n")
            try:
                splitted_title.remove("")
            except ValueError:
                pass
            counter = 0
            for elem in splitted_title:
                splitted_title[counter] = elem.replace("\t", "    ")
                counter += 1
            if len(max(splitted_title, key=len)) >= len(max(splitted_text, key=len)):
                multiplayer = len(max(splitted_title, key=len)) + 2
                multiplayer2 = len(max(splitted_title, key=len))
            else:
                multiplayer = len(max(splitted_text, key=len)) + 2
                multiplayer2 = len(max(splitted_text, key=len))
        else:
            if len(splitted_title) >= len(max(splitted_text, key=len)):
                multiplayer = len(splitted_title) + 2
                multiplayer2 = len(splitted_title)
            else:
                multiplayer = len(max(splitted_text, key=len)) + 2
                multiplayer2 = len(max(splitted_text, key=len))
    else:
        multiplayer = len(max(splitted_text, key=len)) + 2
        multiplayer2 = len(max(splitted_text, key=len))

    if not title:
        vertical = characters[1] * multiplayer
        print(f"{characters[2]}{vertical}{characters[3]}")
        for line in splitted_text:
            if not line.isspace():
                space_multiplayer = len(max(splitted_text, key=len)) - len(line)
                print(f"{characters[0]} {line}{' ' * space_multiplayer} {characters[0]}")
        print(f"{characters[4]}{vertical}{characters[5]}")
    else:
        vertical = characters[1] * multiplayer
        print(f"{characters[2]}{vertical}{characters[3]}")

        if type(splitted_title) == list:
            for line in splitted_title:
                if not line.isspace():
                    if len(max(splitted_title, key=len)) >= len(max(splitted_text, key=len)):
                        space_multiplayer = len(max(splitted_title, key=len)) - len(line)
                    else:
                        space_multiplayer = len(max(splitted_text, key=len)) - len(line)
                    print(f"{characters[0]} {line}{' ' * space_multiplayer} {characters[0]}")
        else:
            if not splitted_title.isspace():
                if len(max(splitted_title, key=len)) >= len(max(splitted_text, key=len)):
                    space_multiplayer = len(max(splitted_title, key=len)) - len(splitted_title)
                else:
                    space_multiplayer = len(max(splitted_text, key=len)) - len(splitted_title)
                print(f"{characters[0]} {splitted_title}{' ' * space_multiplayer} {characters[0]}")

        print(characters[6] + characters[1] * (multiplayer2+2) + characters[7])

        if type(splitted_text) == list:
            for line in splitted_text:
                if not line.isspace():
                    if type(splitted_title) != list:
                        if len(splitted_title) >= len(max(splitted_text, key=len)):
                            space_multiplayer = len(splitted_title) - len(line)
                        else:
                            space_multiplayer = len(max(splitted_text, key=len)) - len(line)
                    else:
                        if len(max(splitted_title, key=len)) >= len(max(splitted_text, key=len)):
                            space_multiplayer = len(max(splitted_title, key=len)) - len(line)
                        else:
                            space_multiplayer = len(max(splitted_text, key=len)) - len(line)
                    print(f"{characters[0]} {line}{' ' * space_multiplayer} {characters[0]}")
        else:

            for line in splitted_text:
                if not line.isspace():
                    if len(str(splitted_title)) >= len(max(splitted_text, key=len)):
                        space_multiplayer = len(max(splitted_title, key=len)) - len(line)
                    else:
                        space_multiplayer = len(max(splitted_text, key=len)) - len(line)
                    print(f"{characters[0]} {line}{' ' * space_multiplayer} {characters[0]}")

        print(f"{characters[4]}{vertical}{characters[5]}")
