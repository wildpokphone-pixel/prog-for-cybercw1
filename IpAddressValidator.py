# ip address validator 

def check_ip(ip: str) -> bool:
    """return true if the ip is four numbers from 0 to 255 splits up by the dots"""
    # get rid of any spaces at the start or end
    ip = ip.strip()

    # a proper address has four parts so three dots
    pieces = ip.split(".")
    if len(pieces) != 4:
        return False

    for piece in pieces:
        #every pirece has to be plain digits this alos catches empty pieces letters and negative numbers
        if not(piece.isascii() and piece.isdigit()):
            return False

        # no piece can be bigger than 255
        if int(piece) > 255:
            return False

    return True     

def main() -> None:
    ip = input("enter an ip address: ")

    if check_ip(ip):
        print("valid ip address")
    else:
        print("invalid ip address")

#only run main() if this file is run directly
if __name__ == "__main__":
    # catch ctrl+c or an early end of input so the program exits cleanly
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram interrupted exiting")