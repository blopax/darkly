# Darkly 
Darkly is a web security project.
Project done with ccorsin.


## Objective 
An iso is provided. You need to launch it on a VM and find 14 exploits.


## How to launch the iso
After downloading the iso, launch Virtualbox. Create a new Machine (Linux/Debian 64bits).
Change the network settings to "bridged adapter"
Launch the VM with the downloaded iso.


## Ressources
Here are some useful ressources:
* OWASP
* OWASP Top 10 application security risks (2017): https://www.owasp.org/index.php/Top_10-2017_Top_10
* OWASP top 10 vulnerabilities explained: https://www.youtube.com/playlist?list=PLyqga7AXMtPPuibxp1N0TdyDrKwP9H_jD


Here are some useful tools:
* Hashtoolkit: https://hashtoolkit.com/
* base64encoder: https://www.base64encode.org
* sqllmap: helps finding SQL injection for instance using commands like: 
`sqlmap -u http://192.168.99.100/index.php\?page\=member\&id\=1\&Submit\=Submit\# —tables` and 
`sqlmap -u http://192.168.99.100/index.php\?page\=member\&id\=1\&Submit\=Submit\# --dump -T users`

## Some other exploits that are not present in this iso
* CSRF: https://www.youtube.com/watch?v=13QPmRuhbhU
* Broken authentification with session ID stored in browser and not refreshed if you disconnect. (Another user on the same computer can access to your session)
