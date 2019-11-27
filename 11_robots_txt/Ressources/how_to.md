# The issue
The robots.txt can give access to hidden folders. No sensitive information should be inside. 

## How to reproduce it on the website?
Go to http://10.13.0.196/robots.txt

Find out that a `/.hidden/` page exists. This folders has thousands of files nested.
The scrap.py aims to find if there is any interesting information.

Run `python3 scrap.py WEBSITE`. WEBSITE should just be the main ip (something like 10.13.0.196) It will show that there is a flag hidden inside.

## Why is it a problem?
You let the hacker access to sensitive information even if it is hidden in a lot of files, some script can help targetting valuable information.


## How to avoid it?
Be sure not to let any sensitive information anywhere on the website even if the page is not directly accessible through clicks.
