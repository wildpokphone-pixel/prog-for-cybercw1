#Security event logger

import random
import socket
from datetime import datetime

def get_my_ip() -> str:
    """Return this computer ips address or 127.0.0.1 if there is no network that can be found"""
    try:
        #connecting with a udp socket does not send anything it just shows what address we use 
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.connect(("8.8.8.8", 80))
            return sock.getsockname()[0]
    except OSError:
        # no network so use the local address instead
        return "127.0.0.1"

def log_attempt(name: str, ip: str, worked: bool) -> None:
    """print a log entry for one login attempt"""
    log_id = random.randint(1000, 9999)
    result = "successful login" if worked else "failed login"
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"event ID: {log_id}")
    print(f"username: {name}")
    print(f"ip address: {ip}")
    print(f"event: {result}")
    print(f"timestamp: {time_now}")
    print()

def main() -> None:
    #test login details
    real_name = "admin"
    real_password = "secure#2026"


    #only look up the ip once it won't change while running
    my_ip = get_my_ip()

    print("SECURITY EVENT LOG")
    print("==================")

    # keep asking until the details are correct
    while True:
        name = input("username: ")
        password = input("password: ")

        worked = name == real_name and password == real_password

        # log every attempt regardless if it failed or not
        log_attempt(name, my_ip, worked)

        if worked:
            break
    # only run main() if this file is run directly
if __name__ == "__main__":
    #catch ctrl+c on an early end of input so the program exits cleanly
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram interrupted Exiting")