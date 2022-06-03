# SecProjectArgus

## Voor de api op te starten doe:
```
uvicorn main:app --host 0.0.0.0 --port 8000 
```
## Voor de queue op te starten, start het master.py scriptje op.

## Voor het downloade van alle images nodig voor de test containers te builden en maken run deze commando's

### login op docker
```
docker login
```
### Inlog gegevens:
```
username: argusproof
password: DeltaTeam
```
### Om alle images tegelijk te pullen:
```
docker image pull --all-tags argusproof/argusproof_deltateam
```
### Hoe start je het systeem?
In SecProjectArgus/Ansible/ steken beide yaml files.
Start de slave.yaml file op deze gaat de slaves builden.
<br>
```
ansible-playbook MakeSlave.yml
```
Start dan master.yaml om de master te builden. 
<br>
```
ansible-playbook MakeMaster.yml
```
ga dan naar de master server en start master.py
```
python3 ~/SecProjectArgus/Ansible/master_software/QueueHandler/master.py
```

## Als je alles manueel wilt opstarten
start de api's manueel in de 2 slaves. ga naar SecProjectArgus/Ansible/slave_software/ en voer volgend commando op beide hosts.
```
uvicorn mainapi:app --host 0.0.0.0 --port 8000 
```
ga dan naar de master server en start master.py
```
python3 ~/SecProjectArgus/Ansible/master_software/QueueHandler/master.py
```
start de main api op. ga naar ~/SecProjectArgus/Ansible/master_software/api/app
```
uvicorn main:app --host 0.0.0.0 --port 8000 
```
start de resulthandler api op. ga naar ~/SecProjectArgus/Ansible/master_software/ResultHandler
```
uvicorn ResultHandler:app --host 0.0.0.0 --port 9000 
```
