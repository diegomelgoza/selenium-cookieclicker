# selenium-cookieclicker

Automating the cookie clicker website using Selenium and Selenium ActionChains.

Running the main.py function will start the script.
Chrome will open in a new window and begin clicking cookies.  
It will buy from the store when you have enough cookies and will
prioritze the buying most expensive item in the store.

Currently upgrades cannot be bought, will update that later.

## Things accomplished with this project:
* First time use of ActionChains.
* Used selenium options to add the web extension U-block origins.
  * I was wanted to know if it was possible to add extensions to web automations. 
  After digging around google I learned how to download the extension as a crx file and add the path.
* Used implicitly_wait to make selenium wait for the web page to finish loading.
* Found elements using class name and ID
