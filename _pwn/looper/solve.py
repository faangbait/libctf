#!/usr/bin/env python
from libctf import Remote, Local
import re

# Set up challenge and response regex
flag_regex = r"n00bz{.*}"
query_regex = r"How many (\d)'s appear till (\d+)\?"

# This should turn a returned query into a desired response
def solve(match: re.match):
    count = 0
    num = match.groups()[0]
    targ = match.groups()[1]
    for i in range(1,int(targ)):
        if num in str(i):
            count+=str(i).count(num)
    return count

# Place known successful test cases here. 
# If solver is coded correctly, all tests should pass.
# Add breakpoints in libctf to debug failing tests.
tests = [
    {"challenge": b"How many 3's appear till 40?", "response": b"14"},
    # {"challenge": b"How many 3's appear till 40?", "response": b"15"}, # demo; should fail
    # {"challenge": b"How many 3's appear till 40?", "response": b"16"}, # demo; should fail
]

##################################################64#char#string#
p = Remote("challs.n00bzunit3d.xyz", 13541)
p.debug=False
p.flag_regex = flag_regex
p.query_regex = query_regex
p.test_challenges = tests
p.test(solve)
p.start(solve)