# The issue
Login page allows credential stuffing (brutforce) which enables to login as a user that has a common password.

## How to reproduce it on the website?
On page  http://10.13.0.53/index.php?page=signin

Enter `admin` + `shadow`

To get those values you can use the brutforce.py file in this folder.
```python3 brutforce.py WEBSITE``` with WEBSITE of the form 10.13.0.53

## Why is it a problem?
A hacker could take control of another account (in this case the admin one...)

## How to avoid it?
Prevent the use of brutforce on your login by limiting failed login and assure you ask for higher password complexity that is not in the list of common passwords.
You can also provide multi factor authentification.
