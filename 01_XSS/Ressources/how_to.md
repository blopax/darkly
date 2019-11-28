# The issue
XSS (Cross Site Scripting) enables to inject client side code to other users.


## How to reproduce it on the website?
On page http://10.13.0.53/?page=feedback

Enter   
name: bob  
message: `<script>alert('bob');</script>`


## Why is it a problem?
When validating the form, this script is saved in the database. It is then called a persistent XSS.
Any user that will open the feedback page will be subject to this script that could ask for personal information 
and send it to another address for instance. It could send the cookie of the new user to the hacker user.


## How to avoid it?
The best way to avoid it is to use a good framework (for instance django with ORM). Or to be sure to escape correctly symbols like <. >, &, ', " 
and transform them in their html notation. 
Beware of using a simple replace('<script>', '') as it could be hacked by a simple '<sc<script>ript>'

