# The issue
This exploit uses the include() fucntions of php that enables to access to pages that are stored outside the web root folder.

## How to reproduce it on the website?
On page http://10.13.0.196/?page=../../../../../../../../../../../../../../etc/passwd 


## Why is it a problem?
A hacker that uses classic patterns can navigate in the server and access sensitive content (in this case the /etc/passwd)

## How to avoid it?
 * Prevent access to pages that are at the root of the website. 
 * Don't show the files in a repertory without index file.
 * Delete useless directory and files. Be sure that the server protect the access to files with sensitive data
 * Prefer working without user input when using file system calls
 * Ensure the user cannot supply all parts of the path – surround it with your path code
 * Validate the user’s input by only accepting known good – do not sanitize the data
 * Use chrooted jails and code access policies to restrict where the files can be obtained or saved to
