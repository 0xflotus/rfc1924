import ipaddress

print(int(ipaddress.ip_address("fe80::fbd6:7860")))

tbl = [
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

lst = [0] * 20
i = int(ipaddress.ip_address("1080:0:0:0:8:800:200C:417A"))
l = 0
print(i)
while i > 0:
    lst[l] = i % 85
    i = i // 85
    l = l + 1

print("".join(list(map(lambda x: tbl[x], list(reversed(lst))))))

print(list(map(lambda x: tbl.index(x), ",".join("4)+k&C#VzJ4br>0wv%Yp").split(","))))
q = 19
sum = 0
for i in list(map(lambda x: tbl.index(x), ",".join("4)+k&C#VzJ4br>0wv%Yp").split(","))):
    sum = sum + i * 85 ** q
    q = q - 1

print(sum)
print(ipaddress.IPv6Address(sum))
