# The issue
Sensitive information in source code and HTTP headers modification.

## How to reproduce it on the website?
On page http://10.13.0.196/?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c 

In the source code, it is written than changing the referer to `https://www.nsa.gov/` and the browser to `ft_bornToSec` you could access a specific page.
In the network tab of the firefox inspector tool you can modify those and access to the page.


## Why is it a problem?
You can access specific pages depending on the HTTP headers parameters.

## How to avoid it?
HTTP headers can be modified. So don't rely on it to guarantee access to specific parts of your website.
It is better to create users in your database to set who can access what.