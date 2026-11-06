# Task 2: security event logger

**Name:** Josh williams 

**Campus:** NCL motherwell

**Banner ID:** B0188344


## what the program does
It's a menu driven security tool written within python the user must log in first and 3 failed attempts results in a locked account once you're logged in the menu offers:

1. **Security event counter** the user can enter a password up to 10 times the program counts correct and failed entries and shows the percentage of the incorrect attempts and raises an alert if more than 50 percent were wrong

2. **brute force simulator** the user has up to 5 tries to guess a set password the program reports if you got it right or you ran our of attempts 

3. **login** repates the login check if it fails 3 times then the account is frozen and the program ends

4. **exit** Closes the program


## requirements
- python 3.x (no other libraries needed) 

## how to run
1. clone the repo and switch to this branch:
``` bash
git clone https://github.com/YOURUSERNAME/prog-for-cybercw1.git
cd prog-for-cyber-cw1
git switch SecurityTool
```
2 Run the program:
``` bash
python SecurityTool.py
```
log in when prompted then pick an option from the menu

## example 
**input** a valid username and password then menu option `1` then 10 password entries some right some wrong

**output**
```
correct passwords: 4
inoccrect passwords:6
percentage incorrect 60.0%
Alert: more than 50 percent of the passwords entered were incorrect
```
Username = Admin

Password = Secure123

## input validation and error handling

- wrong login derails are counted and the account is frozen after 3 wrong attempts

- an invalid menu choice shows an error message and the menu is displayed again

- division by zero is prevented in the percentage calc 

- whitespace around the menu choice is removed so a stray space is not treated as invalid

- `try except` catches ctrl+c and end of input so the program exits cleanly instead of crashing

## testing evidence 
