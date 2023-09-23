# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#
# BY: Tonny-1001
#
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits.
#
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

help_msg = \
    f"""
Commands:
    alias   - Creates alias to specified command.
    aliases - Prints list of all aliases.
    cat     - Prints content of text file.
    cd      - Goes to specified directory.
    clear   - Clears console.
    cp      - Copies file/directory to specified directory
    free    - Prints info about memory.
    help    - Prints help to specified command.
    history - Prints saved session history.
    ls      - Lists files and directories in specified directory.
    mkdir   - Creates new directory.
    mv      - Moves file/directory to specified destination.
    pwd     - Prints current work directory.
    rm      - Removes specified directory or file.
    touch   - Creates text file.
    ulib    - Prints list of libraries that were used in project.
    write   - Writes data to text file.

version: __version__
author:  Tonny-1001
    """

help_ls_msg = \
    """
Lists files in specified directory.
Files are colored in blue folders are colored in yellow.

Syntax:
    ls [option][path]

Options:
    -l, --listing   Displays more information about files.
    -a, --all       Displays hidden files.
    --help          Displays information about the command.
    """

help_cd_msg = \
    """
Changes current work directory to specified one.

Syntax:
    cd [path/directory]

Options:
    --help  Displays information about the command.
    """

help_clear_msg = \
    """
Clears terminal.

Syntax:
    clear

Options:
    --help  Displays information about the command.
    """

help_cp_msg = \
    """
Copies file (source) to specified destination.

Syntax:
    cp [source][destination]

Options:
    --help  Displays information about the command.
    """

help_touch_msg = \
    """
Creates new text file in UTF-8 encoding.

Syntax:
    touch [file]

Options:
    --help  Displays information about the command.
    """

help_cat_msg = \
    """
Displays specified file content.

Syntax:
    cat [option][file]

Options:
    -f, --framed   Displays file content in framed box.
    --help         Displays information about the command.
    """

help_write_msg = \
    """
Writes content to specified text file. 
To exit writing type ":q".

Syntax:
    write [file]

Options:
    --help  Displays information about the command.
    """

help_alias_msg = \
    """
Creates alias for specified command. 
Command must be written in quotation marks.

Syntax:
    alias [option][alias][command]

Options:
    -r, --remove   Deletes specified alias.
    --help         Displays information about the command.

Example:
    alias l "ls -al"
    alias -r l
    """

help_aliases_msg = \
    """
Displays list of aliases.

Syntax:
    aliases [option]

Options:
    -f, --framed   Displays list of aliases in framed box.
    --help         Displays information about the command.
    """

help_rm_msg = \
    """
Removes specified directory or file.

Syntax:
    rm [option][path]

Options:
    -r, --recursive   Deletes folder if not empty.
    --help            Displays information about the command.
    """

help_mv_msg = \
    """
Moves file (source) to specified destination.

Syntax:
    mv [source][destination]

Options:
    --help  Displays information about the command.
    """

help_pwd_msg = \
    """
Prints current work directory.

Syntax:
    pwd

Options:
    --help  Displays information about the command.
    """

help_help_msg = \
    """
Provides help information for Lindow commands.

Syntax:
    help [command]

Options:
    --help  Displays information about the command.
    """

help_history_msg = \
    """
Prints saved session history. 
Every time shell starts history is cleared.

Syntax:
    history

Options:
    --help  Displays information about the command.
    """

help_ulib_msg = \
    """
Prints list of libraries that were used in project.

Syntax:
    ulib

Options:
    --help  Displays information about the command.
    """

help_mkdir_msg = \
    """
Creates new directory in current working directory or in specified one.

Syntax:
    mkdir [path/directory]

Options:
    --help  Displays information about the command.
    """

help_free_msg = \
    """
Displays info about used and free memory.

Syntax:
    free [option]

Options:
    -h, --human   Human readable.
    -b, --bytes   Displays amount of memory in bytes.
    -k, --kilo    Displays amount of memory in kilobytes (default).
    -m, --mega    Displays amount of memory in megabytes.
    -g, --giga    Displays amount of memory in gigabytes.
    --help        Displays information about the command.
    """