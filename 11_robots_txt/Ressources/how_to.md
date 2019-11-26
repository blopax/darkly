# The issue
The robots.txt can give access to hidden folders. No sensitive information should be inside. 

## How to reproduce it on the website?
Go to http://10.13.0.196/robots.txt

Find out that a `/.hidden/` page exists. This folders has thousands of files nested.
The scrap.py aims to find if there is any interesting information.

Modify the line 26 of the scrap.py file so it corresponds to your website. Run `python3 scrap.py`. It will show that there is a flag hidden inside.

## Why is it a problem?
You let the hacker access to sensitive information even if it is hidden in a lot of files, some sci


## How to avoid it?
Be sure not to let any sensitive information anywhere on the website even if the page is not directly accessible through clicks.
The htpasswd should be out of reach of anyuser and well protected outside of the web root folder.
In this case also get a better password to avoid brutforce attack.