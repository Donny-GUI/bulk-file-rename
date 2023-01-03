![bfr](https://user-images.githubusercontent.com/108424001/210458734-0931b43c-8888-4e5d-85f2-2c1f7195de97.png)

# bulk-file-rename

Command line tool that renames files with the given extension argument  as their indexes. Includes the ability to prefix and suffix file type.

# getting started

```Bash

git clone https://github.com/Donny-GUI/bulk-file-rename.git
cd bulk-file-rename
python3 installer.py

```

# Usage

```Bash
bfr
bfr -e png -p hello
bfr -e jpeg -p hi -s mom
```

# Flags

```Bash
-e  --extension # extension for the filetype, this flag is mandatory
-s  --suffix    # suffix flag, provide a suffix to add to the filename
-i  --index     # index, just index the filetype, no name
-p  --prefix    # prefix, add a prefix to the filename
-h  --help      # help, shows the menu
```
