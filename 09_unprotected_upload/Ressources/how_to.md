# The issue
Unprotected uploads check for the user upload in the front-end but doesn't do it in the back-end.


## How to reproduce it on the website?
Go to http://10.13.0.196/?page=upload
Upload a php file (eg the test.php file in this Ressources folder).
In Firefox developers tool you can resend it in the Network tab changing the HTTP request body `Content-Type: text/php`
to `Content-Type: image/jpeg`.
Opening it in a new tab will display the flag.


## Why is it a problem?
By modifying the HTTP parameters you can send a php file instead of the desired format. If in the php file you write malicious code, 
this code could run on the server.

## How to avoid it?
Never trust user input. Check for the uploaded file in the back-end too. 
You can also give the right permissions to the upload directories to prevent code from being executed. You can check the mime-tupe with getimagesize() and the extension of the folder.
Don't put the .htaccess in the upload directory as it enable malicious code to run the code.