# Roboworks
An AI assistant in Geometry Dash that cares more then Obama Care. RobTop if you find an excuse to add better security to make comment uploading a pain then I swear to god I will hit you and knock you on the floor then proceed to do the gangnam style.
## Folders
```
cloudflare-workers - AI for Cloudflare Workers
geometry-dash (WIP) - Geometry Dash bot
php-api - API for your website.
website (WIP) - Why not use a cool HTML frontend instead if you hate yourself that much to install Python.
```
## Setup cloudflare-workers
Create a cloudflare worker with the `@cf/meta/llama-2-7b-chat-int8` AI model on the `Workers & Pages` part of the dashboard. Hook up a custom domain to be fancy.
## Setup php-api (optional, but lets be real plaintext apis are the bomb) (dont read readmes on planes)
Upload the api.php file on your webhost or selfhost it through Cloudflare Tunnels and change the link in the PHP file to your Cloudflare Worker URL.
## Setup geometry-dash
Edit the config part of main.py and install Python 3.8 and install emoji==1.5 through pip. if requests module doesnt work correctly then install requests==2.12.0 through pip. 
## Setup website
Same as php-api instructions but upload index.html or selfhost it.
