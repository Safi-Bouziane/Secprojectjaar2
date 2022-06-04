# SecProjectArgus
### Hoe start je het systeem?
Fork deze repo eerst. Dan kan je het systeem aanpassen zoveel als je wilt.

In SecProjectArgus/Ansible/ steken beide yaml files. Pas hier in de inventory van de slaves en master aan indien nodig. Pas in master.py de ip's van de slaves ook aan.
<br>
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
Ga dan naar de master server en start master.py
```
python3 ~/SecProjectArgus/Ansible/master_software/QueueHandler/master.py
```

## Als je alles manueel wilt opstarten
Clone deze repo op al je machines.
Start de api's manueel in de 2 slaves. ga naar SecProjectArgus/Ansible/slave_software/ en voer volgend commando op beide hosts.
```
uvicorn mainapi:app --host 0.0.0.0 --port 8000 
```
Ga dan naar de master server en start master.py
```
python3 ~/SecProjectArgus/Ansible/master_software/QueueHandler/master.py
```
Start de main api op. ga naar ~/SecProjectArgus/Ansible/master_software/api/app
```
uvicorn main:app --host 0.0.0.0 --port 8000 
```
Start de resulthandler api op. ga naar ~/SecProjectArgus/Ansible/master_software/ResultHandler
```
uvicorn ResultHandler:app --host 0.0.0.0 --port 9000 
```
## Voor het downloade van alle images nodig voor de test containers te builden en maken run deze commando's

### Login op docker
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
### Als je de images wilt rebuilden doe volgend commando in SecProjectArgus/Ansible/
```
ansible-playbook rebuild_images_on_master.yml
```
