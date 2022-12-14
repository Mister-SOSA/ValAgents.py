"""A simple Python module for retrieving Valorant agent data from the Riot Games API."""
import requests


class Agent:
    """A class to represent a Valorant agent."""

    def __init__(self, name, description, display_icon, developer_name, ability_q, ability_e, ability_c, ability_x, role, uuid):
        self.name = name
        self.description = description
        self.display_icon = display_icon
        self.developer_name = developer_name
        self.ability_q = ability_q
        self.ability_e = ability_e
        self.ability_c = ability_c
        self.ability_x = ability_x
        self.role = role
        self.uuid = uuid

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Agent({self.name}, {self.description}, {self.display_icon}, {self.developer_name}, {self.role}, {self.uuid})"


class Ability:
    """A class to represent a Valorant agent ability."""

    def __init__(self, name, description, display_icon):
        self.name = name
        self.description = description
        self.display_icon = display_icon

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Ability({self.name}, {self.description}, {self.display_icon})"


class ValAgents:
    """A class to represent a list of Valorant agents."""

    def __init__(self):
        self.agents = []
        self._get_agents()

    def _get_agents(self) -> None:
        """Retrieves agent data from the Riot Games API."""

        url = "https://valorant-api.com/v1/agents"
        parameters = {"isPlayableCharacter": "true"}

        response = requests.get(url, params=parameters)

        if response.status_code == 200:
            data = response.json()["data"]
            for agent in data:
                name = agent["displayName"]
                description = agent["description"]
                display_icon = agent["displayIcon"]
                dev_name = agent["developerName"]
                ability_q = Ability(agent['abilities'][0]['displayName'], agent['abilities']
                                    [0]['description'], agent['abilities'][0]['displayIcon'])
                ability_e = Ability(agent['abilities'][1]['displayName'], agent['abilities']
                                    [1]['description'], agent['abilities'][1]['displayIcon'])
                ability_c = Ability(agent['abilities'][2]['displayName'], agent['abilities']
                                    [2]['description'], agent['abilities'][2]['displayIcon'])
                ability_x = Ability(agent['abilities'][3]['displayName'], agent['abilities']
                                    [3]['description'], agent['abilities'][3]['displayIcon'])
                role = agent["role"]["displayName"]
                uuid = agent["uuid"]

                self.agents.append(Agent(name, description, display_icon, dev_name,
                                   ability_q, ability_e, ability_c, ability_x, role, uuid))

        else:
            raise Exception(
                f"Failed to retrieve agent data from the Riot Games API. Status code: {response.status_code}")

    def get_agents(self) -> list:
        """Returns a list of Agent objects."""

        return self.agents

    def get_agent(self, name: str) -> Agent:
        """Returns the agent with the given name."""

        return [agent for agent in self.agents if agent.name.lower() == name.lower()][0]

    def get_agents_by_role(self, role: str) -> list:
        """Returns a list of agents with the given role."""

        return [agent for agent in self.agents if agent.role.lower() == role.lower()]

    def query_agents_by_name(self, name: str) -> list:
        """Returns a list of Agent objects whose name contains the given string."""

        return [agent for agent in self.agents if name.lower() in agent.name.lower()] if name else self.agents

    def __getitem__(self, key):
        return self.agents[key]

    def __len__(self):
        return len(self.agents)

    def __iter__(self):
        return iter(self.agents)

    def __str__(self):
        return str(self.agents)

    def __repr__(self):
        return f"ValAgents({self.agents})"
