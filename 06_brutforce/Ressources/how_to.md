# The issue
Login page allows brutforce which enables to login as a user that has a common password.

## How to reproduce it on the website?
On page  http://10.13.0.53/index.php?page=signin

Enter `admin` + `shadow`

To get those values you can use the brutforce.py file in this folder.
Modify the line 15 of the file so it corresponds to your website. 
```python3 python3 brutforce.py ```


## Why is it a problem?
A hacker could take control of another account (in this case the admin one...)

## How to avoid it?
Prevent the use of brutforce on your login by preventing unlimited tries and assure you ask for a strong enough password.
