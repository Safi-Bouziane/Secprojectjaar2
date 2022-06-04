# Hoe zet je nginx op?
Ik heb volgende sites gebruikt om alles op te zetten. Ik heb in plaats van your_domain secproject gebruikt, hier moet je rekening mee houden.
<br>
https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-20-04
<br>
https://certbot.eff.org/instructions
## config files
Deze config file zorgt voor ip redirectie. Dit is de default file die je zal vinden in /etc/nginx/sites-enabled.
```
server {
        listen 80;
        server_name 20.29.225.200;
        return 302 $scheme://deltateam.be$request_uri;
        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
        server_name _;
        location / {
                try_files $uri $uri/ =404;
        }
}
```
Dit is de config file voor ons domein. Ik heb deze secproject genoemd en roep deze ook zo aan in onze files. proxy_pass zorgt ervoor dat onze main site aan de api kan.
```
server {

        root /var/www/secproject/html;
        index index.html index.htm index.nginx-debian.html;

        server_name Deltateam.be www.Deltateam.be;
        location /result {
               proxy_pass http://20.29.225.200:9000/docs;
        }
        location /resulhandleropenapi.json {
               proxy_pass http://20.29.225.200:9000/resulhandleropenapi.json;
        }
        location /user/signup {
               proxy_pass http://20.29.225.200:8000/user/signup;
        }
        location /user/login {
               proxy_pass http://20.29.225.200:8000/user/login;
        }
        location /api {
               proxy_pass http://20.29.225.200:8000/docs;
        }
        location /openapi.json {
               proxy_pass http://20.29.225.200:8000/openapi.json;
        }
        location /add {
               proxy_pass http://20.29.225.200:8000/add;
        }
        location / {
               try_files $uri $uri/ =404;
        }

    listen [::]:443 ssl ipv6only=on; # managed by Certbot
    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/www.deltateam.be/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/www.deltateam.be/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot



}
server {
    if ($host = www.deltateam.be) {
        return 301 https://$host$request_uri;
    } # managed by Certbot


    if ($host = deltateam.be) {
        return 301 https://$host$request_uri;
    } # managed by Certbot

        listen 80;
        listen [::]:80;
        server_name Deltateam.be www.Deltateam.be;
    return 404; # managed by Certbot
}
```
## api
De landing page staat in /var/www/secproject/html. Dit is de pagina die je krijgt als je naar ons domein (deltateam.be) surft. je hebt als endpoints ook /result en /api.
In /api zie je de documentatie van onze main api. Hhier kan je data naar onze queue sturen. Voor je dat kan doen moet je je eerst registreren en inloggen. Je krijgt dan een token die je kan gebruiken om de main api te gebruiken.
In /result kan je het resultaat van de testen opvragen. Je hebt hier 2 mogelijke api calls.
1) results: Hier geef je een ip mee en krijg je de test resultaten terug.
2) verify: Hier geef je weer het ip en als je bij verify true zet worden de resultaten van die test uit de database verwijderd. Als je dit niet doet blijven ze in de database.
