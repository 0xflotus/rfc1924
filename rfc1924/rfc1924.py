from ipaddress import IPv6Address
from typing import Str

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


def encode(ipv6: Str) -> Str:
    lst = [0] * 0o24
    num_ipv6 = int(IPv6Address(ipv6))
    idx = 0
    while num_ipv6 > 0:
        lst[idx] = num_ipv6 % 0x55
        num_ipv6 /= 0x55
        idx += 1
    return "".join(list(map(lambda x: lookup_table[x], list(reversed(lst)))))


def decode(encoded_ipv6: Str) -> Str:
    exp = 0o23
    sum = 0
    for elem in list(
        map(lambda x: lookup_table.index(x), ",".join(encoded_ipv6).split(","))
    ):
        sum += elem * 0x55 ** exp
        exp -= 1
    return IPv6Address(sum)
