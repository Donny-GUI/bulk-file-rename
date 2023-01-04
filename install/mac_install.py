import os
import sys
import time
import shutil 

 
class Darwin:
    user = __file__.split("/")[2]
    home = f'/Users/{user}'
    alias_file = f'Users/{user}/.zprofile'
    alias_string = f'alias bfr="python3 /Users/{user}/bfr/main.py'
    folder = f'/Users/{user}/bfr'
    

def cwd_mac() -> str:
    current_file = __file__
    current_dir = "/".join(current_file.split("/")[:-1])
    cwd = current_dir.replace('root', Darwin.user)
    print(cwd)

def make_folder_mac() -> None:
    os.mkdir(Darwin.folder)
    os.sync()

def copy_file_mac() -> None:
    shutil.copy(src=f'{cwd_mac()}/index_files.py', dst=f'{Darwin.folder}/main.py')
    os.sync()
  
def write_alias_mac() -> None:
    with open(Darwin.alias_file, 'a') as afile:
        afile.write(f'\n# Bulk file renamer\n{Darwin.alias_string}\n')
    os.sync()

def update_mac() -> None:
    print(f"\n Please run \033[32m source /User/{Darwin.user}/.zprofile  \033[0m to enable bfr command")

def install_mac() -> None:
    """ install bfr for MacOs """

    lines = ['Making Directories...', 'Coping Files...', 'Writing Alias...', 'Done.' ]
    functions = [make_folder_mac, copy_file_mac, write_alias_mac, update_mac]
    elines = enumerate(lines)
    for index, x in elines:
        print(x)
        functions[index]()

def cleanup_mac() -> None:
    cwd = "/".join(__file__.split("/")[:-1])
    shutil.rmtree(cwd)

def main() -> None:
    install_mac()
    cleanup_mac()
 
if __name__ == '__main__':
    main()
