import os
from sys import argv

#
#   [name]:        index_files.py
#   [description]: will rename files of the current working directory  
#	[author]:      Donald Guiles  1/3/2022
#

def show_help():
	""" show the help menu """

	print('\033[1;32mBulk File Rename v1.1\033[0m')
	print("  [\033[1musage\033[0m]")
	print("    indexf ")
	print("    indexf -p <name to add to prefix>")
	print("    indexf -p <prefix> -e <extension to rename>")
	print("  [\033[1mdescription\033[0m]")
	print("    Rename all the files in the current directory")
	print("  [\033[1moptions\033[0m]")
	print("    -e, --extension   ->   extension to change, mandatory argument")
	print("    -s  --suffix      ->   suffix to add to filename")
	print("    -p  --prefix      ->   prefix to add to filename")
	print("    -i  --index       ->   just name the files as indices")



def get_files_by_extension(extension: str, verbose: bool) -> list[str]:
	""" gets all the files in the current directory 
		with <extension> as a list of strings """

	message('fetch', f' getting files by extension {extension}', verbose)
	ext = has_dot(extension, False)
	os.system('ls > tempfile.txt')
	with open('tempfile.txt', 'r') as rfile:
		lines = [x.strip('\n') for x in rfile.readlines()]
		lines.remove('tempfile.txt')
		print(lines)
	os.remove('tempfile.txt')
	os.sync()
	return lines

def list_dir(extension: str, verbose):
	files = get_files_by_extension(extension, False)
	for file in files:
		print(file)

def has_dot(ext: str, verbose: bool):
	""" adds a dot to the extension if there is not one """

	message('checking', f' {ext}', verbose)
	extension = ext
	if not extension.startswith('.'):
		extension = '.' + extension
	return extension

def get_extension():
	""" gets the extension argument """

	for index, arg in enumerate(argv):
		if arg in ['-e', '-extension']:
			try:
				nextidx = index+1
				return has_dot(argv[nextidx], False)
			except:
				show_help()
				exit()
	return None

def get_prefix():
	""" gets the prefix argument """

	for index, arg in enumerate(argv):
		if arg in ['-p', '--prefix']:
			try:
				nextidx = index+1
				return argv[nextidx]
			except:
				show_help()
				exit()
	return None

def get_suffix():
	""" gets the suffix argument """

	for index, arg in enumerate(argv):
		if arg == '-s' or arg == '--suffix':
			try:
				nextidx = index+1
				return argv[nextidx]
			except IndexError:
				show_help()
				exit()
	return None

def rename_with_extension_prefix_suffix(extension: str, prefix: str, suffix: str, verbose: bool):
	""" rename all files in the current directory
		with extension <extension> adding <prefix>index<suffix> 
	"""

	ext = has_dot(extension, verbose)
	files = get_files_by_extension(ext, verbose)
	for index, name in enumerate(files):
		message('rename', f'{name} to {prefix}{index}{suffix}{ext}', verbose)
		os.rename(name, f"{prefix}{index}{suffix}{ext}")


def rename_with_extension_prefix(extension: str, prefix: str, verbose: bool):
	""" rename all files in the current directory 
		with extension <extension> adding <prefix>index<extension> 
	"""

	ext = has_dot(extension, verbose)
	files = get_files_by_extension(ext, verbose)
	for index, name in enumerate(files):
		message('rename', f'{name} to {prefix}{index}{ext}', verbose)
		os.rename(src=f'{os.getcwd()}/{name}', dst=f"{os.getcwd()}/{prefix}{index}{ext}")

def rename_with_extension_suffix(extension: str, suffix: str, verbose: bool):
	
	ext = has_dot(extension, verbose)
	files = get_files_by_extension(ext, verbose)
	for index, name in enumerate(files):
		message('rename', f'{name} to {index}{suffix}{ext}', verbose)
		os.rename(name, f"{index}{suffix}{ext}")

def index_with_extension(extension: str, verbose: bool):
	""" rename the files with the extension their index """

	ext = has_dot(extension, verbose)
	files = get_files_by_extension(ext, verbose)
	for index, name in enumerate(files):
		message('rename', f'{name} to {index}{ext}', verbose)
		os.rename(src=f'{os.getcwd()}/{name}', dst=f"{os.getcwd()}/{index}{ext}")

def bulk_rename(extension: str, prefix: str, suffix: str, verbose: bool):

	message('init', f'bulk rename for all files with extension {extension} in current working directory', verbose)

	if extension != None and prefix!=None and suffix!=None:
		message('option', f'rename files with extension {extension} using prefix {prefix} and suffix {suffix}', verbose)
		rename_with_extension_prefix_suffix(extension, prefix, suffix, verbose)
		os.sync()
		os.system('ls')
		exit()
	if extension != None and prefix!=None:
		message('option', f'rename files with extension {extension} and prefix {prefix}', verbose)
		rename_with_extension_prefix(extension, prefix, verbose)
		os.sync()
		os.system('ls')
		exit()
	if extension != None and suffix!=None:
		message('option', f'rename files with extension {extension} and suffix {suffix}', verbose)
		rename_with_extension_suffix(extension, suffix, verbose)
		os.sync()
		os.system('ls')
		exit()
	if extension != None:
		message('option', f'rename files as index with extension {extension}', verbose)
		index_with_extension(extension, verbose)
		os.sync()
		os.system('ls')
		exit()

def just_index(extension: str, verbose: bool):
	""" just renames files with <extension> as their index + extension """

	ext = has_dot(extension, verbose)
	files = get_files_by_extension(ext, verbose)
	for index, file in enumerate(files):
		message('rename', f'{file} to {index}{ext}', verbose)
		os.rename(src=file, dst=f"{index}{ext}")

def get_just_index():
	""" ensures that -i or --index is not called """

	args = argv
	for index, item in enumerate(args):
		if item in ['-i', '--index']:
			return True
	return False


def precheck_args():
	""" makes sure the correct amount of args exist """

	lenargv = int(len(argv))
	for arg in argv:
		if arg == '-h' or arg == '--help':
			show_help()
			exit()
	if lenargv == 1:
		show_help()
		exit()
	if lenargv == 2:
		show_help()
		exit()

def get_verbose():
	""" ensures verbose was or wasnt called """

	if '-v' or '--verbose' in argv:
		return True
	if 'v' in argv[1]:
		return True
	return False

def message(title: str, msg: str, verbose: bool):
	""" prints a message if verbose is called """

	if verbose == True:
		print(f"[\033[32m{title}\033[0m]: \033[3m{msg}\033[0m")

def main():
	
	verbose = get_verbose()
	ext = get_extension()
	if ext == None:
		show_help()
		exit()
	prefix = get_prefix()
	suffix = get_suffix()
	jindex = get_just_index()
	if jindex == False:
		bulk_rename(ext, prefix, suffix, verbose)
		exit()
	if ext==None:
		show_help()
		exit()
	else:
		just_index(ext, verbose)
		exit()

if __name__ == '__main__':
	precheck_args()
	main()