"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
def sys_cli():
    for i in sys.argv:
        print(i)

print(sys_cli())

# Print out the OS platform you're using:

print(sys.platform)

# Print out the version of Python you're using:
# YOUR CODE HERE

version_dict = {"Simple": sys.version, "Verbose": sys.version_info}
print(version_dict)

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID

current_pid = os.getpid()

print(current_pid)

# Print the current working directory (cwd):

cwd = os.getcwd

print(cwd)
# Print out your machine's login name
login_name = os.getlogin()

print(login_name)

