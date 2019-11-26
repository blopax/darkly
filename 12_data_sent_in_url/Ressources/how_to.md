# The issue
Login page allows brutforce which enables to login as a user that has a common password.

## How to reproduce it on the website?
On page  http://10.13.0.196/?page=media&src=nsa

Inspecting the code we can see: `<object data="http://10.13.0.196/images/nsa_prism.jpg"></object>`

The source is directly passed as url. You can then pass another kind of data. 
For instance `<script>alert('hack')</script>` which encoded is: `PHNjcmlwdD5hbGVydCgnaGFjaycpPC9zY3JpcHQ+`

So you can now call the page: `http://10.13.0.196/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgnaGFjaycpPC9zY3JpcHQ+`

## Why is it a problem?
Since PHP allows object serialization, attackers could pass ad-hoc serialized strings to a vulnerable unserialize() call, resulting in an arbitrary PHP object(s) injection into the application scope. 

## How to avoid it?
Never trust user input and the data should be generated in the back-end.
Do not use unserialize() function with user-supplied input, use JSON functions instead. 