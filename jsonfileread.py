import pandas as pd
#import JSON file into python
#json: JavaScript Object Notation (JSON) is a standard text-based format for representing structured data based on JavaScript object syntax
data=pd.read_json('*.json')
data.head() 