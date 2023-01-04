import os
import shutil
import sys
import time



class Linux:
    user = os.getlogin()
    home = f'home/{user}'
    alias_file = f'/home/{user}/.bashrc'
    alias_string = f'alias bfr="python3 /home/{user}/bfr/main.py'
    folder = f'/home/{user}/bfr'

def make_folder_linux() -> None:
    os.mkdir(Linux.folder)
    os.sync()

def copy_file_linux() -> None:
    shutil.copy(src=f'{os.getcwd()}/index_files.py', dst=f'{Linux.folder}/main.py')
    os.sync()

def write_alias_linux() -> None:
    with open(Linux.alias_file, 'a') as afile:
        afile.write(f'\n# bulk file renamer\n{Linux.alias_string}\n')
    os.sync()

def update_linux() -> None:
    print(f"\n Please run \033[32m source /home/{Linux.user}/.bashrc  \033[0m to enable bfr command")

def install_linux() -> None:
    """ install bfr for linux """

    lines = ['Making Directories...', 'Coping Files...', 'Writing Alias...', 'Done.' ]
    functions = [make_folder_linux, copy_file_linux, write_alias_linux, update_linux]
    elines = enumerate(lines)
    for index, x in elines:
        print(x)
        functions[index]()
    
def cleanup_linux() -> None:
    cwd = "/".join(__file__.split("/")[:-1])
    shutil.rmtree(cwd)

def main() -> None:
    install_linux()
    cleanup_linux()

if __name__ == '__main__':
    main()
