# ValAgents.py | Valorant Agents Module

A Python module that can return the names of VALORANT agents and/or their respective UUIDs. Fetch by agent role, or fetch all the agents.
This is a much simpler, offline alternative to the official VALORANT API. I will soon make a version of this module which fetches from the API, so you never have to update it.

## ⚙️ Installation

No support for PyPi yet, and thus you cannot install this module with `pip install`. Maybe I will do this in the future.
For now, just download from [here](https://github.com/Mister-SOSA/ValAgents.py/releases/tag/v1.0) and place `ValAgents.py` in your project directory.

## 🔧 Usage & Examples

Be sure that you import the module into your project using
```py
import ValAgents
```

Optionally, you can make your workflow a little smoother by importing it as something like `agents` for example.
```py
import ValAgents as agents
```
Now you can access the module like so:
```py
agents.controllers()
```

By default, all functions return a dictionary with the agent names as the keys, and their UUIDs as the values.
The functions are named after the agents' roles, so that calling `agents.initiators()` will return all the initiators.
You can also access the module as an object, where `agents.list_sentinels` will return the same `dict` as `agents.sentinels()`

Below you can find some examples of the module in action. Here are some potential goals, with a code block showing you how to accomplish
that goal.



### **Print a dictionary with every sentinel as the key, and their respective UUID as the value:**

```py
import ValAgents as agents

sentinels = agents.sentinels()

print(sentinels)
```
***Ouput:***
```py
{'Killjoy': '1e58de9c-4950-5125-93e9-a0aee9f98746', 'Cypher': '117ed9e3-49f3-6512-3ccf-0cada7e3823b', 'Sage': '569fdd95-4d10-43ab-ca70-79becc718b46'}
```

### **Print Jett's UUID:**

```py
import ValAgents as agents

jett_uuid = agents.deulists().get('Jett')

print(jett_uuid)
```
***Output:***
```
add6443a-41bd-e414-f6ad-e58d267f4e9
```

### **Print a list of all the agents alphabetically:**

```py
import ValAgents as agents

all_agents = list(agents.list_all_agents.keys()) # get only agent names from dict

all_agents.sort() # sort the agents alphabetically

print(all_agents)
```
***Output:***
```py
['Astra', 'Breach', 'Brimstone', 'Cypher', 'Jett', 'KAY/O', 'Killjoy', 'Omen', 'Phoenix', 'Raze', 'Reyna', 'Sage', 'Skye', 'Sova', 'Viper', 'Yoru']
```


## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
