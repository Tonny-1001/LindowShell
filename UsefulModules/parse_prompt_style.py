

def parse_prompt_style(file):
    try:
        with open(f"{file}", "r", encoding="UTF-8") as f:
            promt_style = f.read()
    except FileNotFoundError:
        pass

    promt = promt_style.split("<endofprompt>")[0].split("<startofprompt>")[-1]
    return promt