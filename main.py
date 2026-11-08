# main.py
import SecurityTools

def show_password_result(password: str) -> None:
    """check a password abd suggest a strong one if it's weak"""
    ok, problems = SecurityTools.check_password(password)

    if ok:
        print("password: strong enough")
    else:
        print("password: weak -", "; ".join(problems) + ".")
        # offer a random strong on instead
        print("suggested strong password:", SecurityTools.make_password())

def show_ip_result(ip: str) -> None:
    """check an ip address and say if the format is correct"""
    if SecurityTools.check_ip(ip):
        print(f"ip address {ip}: valid format")
    else:
        print(f"ip address {ip}: invalid format")

def main () -> None:
    #ask for a password and an ip address
    password = input("enter a password: ")
    ip = input("enter an ip address: ").strip()

    #run both checks and shows the results
    print()
    show_password_result(password)
    show_ip_result(ip)

#only run main() if this file is run directly
if __name__ == "__main__":
    # carch ctrl+c or an early end of input so the program exits cleanly
    try:
        main()
    except(KeyboardInterrupt, EOFError):
        print("\nprogram interrupted exiting")

