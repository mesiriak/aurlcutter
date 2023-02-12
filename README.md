<h1>aurlcutter</h1>

#### Simple asynchronous python url shortener api wrapper

---
**Source code**: <a href="https://github.com/mesiriak/aurlcutter" target="_blank">https://github.com/mesiriak/aurlcutter</a>

---


### Installation guide:
```
pip install aurlcutter
```

### For watcing full list of services:
#
```python
from aurlcutter import Cutter

cutter_instance = Cutter()

print(cutter_instance.cutters)

>>> ["tinyurl", "isgd", "dagd", ...]
```

### Usage example:
#
```python
from aurlcutter import Cutter

cutter_instance = Cutter()

your_link = "www.google.com"

# you can choose api what you need by yourself
cutted_link = cutter_instance.tinyurl.cut(your_link)
>>>>>>> Stashed changes
