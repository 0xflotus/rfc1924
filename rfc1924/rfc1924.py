from ipaddress import IPv6Address
from functools import reduce

lookup_table = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "!",
    "#",
    "$",
    "%",
    "&",
    "(",
    ")",
    "*",
    "+",
    "-",
    ";",
    "<",
    "=",
    ">",
    "?",
    "@",
    "^",
    "_",
    "`",
    "{",
    "|",
    "}",
    "~",
]


def encode(ipv6):
    lst = [0] * 0o24
    num_ipv6 = int(IPv6Address(ipv6))
    idx = 0
    while num_ipv6 > 0:
        lst[idx] = num_ipv6 % 0x55
        num_ipv6 //= 0x55
        idx += 1
    return "".join(list(map(lambda x: lookup_table[x], list(reversed(lst)))))


def decode(encoded_ipv6):
    return str(
        IPv6Address(
            reduce(
                lambda sum, vec: sum + vec[0] * 0x55 ** (0o23 - vec[1]),
                map(
                    lambda vec: (lookup_table.index(vec[0]), vec[1]),
                    zip(encoded_ipv6, range(0o24)),
                ),
                0,
            )
        )
    )


def savings(ipv6):
    return f"You saved {int((1 - len(encode(ipv6)) / len(ipv6)) * 100)}%"
