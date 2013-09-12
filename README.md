file-renamer
============

A command line utility for renaming files within a directory in different ways.

Usage
=====
`python3 file-renamer.py <command> <input directory> <output directory> <file name pattern> <text> <options>`

command:
	`append`: Places the `<text>` argument at the end of the file name

options:
	`-e`, `--ext`: Performs the command on the part of the filename prior to the file extension

Example:

	`python3 file-renamer.py append somdir newdir ".*\.xml$" "_newname" -e`

	Files Before:
		`somedir/data1.xml
		somedir/data2.xml
		somedir/image.jpg`

	Files After:
		`newdir/data1_newname.xml
		newdir/data2_newname.xml
		somedir/image.jpg`