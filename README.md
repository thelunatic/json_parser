PYTHON JSON PARSER
==================

This is a simple json parser library written from scratch
the main objective was to experiment how parsers work and
to implement it myself.

How to use it
=============

From your python file (let's say file.py) :

```
import json_parser as jp

my_dict = jp.load('myjsonfile.json')
print(my_dict)
```

the jp.load returns a dictionary object of the whole json file
So my_dict can be used anywhere you want and invoke the json 
values.

