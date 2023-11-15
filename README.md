# Iserv-LMS
 
## Simple tools for Iserv of LMS. Made with selenium and python

## Login
┌── Login\
│   ├── login.py\
│   └── login-with-mfa.py\

Simple login script either with or without mfa support. Uses as default Firefox to open\

## Setup

To setup login without mfa, replace username and password with yourselfs.\
To setup login with mfa, you will need to write down the secret key during setup. If you already setup mfa, you can either add another one or restart the setup by deleting and creating your mfa key (be sure to disable mfa before deleting it)