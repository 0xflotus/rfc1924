from ipaddress import IPv6Address

# fmt: off
lookup_table = (
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
    "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
    "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d",
    "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
    "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
    "y", "z", "!", "#", "$", "%", "&", "(", ")", "*",
    "+", "-", ";", "<", "=", ">", "?", "@", "^", "_",
    "`", "{", "|", "}", "~"
)
# fmt: on

lookup_table_char_to_idx: dict[str, int] = {
    char: idx for (idx, char) in enumerate(lookup_table)
}


def encode(ipv6: str | int) -> str:
    return "".join(
        lookup_table[int(IPv6Address(ipv6)) // 0x55**cnt % 0x55]
        for cnt in range(0o24 - 1, -1, -1)
    )


def decode(encoded_ipv6: str) -> str:
    return str(
        IPv6Address(
            sum(
                lookup_table_char_to_idx[ch] * 0x55**exp
                for ch, exp in zip(encoded_ipv6, range(0o23, -1, -1))
            )
        )
    )


def savings(ipv6: str) -> str:
    return f"You saved {int((1 - len(encode(ipv6)) / len(ipv6)) * 100)}%"
