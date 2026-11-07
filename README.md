# Task 2: security event logger 

**Name:** Josh williams

**Campus:** NCL motherwell

**Banner id:** B01888344

## what the program does
the program asks for a username and password and keeps asking until the login works correctly every attempt regardless if it works or no is logged with:

- a random 4 digit **event id**
- the **username** entered
- the **ip address** of the computer
- the **event** failed or successful login
- a **timestamp** date and time of attempt

the program ends once a login works

## requirements
- python 3.x
- standard libary only so nothing needs installing 

## how to run 
1. clone the repo and switch to this branch: 
```bash
git clone https://github.com/YOURUSERNAME/prog-for-cybercw1.git
cd prog-for-cybercw1
git switch security-event-logger
```
2. run the program:
```bash
python SecurityEventLogger
```
3. enter the demo username and password when prompted 

username = "admin"

password = "secure#2026"



## example output
```
SECURITY EVENT LOG
==================
username: admin
password: wrongpass
event id :4821