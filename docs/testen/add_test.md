# Hoe voeg je een test toe?
## Python
Maak een test dockerfile voor deze test, steek deze in /mastersoftware/QueueHandler/
<br>
Pas rebuild_images_on_master.yml aan zodat deze een docker container maakt en pusht naar de dockerhub repo.
<br>
Je runt deze file met volgend commando.

```
ansible-playbook rebuild_images_on_master.yml
```
<br>
Voeg in de master.py file een extra if toe zodat de queue ook werkt met de toegevoegde test.
<br>

![image](https://user-images.githubusercontent.com/78704181/171904799-210cef20-31e7-4adb-b20e-c7727b908295.png)

Als je de test op deze manier toevoegt, is het belangerijk dat je dezelfde structuuur behoudt als de andere testen.
Steek de test in een methode die een paramter vraagt. Deze methode zal dan het resultaat returnen.
Maak dan een variabele aan die de methode aanroept met parameter sys.argv[1] en als row id  sys.argv[2].
Onderstaande code is van onze 5de test. Je kan deze SQL code kopiëren. Wel moet je test5 veranderen naar het corresponderende nummer.
![image](https://user-images.githubusercontent.com/78704181/171905272-579ff27e-247a-4dc0-beaf-b425556323f7.png)

## API
De api aanpassen is simpel. Je moet maar één file aanpassen, de main.py file. Pas de InsertIntoQueue methode aan en voeg de test toe aan de Resultaat class.
![image](https://user-images.githubusercontent.com/78704181/171906438-eec63b5a-1c73-48b0-8bb0-2885421ca3e8.png)

## Database
Dit is ook redelijk simpel voorzien. In de tabellen queue en result maak je een extra row voor de test.
Zorg ervoor dat deze row dezelfde naam heeft als je diegene die je hebt gebruikt in de code!
