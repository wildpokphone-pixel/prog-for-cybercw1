# Programming for Cyber security: CW 1 

**Name** Josh williams

**Campus:** NCL motherwell

**Banner ID:** B01888344

## Overview
This repository is my course work 1 portfolio. Work will be uploaded with it's own git branch with the code itself, readme, license and test screenshots.

## Exercises and Branches

| Task | Branch | Description |
|------|--------|-------------|
| 1 | security-tool | A menu focused python program that requires a login with 3 login attempts before account is frozen. then offers a security event counter that records correct and failed password entries then it goes on to calculate a percentage and if inccorect and has a value above 15 percent it raises an alert along with a brute force simulator with a mlimited number of guesses and a repetable login authentication checker |
| 2 | `security-event-logger` |  A Python program that logs every login attempt regardless if it fails or passes each login entry records a random event ID with the username entered along with the ip address of they system the event type and the timestamps as it keeps asking for details till the login works 
| 3 | `ip-address-validator` | A Python program that asks for an IP address and checks that it is a correctly formatted IPv4 address: four parts separated by dots, digits only each between 0 and 255. It reports whether the address is valid or invalid. |
| 4 | security-incident-manager | A Python program that stores one security incident in a dictionary username, IP address, event type and risk level It displays the username and IP address adds a status field updates the risk level removes a field then displays the remaining keys and values and the total number of key value pairs |
| 5 | cyber-security-utilities | A Python program split into two files The module security_tools.py holds reusable functions that validate a password length letter digit symbol check the format of an IPv4 address and generate a strong random password of 10 to 16 characters main.py imports the module asks the user for a password and an IP address, reports whether each is valid and suggests a generated password if the entered one is weak |

## How to see a branch 

```bash
git clone https://github.com/YOURUSERNAME/prog-for-cybercw1.git
cd prog-for-cybercw1
git switch security-tool
```

Replace `security-tool` with any branch name from the table

## License
This project is licensed under the MIT license. see the `LICENSE` file


