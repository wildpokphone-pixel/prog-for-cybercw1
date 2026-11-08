# security toold

import secrets
import string

def check_password(password: str) -> tuple[bool, list[str]]:
    """check a password is 8 plus chracters with a letter digit and a symbol
    returns ok problems where problems list whatever is missing
    """

    problems = []

    # too short?
    if len (password) < 8:
        problems.append("must be at least 8 characters long")

    # look for at least one letter digit and symbol
    if not any(char.isalpha() for char in password):
        problems.append("must contain at least one letter")
    if not any(char.isdigit() for char in password):
        problems.append("must contain at least one digit")
    if not any(char in string.punctuation for char in password):
        problems.append("must contain at least one symbol")

    return len(problems) == 0, problems

def check_ip(ip: str) -> bool:
    """retrun true if ip is four number from 0 to 255 split up ny dots"""
    # a proper address has four pieces so three dots
    pieces = ip.split(".")
    if len(pieces) != 4:
        return False

    for piece in pieces:
        #plain digits only this also catches empty pieces letter and minus signs
        if not (piece.isascii() and piece.isdigit()):
            return False

        # no piece can be bigger than 255
        if int(piece) > 255:
            return False

    return True

def make_password() -> str:
    """return a random password 10 to 16 chracters with all four chracters types."""
    #pick a random length from 10 to 16
    how_long = secrets.randbelow(7) +10

    # start with one of each type so none are missing 
    picked = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation),
    ]

    # fill up the rest from every type of character
    all_chars = string.ascii_letters + string.digits + string.punctuation
    picked += [secrets.choice(all_chars) for _ in range(how_long - len(picked))]

    #shuffle so the first four arent always in the same order
    secrets.SystemRandom().shuffle(picked)

    return "".join(picked)