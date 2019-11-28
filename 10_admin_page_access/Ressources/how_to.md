# The issue
A lot of websites have an admin page giving access to the back-office. Beware of protecting this access.


## How to reproduce it on the website?
Go to http://10.13.0.196/robots.txt

Find out that a `/whatever/` page exist.

In this page, find out the htpasswd. Open it and find: `root:8621ffdbc5698829397d97767ac13db3`
Decrypt the password it is 'dragon'

On the `http://10.13.0.196/admin/` enter root/dragon and login.

PS: note that it could also be found with brutforce as root is a common username and dragon a common password.

## Why is it a problem?
You give critical information to a hacker that can get access to your back-office.

## How to avoid it?
Be sure not to let any sensitive information anywhere on the website even if the page is not directly accessible through clicks.
The htpasswd should be out of reach of any user and well protected outside of the web root folder.
In this case also get a better password to avoid brutforce attack.
