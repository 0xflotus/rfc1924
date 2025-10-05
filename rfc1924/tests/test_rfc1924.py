from rfc1924 import encode, decode, savings


def test_encode():
    assert encode("2345:425:2ca1::567:5673:23b5") == "AN?6(i3Y+yVr74uX@J3P"


def test_decode():
    assert decode("AN?6(i3Y+yVr74uX@J3P") == "2345:425:2ca1::567:5673:23b5"


def test_savings():
    assert savings("2345:425:2ca1::567:5673:23b5") == "You saved 28%"
