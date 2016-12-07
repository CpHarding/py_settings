# py_settings
Settings files for Python

ever wanted to have a easy way to store and retrieve data to file?

look no further. This saves data in a file in JSON format.

Tested on 3.5.1, and 2.7.11

Instantiation:
```python
>from py_settings import Settings
>settings = Settings(__file__)
```
Creates a file called 'settings.ini' on the same level as __file__

```python
>from py_settings import Settings
>settings = Settings(__file__, filename='My_custom_settings.conf')
```
Creates a file called 'My_custom_settings.conf' on the same level as __file__

```python
>from py_settings import Settings
>settings = Settings(r'C:\my_project')
```
Creates a file with the default name on the same level as C:\my_project

##Usage:
### Adding a Value
```python
>settings.set('Some_Name', 'Some_Value')
```
adds a value 'Some_Value' under the key 'Some_Name'

or you can a value when you get it

```python
>settings.get('Key, default='Item', add=True)
Item
```
This will return the value in the settings file, unless one is not present, then it will return 
the default, and add it to the settings file

### Getting a Value
```python
>settings.get('Key')
None
>settings.get('Key', default='Item')
Item
```

### Seeing the contents of the settings file
```python
>settings.dump()
```


## Examples
```python
import logging
import argparse
from py_settings import Settings

logger = logging.getLogger(__file__)

settings = Settings(__file__)

parser = argparse.ArgumentParser()
parser.add_argument('--log', default=setttings.get('log', default='INFO', add=True))

args = parser.parse_args()

logger.setLevel(args.log)
```

This will create a settings file on first run, with a log level as INFO specified in it.
This allows temporary changes to the value (from command line) or changes which persist between runs, in the settings file.


