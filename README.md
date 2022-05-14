# SecProjectArgus

##Voor de api op te starten doe:
```
uvicorn main:app --host 0.0.0.0 --port 8000 
```
##Voor de queue op te starten, start het master.py scriptje op.

##Voor het downloade van alle images nodig voor de test containers te builden en maken run deze commando's
```
docker login
```
###Inlog gegevens:
```
username: argusproof
password: DeltaTeam
```
###Om alle images tegelijk te pullen:
```
docker image pull --all-tags argusproof/argusproof_deltateam
```
