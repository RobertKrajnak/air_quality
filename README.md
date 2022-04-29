# Lokálne nastavenia (bude predbežne doplňané)

## Na stiahnutie

Pre príkaz _npm_ stiahnúť a inštalovať [_node.js_](https://nodejs.org/en/download/).  
Pre spustenie backendu, a teda hlavnej .py aplikácie použite virtuálne prostredie, napr. [_Anacondu_](https://docs.anaconda.com/anaconda/install/windows/).  
Nainštalovať flask k interpréteru pomocou _pip install flask_.

Po _git clone_ je pre spustenie aplikácie nutne vykonať _build_.

```
npm run build
```

Následne sa spustí .py aplikácia pomocou.

```
python .py -v
```

Pre react-chart je potrebné inštalovať modul react-chartjs-2

```
npm install react-chartjs-2
```

Pre Luftdaten a Firebase databazu je potrebne nainstalovať:

```
pip install requests
pip install firebase
pip install python-firebase
pip install firebase-admin
```

Predbežne.. neskôr možno fixneme inak..
Je potrebné pre firebase-admin package zakomentovať a prepísať nasledujúce riadky (kvôli outdated urllib3 package)
v súbore "\_http_client.pycd"

#path : ..\your_env\Lib\site-packages\firebase_admin_http_client.pycd

#zakomentovať:

```
    #from requests.packages.urllib3.util import retry
    #DEFAULT_RETRY_CONFIG = retry.Retry(
    #connect=1, read=1, status=4, status_forcelist=[500, 503],
    #raise_on_status=False, backoff_factor=0.5)
```

#prepísať "retries=1" :

```
def __init__(
        self, credential=None, session=None, base_url='', headers=None,
        retries=1):
```

## Raspberry config:

Pre jednokrokovú inštaláciu všetkých knižníc:

```
curl -sSL https://get.pimoroni.com/enviroplus | bash
```

Povolenie prístupu na raspberry cez ssh:

```
sudo systemctl enable ssh
sudo systemctl start ssh
```

### Ngrok config:

Je nutné vytvorenie účtu na [ngrok](https://ngrok.com). Následne stiahnite samotný ngrok do Raspberry Pi a extrahujte:

```
unzip /path/to/ngrok.zip
```

Nastavte autentifikačný token získaný z ngrok účtu:

```
./ngrok authtoken #auth-token#
```

Pre nastavenie viacerých tunelov je nutné upraviť configuračný súbor ngrok-u:

```
sudo nano .ngrok2/ngrok.yml
```

Zmena daného súboru na:

```
authtoken: #auth-token#
tunnels:
  ssh:
    proto: tcp
    addr: 22
  dashboard:
    proto: http
    addr: 5000
```

- ssh, dashboard - mená pre tunely
- proto - označenie protokolu
- addr - port, ktorý má byť forwardnutý

Následne spustite ngrok:

```
./ngrok start --all
```
