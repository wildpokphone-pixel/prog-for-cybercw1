# security incident manager

def show_everything(incident: dict[str, str]) -> None:
    """print the keys and the values and each key value pair of the incident"""
    print("keys:", list(incident.keys()))
    print("values:", list(incident.values()))
    print("key-value pairs:")
    for key, value in incident.items():
        print(f"     {key}: {value}")

def main() -> None:
    # make a dictionary with the username ip adrress event type and risk level
    incident = {
        "username": "Jsmith",
        "ip_address": "203.0.113.45",
        "event_type": "failed login",
        "risk_level": "medium",
    }

    # show the username and ip address by looking them up with their keys 
    print("username:", incident["username"] )
    print("ip address:", incident["ip_address"])

    #add a new field called status 
    incident["status"] = "open"
    print("\nafter adding status:", incident)

    #change the risk level this overwrites the old value
    incident["risk_level"] = "high"
    print("after updating risk level:", incident)

    #remove one field with del 
    try:
        #del incident["event_type"]
        del incident["pokemon"]
        print("after removing event_type:", incident)
    except KeyError:
        # the key isn't there so there is nothing to remove
        print("event_type was not found nothing removed")

    #show everything that is left
    print()
    show_everything(incident)

    # show how many key value pairs there is
    print("\ntotal key value pairs:", len(incident))

# only run main() if this file is run directly
if __name__ == "__main__" :
    #catch ctrl+c so the program exits cleanly
    try:
        main()
    except KeyboardInterrupt:
        print("\nprogram interrupted exiting")   