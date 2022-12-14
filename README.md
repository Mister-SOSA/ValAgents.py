# ValAgents.py | Valorant Agents Module

A Python module that essentially serves as a wrapper for the Valorant API Agents endpoint.

## ⚙️ Installation

No support for PyPi yet, and thus you cannot install this module with `pip install`. Maybe I will do this in the future.
For now, just download from Releases and place `ValAgents.py` in your project directory.

## 🔧 Usage & Examples

1) Import the module
```py
from ValAgents import ValAgents
```
2) Initialize
```py
agents = ValAgents()
```
3) Start calling stuff
```py
print(agents.get_agent("Breach").ability_q.description)
```

## Objects
### Agent
Results will be returned as `Agent` objects.

|Attribute       |Description                                             |
|----------------|--------------------------------------------------------|
| name           | Agent's display name                                   |
| description    | Agent's official description                           |
| display_icon   | The 256x256 icon that appears in Agent Selection       |
| developer_name | The codename for the agent that is used in development |
| ability_q      | An `Ability` object for the agent's `Ability1`         |
| ability_e      | An `Ability` object for the agent's `Ability2`         |
| ability_c      | An `Ability` object for the agent's `Ability3`         |
| ability_x      | An `Ability` object for the agent's Ultimate           |
| role           | The agent's game role (i.e. Sentinel)                  |
| uuid           | The identification value for the agent                 |

## Ability

Objects representing an agent's in-game ability charge

| Attribute    | Description                                               |
|--------------|-----------------------------------------------------------|
| name         | The ability's display name                                |
| description  | The ability's official description                        |
| display_icon | The icon which appears in the in-game HUD for the ability |

## ValAgents

The main object which houses agent results and methods.

| Method                                | Description                                                                                               |
|---------------------------------------|-----------------------------------------------------------------------------------------------------------|
| `def get_agent(self, name: str)`      | Retrieves an agent by full name. Returns `Agent` object                                                   |
| `def get_agents_by_role(role: str)`   | Retrieve a list of agents by their role (i.e. `Sentinel`). Returns a `list` of `Agent` objects            |
| `def query_agents_by_name(name: str)` | Returns a `list` of `Agent` objects whose names contain the given string. Good for autocomplete and such. |
