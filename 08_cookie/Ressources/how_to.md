# The issue
Cookies exploits are common. No important values should be passed. It should be considered as any value passed in a url.


## How to reproduce it on the website?
Modify the value of the cookie `I_am_admin` to True encryted in md5.


## Why is it a problem?
If by modifying the cookie you can become an admin, anyone could act as an admin. 
No important values (like the password) or sensitive variables should be passed in a cookie.

## How to avoid it?
Never trust user input. You can use random cookies to avoid easy modifiable cookie. Sensitive information should be store in back-end never in the front.
Use randomly created session ids to identify users.
