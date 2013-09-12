import shutil
import sys
import os
import re
from optparse import OptionParser


# ---------- Helper Functions ---------
def append_file_name(old_file_name, insertion_text, before_extension):
	if before_extension:
		(file_prefix, file_extension) = split_file_extension(old_file_name) 
		return file_prefix + insertion_text + file_extension
	else:
		return old_file_name + insertion_text

file_ext_split_pattern = re.compile("(?P<prefix>.*)(?P<extension>\..+)$")
def split_file_extension(file_path):
	match = file_ext_split_pattern.match(file_path)
	if match:
		return (match.group('prefix'), match.group('extension'))
	else:
		return (file_name, '')

# ---------- Main Execution ---------

usage_str = '''Usage:

python3 file-renamer.py <command> <input directory> <output directory> <file name pattern> <text> <options>

command:
	append: Places the `<text>` argument at the end of the file name

options:
	-e, --ext: Performs the command on the part of the filename prior to the file extension

Example:

	python3 file-renamer.py append somdir newdir ".*\.xml$" "_newname" -e

	Files Before:
		somedir/data1.xml
		somedir/data2.xml
		somedir/image.jpg

	Files After:
		newdir/data1_newname.xml
		newdir/data2_newname.xml
		somedir/image.jpg
'''

# Parse the command line arguments
arg_parser = OptionParser()
arg_parser.add_option('-e', '--ext', dest='before_extension', action='store_true')
(options, arguments) = arg_parser.parse_args()

# Verify that all the required arguments are there
if(len(arguments) != 5):
	print()
	print('Incorrect number of arguments.')
	print(usage_str)
	sys.exit(1)

arg_command = arguments[0]
arg_input_dir = arguments[1]
arg_output_dir = arguments[2]
arg_pattern = arguments[3]
arg_text = arguments[4]

# Verify that the command exists
valid_commands = ('append')
if arg_command not in valid_commands:
	print('Incorrect command.')
	print(usage_str)
	sys.exit(1)

if arg_command == 'append':
	get_new_name = append_file_name

# Verify that the input directory exists
if not os.path.isdir(arg_input_dir):
	print('Input directory does not exist.')
	print(usage_str)
	sys.exit(1)

# Create the output directory if it doesn't exist
if not os.path.exists(arg_output_dir):
	os.makedirs(arg_output_dir)

# Compile the regular expression used to match files
file_name_pattern = re.compile(arg_pattern)

# Iterate through the matching files in the input directory and move/rename
for file_name in os.listdir(arg_input_dir):
	# Check to see if the file name matches the pattern
	if not file_name_pattern.match(file_name):
		continue

	# Change the file name
	new_file_name = get_new_name(file_name, arg_text, options.before_extension)

	# Construct the old and new paths
	old_file_path = arg_input_dir + '/' + file_name
	new_file_path = arg_output_dir + '/' + new_file_name

	# Perform the rename/move
	shutil.move(old_file_path, new_file_path)