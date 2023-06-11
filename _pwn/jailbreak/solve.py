#!/usr/bin/env python
from libctf import Remote
import inspect

# Set up challenge and response regex
flag_regex = r""
query_regex = r""
jailed_substrings = ["print"]

# Write the script you want to run inside the jail
def solve():
    foo="cat flag.txt"
    bar="cat flag2.txt"

# Generates the payload that will be sent; turns solve into strings with \n breaks
def unjail():
    lines = inspect.getsourcelines(solve)[0]
    lines.pop(0) # remove first line, always def solve():
    return "\n".join([line.strip() for line in lines])

##################################################64#char#string#
p = Remote("challs.n00bzunit3d.xyz", 13541)
p.debug=True
p.flag_regex = flag_regex
p.query_regex = query_regex

if True in [substr in unjail() for substr in jailed_substrings]:
    raise Exception("Jailed substring found in solve()")

match = p.challenge()
if match:
    p.response(unjail().encode("utf-8"))