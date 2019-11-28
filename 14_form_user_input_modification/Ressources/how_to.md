# The issue
User input in form can be modified.

## How to reproduce it on the website?
On page http://10.13.0.53/index.php?page=survey#

in the source code look for the dropdown and change the value to `10000` befre sending the form.


## Why is it a problem?
In this specific example for instance it changed the average votes of the survey by using a value that has nothing to do with the proposed values.


## How to avoid it?
Don't trust user input. Handle values that come from form and check for errors.