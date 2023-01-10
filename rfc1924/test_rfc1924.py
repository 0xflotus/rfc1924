from rfc1924 import *

assert encode("2345:425:2ca1::567:5673:23b5") == "AN?6(i3Y+yVr74uX@J3P"
assert decode("AN?6(i3Y+yVr74uX@J3P") == "2345:425:2ca1::567:5673:23b5"

print(savings("2345:425:2ca1::567:5673:23b5"))
