# Hoe voeg je een test toe?
## Python
Maak een testen dockerfile voor deze test, steek deze in /mastersoftware/QueueHandler/
<br>
pas rebuild_images_on_master.yml aan zodat die deze docker container maakt en pusht naar onze dockerhub repo.
<br>
je runt deze file met volgend commando.

```
ansible-playbook rebuild_images_on_master.yml
```
<br>
Voeg in master.py een extra if toe, zodat de queue ook werkt met deze.
<br>

![image](https://user-images.githubusercontent.com/78704181/171904799-210cef20-31e7-4adb-b20e-c7727b908295.png)

Als je de test op deze manier toevoegt is het belangerijk dat je dezelfde structuuur als de andere testen hebt.
dus steek de de test in een methode die een paramter vraagt, die methode returned het resultaat.
maak dan een variabele die de methode aanroept met parameter sys.argv[1] en als row id  sys.argv[2]
onderstaande code is van onze 5de test. je kan deze sql code kopieren je moet wel test5 veranderen naar het juiste nummer.
![image](https://user-images.githubusercontent.com/78704181/171905272-579ff27e-247a-4dc0-beaf-b425556323f7.png)

## API
De api aanpassen is simpel. Je moet maar een file aanpassen dat is de main.py. Pas de InsertIntoQueue methode aan en voeg de test toe aan de Resultaat class
![image](https://user-images.githubusercontent.com/78704181/171906438-eec63b5a-1c73-48b0-8bb0-2885421ca3e8.png)

## Database
Dit is ook redelijk simpel voorzien in de tabellen queue en result een extra row voor de test. 
Zorg ervoor dat deze row dezelfde naam heeft als je diegene die je hebt gebruikt in de code!!
