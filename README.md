# Trad-Teve: traditionell teve med python och vlc

## Syfte
Traditionell teve och radio att ha i bakgrunden är en rätt trevlig tanke ändå.
Utbudet lämnar dock ett och annat att önska.
För den som råkar ha ett antal videofiler på sin hårddisk så finns dock byggstenarna till mediauppspelning programmerad efter eget tycke. 
Detta är en ansatts att skapa en programmerbar teve-tablå utefter de filer man har på disk.

## Beskrivning

## Användning
```
# Klona trad-teve och navigera till roten av den nya katalogen.

# Skapa en lokal miljö för python
python3 -m venv env

# Aktivera miljön
. env/bin/activate

# Installera beroenden
python3 -m pip install -r requirements.txt

# Kör igång
python main.py <filnamn>
```

## Att göra
- [x] videofil kan spelas upp via vlc
- [ ] videofiler kan spelas upp i följd
- [ ] videofiler kan spelas upp enligt mönster som delvis beror på angett filträd
- [ ] teve-tablå kan genereras och visas mellan avsnitt, med bakgrundsmusik
 
## Begränsningar
För närvarande skriver jag inte det här projektet med videoströmmning i åtanke.

## Länkar
- https://pypi.org/project/python-vlc/
- https://pypi.org/project/moviepy/
