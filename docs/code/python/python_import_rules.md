# Import rules

Cf [bible](https://google.github.io/styleguide/pyguide.html#22-imports) 2.2 & 2.3

## Rules

- Pas d'import relatif
- Pas d'import de fonction/variable direct (sauf  dans `__init__.py`)
- Pas de `import *` (sauf  dans `__init__.py` pour des trucs génériques comme `constants.py` qui stock les constantes et `functional.py` qui stock des fonctions utilitaires)

## Examples

`OK`
```python
from tini.model.encoder import vision
...
vision.blabla()
vision.toto()
```
`OK` (mais plus verbeux)
```python
from tini.model.encoder.vision
...
tini.model.encoder.vision.blabla()
tini.model.encoder.vision.toto()
```

`NOK`
```python
from tini.model.encoder.vision import blabla, toto
...
blabla()
toto()
```


`utils` (dossiers `\utils` ou fichiers `utils.py` ) "éclatés" dans les `__init__.py` donc pas besoin de les importer
```python
# vision/__init__.py
from tini.model.encoder.vision.utils import *

# vision/utils/__init__.py
from tini.model.encoder.vision.utils import debug, ... # vision.utils.debug -> vision.debug
from tini.model.encoder.vision.utils.constants import * # Expose le contenu de constants.py
from tini.model.encoder.vision.utils.functional import * # Expose le contenu de functional.py

# elsewhere.py
from tini.model.encoder import vision

vision.debug.Dumper() # Dumper dans vision/utils/debug
vision.detection.find_theta_class() # find_theta_class dans vision/utils/detection
vision.CURVE_TYPE  # CURVE_TYPE dans vision/utils/constants.py
```

Ca permet d'avoir une architecture plus propre/mieux rangée sans se compliquer la vie avec des imports à rallonge


On utilise l'arborescence et les imports comme information sur ce que la fonction fait

`OK`
```python
#vision/detect.py
def blobs():
    ...

def elements():
    ...

#vision/controller.py
from tini.model.encoder.vision import detect

detect.blobs() # Detecte les blobs
detect.elements() # Detecte les elements
```
`NOK` (redondant)
```python
#vision/detect.py
def detect_blobs():
    ...

def detect_elements():
    ...

#vision/controller.py
from tini.model.encoder.vision import detect

detect.detect_blobs() # detect est redondant
detect.detect_elements() # detect est redondant
```

`NOK` (on importe pas les fonctions/variables directement)
```python
#vision/detect.py
def detect_blobs():
    ...

def detect_elements():
    ...

#vision/controller.py
from tini.model.encoder.vision.detect import detect_blobs, detect_elements

detect_blobs()
detect_elements()
```

On peut exposer une function quand elle a le même nom que son fichier, pour éviter les redondances

```python
#tini/model/encoder/vision/preprocessing/mava.py
def mava(x):
    ...

#tini/model/encoder/vision/preprocessing/__init__.py
from tini.model.encoder.vision.preprocessing.mava import mava

#elsewhere.py
from tini.model.encoder.vision import preprocessing

y = preprocessing.mava(x) # apply mava preprocessing to some input x
```
