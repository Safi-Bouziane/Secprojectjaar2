# SecProjectArgus
### Hoe start je het systeem?
In SecProjectArgus/Ansible/ steken beide .yaml files.
Start de slave.yaml file op en deze zal de slaves builden.
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
Start de api's manueel in de 2 slaves. Ga naar SecProjectArgus/Ansible/slave_software/ en voer volgend commando op beide hosts.
```
uvicorn mainapi:app --host 0.0.0.0 --port 8000 
```
Ga dan naar de master server en start master.py
```
python3 ~/SecProjectArgus/Ansible/master_software/QueueHandler/master.py
```
Start de main api op. Ga naar ~/SecProjectArgus/Ansible/master_software/api/app
```
uvicorn main:app --host 0.0.0.0 --port 8000 
```
Start de resulthandler api op. Ga naar ~/SecProjectArgus/Ansible/master_software/ResultHandler
```
uvicorn ResultHandler:app --host 0.0.0.0 --port 9000 
```
## Voor het downloaden van alle images, nodig voor de test containers te builden en te maken, run volgende commando's.

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
