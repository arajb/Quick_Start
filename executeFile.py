import os

filename = 'c:\Python27\hello.py'
if filename and os.path.isfile(filename):
    with open(filename) as fobj:
        startup_file = fobj.read()
	exec(startup_file)
	print "Execution complete"
else:
	print "File Not Found"

# Note: Code can be modified from line#5 to #7 with exec(open('c:\Python27\hello.py').read())
