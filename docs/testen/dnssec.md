# DNSSEC check

## Bedoeling van de check
Met deze test wordt er gekeken of het meegegeven ip adres DNSSEC heeft.

## Werking van de code
Voor de test hebben we volgende libraries nodig.
```
import urllib.request
```

Met volgende code checken we op de aanwezigheid van DNSSEC.
```
results = urllib.request.urlopen('http://portfolio.sidnlabs.nl/check/%s' % Url).read()
```

Het vervolg van de code wordt gebruikt voor het weergeven van het resultaat.
```
newResults = results.decode('utf-8').split()
                finalResult = newResults[0].replace(Url, '').replace(',', '')
                return Url + " is " + finalResult + " with DNSSEC."
```
