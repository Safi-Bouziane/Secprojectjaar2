# API

## Landingpage
De landing page staat in /var/www/secproject/html. 
Dit is de pagina die je krijgt als je naar ons domein (deltateam.be) surft. 

## Endpoints
De aanwezige endpoints zijn /result en /api.

### /api
In /api zie je de documentatie van onze main api. Hhier kan je data naar onze queue sturen. Voor je dat kan doen moet je je eerst registreren en inloggen. 
Je krijgt dan een token die je kan gebruiken om de main api te gebruiken.

### /result
In /result kan je het resultaat van de testen opvragen. Je hebt hier 2 mogelijke api calls.
- results: Hier geef je een ip mee en krijg je de test resultaten terug.
- verify: Hier geef je weer het ip en als je bij verify true zet worden de resultaten van die test uit de database verwijderd. Als je dit niet doet blijven ze in de database.
