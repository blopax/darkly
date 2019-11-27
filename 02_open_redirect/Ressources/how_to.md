# The issue
On the front end we can modify the source code and change the redirect target.

## How to reproduce it on the website?
On page http://10.13.0.53/
Go to social icons and inspect them

Change
`<a href="index.php?page=redirect&amp;site=twitter" class="icon fa-twitter"></a>`
by 
`<a href="index.php?page=redirect&amp;site=bob" class="icon fa-twitter"></a>`



## Why is it a problem?
The redirect looks for the website passed in the data. This data can be changed. So it creates an unexpected error on the server.


## How to avoid it?
Don't trust user input before handling it with your server.
In this case the link to the social pages could be directly there without redirect. Or the redirection should be handled more thorougly.
