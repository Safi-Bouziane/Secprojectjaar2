# Ansible
## Waarom?
we hebben gebruik gemaakt van ansible om de configuratie van ons project zo gebruikersvriendelijk mogelijk te maken.

## Key features
Belangerijke stappen die onze ansible playbooks gaan uitvoeren:
1. Installeren van docker.
2. De juiste code copieren naar de specifieke hosts.
3. Python installeren.
4. De nodige python packages installeren.
5. Firewall instellen.
6. Inloggen op docker hub.
7. Custom images pullen van de private repository.



## Welke stappen worden er gezet.

Voor het systeem te configureren moeten er 3 zaken gebeuren:

1. Configureren van ssh keys.
4. Het sudo password tijdelijk weghalen.
2. configureren en runnen van ansible-playbook
3. (Enkel voor de master) runnen van master.py


## Stap 1: configureren ssh-keys

Voor dat we de keys kunnen instellen op de target servers moeten we natuurlijk eerst een key genereren.

Dit doen we met het commando 

`ssh-keygen`


Wanneer dit gebeurd is zal u een key gegenereerd hebben, u heeft nu een publieke en een private key. Het is uiterst van belang dat u uw private key nooit deelt, deze bied u toegang tot uw infrastructuur. 

---

om nu de keys te kopiëren naar de servers doet u dit met het commando 

`ssh-copy-id [gebruikersnaam]@[ipvanuwhost]`

- gebruikersnaam: gebruikersnaam van de gebruiker op de server.
- ipvanuwserver dit is het publieke ip van uw server.
Staat uw ssh poort anders ingesteld zal u het argument `-p poortnummer`moeten toevoegen om dit mogelijk te kunnen maken. 

## Stap 2: sudo password tijdelijk weghalen

U opent een ssh sessie met uw key naar de host.

`ssh -i "[privatekey]" [gebruiker]@[ipvanuwhost]`

Vervolgens geeft u het commando in:

`sudo visudo`

Het systeem zal uw wachtwoord vragen.

Zoek deze lijn:

%sudo ALL=(ALL) ALL

En verander het naar:

%sudo ALL=(ALL) NOPASSWD: ALL


## Stap 3: ansible configureren en runnen

De eerste stap die we hier moeten zetten is het toevoegen van onze hosts(servers) aan onze inventory. 

Als u gaat kijken vind u een file in de ansible map genaamd "inventory".
Deze file gaat u openen en aanpassen naar uw configuratie. 

Voor de master gaat u deze lijn moeten toevoegen met uw gegevens.
```
[master]
[ipvanuwhost] ansible_user=master
```
En voor elke slave doet u het volgende.
```
[slave]
[ipvanuwhost] ansible_user=slave
```
In deze handleiding werken we met haakjes voor aan te duiden waar u uw gegevens moet ingeven. bij dit deel moet u er wel op letten dat u de haakjes rond de naam van de host wel laat staan. 

---

Daarna dient u den hosts en de user te specifieren van bove in de playbooks: 
In de makemaster playbook:
![Image](playbookImage1.png)
U doet het zelfde met alle slaves in de makeslave playbook.

---

En dan nu kan u ze runnen met het commando: 

`ansible-playbook MakeSlave.yml`

`ansible-playbook MakeMaster.yml`

## Stap 4: runnen van de master.py

U logt in met u key op de master host(server).

`ssh -i "[privatekey]" [gebruiker]@[ipvanuwhost]`

- Privatekey: dit is de key die niet eindigt met .pub.

Vervolgens gaat u naar de juiste directory met het commando:

`cd /home/[user]/master_software/Queuehandler/``

En voert u het commando uit:

`python master.py &`