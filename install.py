import sys
import os
import shutil
import time


def get_python_home_windows() -> str:
    """ get the path of python """

    os.system(f'where python.exe > {os.getcwd}\\tempfile.txt')
    try: 
        os.sync()
    except:
        time.sleep(2)
    with open('tempfile.txt', 'r') as rfile:
        lines = [x.strip('\n') for x in rfile.readlines()]
    home = lines[0].replace('/', '\\')
    os.remove(f'{os.getcwd()}\\tempfile.txt')
    return home

def check_profile() -> str:
    """"""
    os.system(f"echo Test-Path $Profile > {os.getcwd()}\\tempfile.txt")
    with open('tempfile.txt', 'r') as rfile:
        lines = [x.strip('\n') for x in rfile.readlines()]
    home = lines[0]
    os.remove(f'{os.getcwd()}\\tempfile.txt')
    return home

def get_profile_home_windows() -> str:
    os.system(f"echo $Profile > {os.getcwd()}\\tempfile.txt")
    with open('tempfile.txt', 'r') as rfile:
        lines = [x.strip('\n') for x in rfile.readlines()]
    home = lines[0].replace('/', '\\')
    os.remove(f'{os.getcwd()}\\tempfile.txt')
    return home


def write_alias_windows() -> None:

    location = get_profile_home_windows()
    exists = check_profile()
    if exists == 'False':
        os.system(f'New-Item -Type file -Path $Profile -Force')
    lines = [
        'function bfr([string]$ArgOne, [string]$ArgTwo, [string]$ArgThree, [string]$ArgFour, [string]$ArgFive)',
        '{',
        f'    python3.exe C:\\Users\\{Windows.user}\\bfr\\main.py "$ArgOne" "$ArgTwo" "$ArgThree" "$ArgFour" "$ArgFive"',
        '}',
    ]
    with open(location, 'a') as afile:
        afile.write('\n')
        for line in lines:
            afile.write(f'{line}\n')
    

    
class Darwin:
    user = __file__.split("/")[2]
    home = f'/Users/{user}'
    alias_file = f'Users/{user}/.zprofile'
    alias_string = f'alias bfr="python3 /Users/{user}/bfr/main.py'
    folder = f'/Users/{user}/bfr'
    

class Linux:
    user = os.getlogin()
    home = f'home/{user}'
    alias_file = f'/home/{user}/.bashrc'
    alias_string = f'alias bfr="python3 /home/{user}/bfr/main.py'
    folder = f'/home/{user}/bfr'

class Windows:
    user = os.getlogin()
    home = f'C:\\Users\\{user}\\'
    folder = f'C:\\Users\\{user}\\bfr\\'
    file = f'C:\\Users\\{user}\\bfr\\main.py'
    cmdcommand = f'doskey bfr=py C:\\Users\\{user}\\bfr\\main.py'
    pscommand = f'New-Alias '
    python_home = get_python_home_windows()
    alias_file = get_profile_home_windows()



def cwd_mac() -> str:
    current_file = __file__
    current_dir = "/".join(current_file.split("/")[:-1])
    cwd = current_dir.replace('root', Darwin.user)
    print(cwd)

def make_folder_windows() -> None:
    os.mkdir(Windows.folder)
    try:
        os.sync()
    except:
        time.sleep(1)

def make_folder_mac() -> None:
    os.mkdir(Darwin.folder)
    os.sync()

def make_folder_linux() -> None:
    os.mkdir(Linux.folder)
    os.sync()

def copy_file_windows() -> None:
    shutil.copy(src=f'{os.getcwd()}\\index_files.py', dst=f'{Windows.folder}\\main.py')
    try:
        os.sync()
    except:
        with open(f'{os.cwd()}\\index_files.py', 'r') as rfile:
            lines = rfile.readlines()
        with open(Windows.file, 'w') as wfile:
            for line in lines:
                wfile.write(line)
    try:
        os.sync()
    except:
        pass

def copy_file_mac() -> None:
    shutil.copy(src=f'{cwd_mac()}/index_files.py', dst=f'{Darwin.folder}/main.py')
    os.sync()
    
def copy_file_linux() -> None:
    shutil.copy(src=f'{os.getcwd()}/index_files.py', dst=f'{Linux.folder}/main.py')
    os.sync()



def write_alias_mac() -> None:
    with open(Darwin.alias_file, 'a') as afile:
        afile.write(f'\n# Bulk file renamer\n{Darwin.alias_string}\n')
    os.sync()

def write_alias_linux() -> None:
    with open(Linux.alias_file, 'a') as afile:
        afile.write(f'\n# bulk file renamer\n{Linux.alias_string}\n')
    os.sync()

def update_mac() -> None:
    print(f"\n Please run \033[32m source /User/{Darwin.user}/.zprofile  \033[0m to enable bfr command")

def update_linux() -> None:
    print(f"\n Please run \033[32m source /home/{Darwin.user}/.bashrc  \033[0m to enable bfr command")

def install_mac() -> None:
    """ install bfr for MacOs """

    lines = ['Making Directories...', 'Coping Files...', 'Writing Alias...', 'Done.' ]
    functions = [make_folder_mac, copy_file_mac, write_alias_mac, update_mac]
    elines = enumerate(lines)
    for index, x in elines:
        print(x)
        functions[index]()
    
def install_linux() -> None:
    """ install bfr for linux """

    lines = ['Making Directories...', 'Coping Files...', 'Writing Alias...', 'Done.' ]
    functions = [make_folder_linux, copy_file_linux, write_alias_linux, update_linux]
    elines = enumerate(lines)
    for index, x in elines:
        print(x)
        functions[index]()
    
def install_windows() -> None:
    """ install bfr for windows """

    lines = ['Making Directories...', 'Coping Files...', 'Writing Alias...']
    functions = [make_folder_windows, copy_file_windows, write_alias_windows]
    elines = enumerate(lines)
    for index, x in elines:
        print(x)
        functions[index]()

def cleanup_windows() -> None:
    cwd = "\\".join(__file__.split("\\")[:-1])
    shutil.rmtree(cwd)

def cleanup_mac() -> None:
    cwd = "/".join(__file__.split("/")[:-1])
    shutil.rmtree(cwd)

def cleanup_linux() -> None:
    cwd = "/".join(__file__.split("/")[:-1])
    shutil.rmtree(cwd)

def main() -> None:
    print(f' installing bfr for {sys.platform}... ')
    if sys.platform.lower() == 'linux':
        install_linux()
        cleanup_linux()
    elif sys.platform.lower() == 'windows':
        install_windows()
        cleanup_windows()
    elif sys.platform.lower() == 'darwin':
        install_mac()
        cleanup_mac()
    


if __name__ == '__main__':
    main()
