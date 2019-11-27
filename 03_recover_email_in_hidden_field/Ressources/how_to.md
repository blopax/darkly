# The issue
On the front end we can modify the source code and change the recover email parameters or get access to the webmaster email.

## How to reproduce it on the website?
On page http://10.13.0.53/?page=signin

Examine the source code.

Change
`<input name="hidden" value="webmaster@borntosec.com" maxlength="15" type="text">`
by 
`<input name="mail" value="bob@borntosec.com" maxlength="15" type="text">`



## Why is it a problem?
The recover password can be sent to someone else than the original intended email.

## How to avoid it?
Don't trust user input before handling it with your server even if in a hidden field it can be modified.
In this specific example the whole recover flow is very poor.
