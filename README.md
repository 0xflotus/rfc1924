# RFC 1924

This python library is an implementation of [RFC 1924](https://www.rfc-editor.org/rfc/rfc1924). 

## A Compact Representation of IPv6 Addresses

With this library you can store IPv6 addresses in a more compact form. It's Base85 encoded.

## Usage

```py
from rfc1924 import *

print(encode("2345:0425:2CA1::0567:5673:23b5")) # -> AN?6(i3Y+yVr74uX@J3P
print(decode("AN?6(i3Y+yVr74uX@J3P")) # -> 2345:0425:2CA1::0567:5673:23b5
```

Save up to 48% space with this compact form:

`ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff` -> `=r54lj&NUUO~Hi%c2ym0`
