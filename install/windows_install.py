import os
import sys
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

class Windows:
    user = os.getlogin()
    home = f'C:\\Users\\{user}\\'
    folder = f'C:\\Users\\{user}\\bfr\\'
    file = f'C:\\Users\\{user}\\bfr\\main.py'
    cmdcommand = f'doskey bfr=py C:\\Users\\{user}\\bfr\\main.py'
    pscommand = f'New-Alias '
    python_home = get_python_home_windows()
    alias_file = get_profile_home_windows()

def make_folder_windows() -> None:
    os.mkdir(Windows.folder)
    try:
        os.sync()
    except:
        time.sleep(1)

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

def main() -> None:
    install_windows()
    cleanup_windows()


if __name__ == '__main__':
    main()
