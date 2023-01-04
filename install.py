import sys

if __name__ == '__main__':
    if sys.platform.lower() == 'linux':
        from install.linux_install import main
        main()
    elif sys.platform.lower() == 'darwin':
        from install.mac_install import main
        main()
    elif sys.platform.lower() == 'windows':
        from install.windows_install import main()
        main()