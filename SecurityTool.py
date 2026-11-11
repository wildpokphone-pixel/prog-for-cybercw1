# Security Tool


def get_percentage(part: int, total: int) ->float:
    """Return part as a percentage of the total that or 0.0 if total is zero""" 
    if total == 0:
        return 0.0
    return (part / total) * 100

def details_match(name: str, password: str, real_name: str, real_password: str) -> bool:
    """Retrun true if both of the names and passwords match with the correct and real ones"""
    return name == real_name and password == real_password


def show_menu() -> None:
    """show the menu to pick from the options"""
    print("\nSECURITY MENU")
    print("1. security event counter")
    print("2. brute force simulator")
    print("3. login")
    print("4. exit")


def login(real_name: str, real_password: str, max_tries: int) -> bool:
    """ask for login details and crednetials until the correct or max about of tries is reached returning true if the login is succesful"""
    failed = 0

    # keep asking until the login work or the attempts run out
    while failed < max_tries: 
        name = input("enter username: ")
        password = input("enter password: ")

        if details_match(name, password, real_name, real_password):
            print("login worked!")
            return True

        failed += 1
        print(f"Login stinks. failed tries: {failed} of {max_tries}")

    print("Account is locked for the next 24 hours, better luck next time")
    return False

def count_events(real_password: str, total_tries: int, alert_limit: float) -> None:
    """Ask for a password equal to the amount of of total_tries times and count the results and show an alert if needed"""
    right = 0
    wrong = 0

    print("\nSECURITY EVENT COUNTER")


#record each password entry attempt as a right or wrong event
    for try_number in range(1, total_tries + 1):
        typed = input(f"Try {try_number} of {total_tries} - enter password ")

        if typed == real_password: 
            right += 1
        else:
            wrong += 1
    wrong_percent = get_percentage(wrong, total_tries)


    print(f"correct passwords: {right}")
    print(f"incorrect passwords: {wrong}")
    print(f"percentace incorrect: {wrong_percent:.1f}%")

    # show an alert if the wrong entries go above the limit
    if wrong_percent > alert_limit:
        print(F"ALERT: more than {alert_limit:.0f} percent of the passwords were incorrect")

def brute_force(secret_password: str, max_tries: int) -> None:
    """Let the users guess the passwor until it's either right or the number of attempts run out"""
    tries = 0
    found = False

    print("\nBRUTE FORCE SUMULATION")

    #keep going until the password is found or there is no attempts left
    while tries < max_tries and not found:
        guess = input(f"try {tries + 1} of {max_tries} - guess the password: ")
        tries += 1

        if guess == secret_password:
            found = True
        elif tries >= max_tries:
            print(f"Max tries ({max_tries})reached password not guessed")


def main():
    # the real login details and limits that are bieng used by the tool
    real_name = "Admin"
    real_password = "Secure123"
    login_tries = 3
    event_tries = 10
    alert_limit = 50.0
    guess_tries = 5

    # the user must login before the menu can be shown 

    print("login needed")
    if not login(real_name, real_password, login_tries):
        return

    #keep showing the menu until the user chooses to leave it
    running = True
    while running:
        show_menu()
        choice = input("select an option (1-4): ").strip()

        if choice == "1":
            count_events(real_password, event_tries, alert_limit)
        elif choice =="2":
            brute_force(real_password, guess_tries)
        elif choice == "3":
            print("\nLOGIN")
            #end the program if the account become frozen 
            if not login(real_name, real_password, login_tries):
                running = False
        elif choice == "4":
            print("thanks for using the security tools")
            running = False
        else:
            print("invalid choice please enter a number from 1 to 4")


#only run main() when this file is run directly, not imported
if __name__ == "__main__":
    # try except stops a crash if the user presses cntrl+c or ends the input early
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nprogram interrupted exiting program")

                    
