""" Dictionaries of all VALORANT agents with their respective UUIDs, categorized by role. """

list_all_agents = {
    "Jett" : "add6443a-41bd-e414-f6ad-e58d267f4e95",
    "Reyna" : "a3bfb853-43b2-7238-a4f1-ad90e9e46bcc",
    "Raze" : "f94c3b30-42be-e959-889c-5aa313dba261",
    "Yoru" : "7f94d92c-4234-0a36-9646-3a87eb8b5c89",
    "Phoenix" : "eb93336a-449b-9c1b-0a54-a891f7921d69",
    "Neon" : "bb2a4828-46eb-8cd1-e765-15848195d751",
    "Breach" : "5f8d3a7f-467b-97f3-062c-13acf203c006",
    "Skye" : "6f2a04ca-43e0-be17-7f36-b3908627744d",
    "Sova" : "320b2a48-4d9b-a075-30f1-1f93a9b638fa",
    "KAY/O" : "601dbbe7-43ce-be57-2a40-4abd24953621",
    "Killjoy" : "1e58de9c-4950-5125-93e9-a0aee9f98746",
    "Cypher" : "117ed9e3-49f3-6512-3ccf-0cada7e3823b",
    "Sage" : "569fdd95-4d10-43ab-ca70-79becc718b46",
    "Chamber" : "22697a3d-45bf-8dd7-4fec-84a9e28c69d7",
    "Omen" : "8e253930-4c05-31dd-1b6c-968525494517",
    "Brimstone" : "9f0d8ba9-4140-b941-57d3-a7ad57c6b417",
    "Astra" : "41fb69c1-4189-7b37-f117-bcaf1e96f1bf",
    "Viper" : "707eab51-4836-f488-046a-cda6bf494859"
}

list_deulists = {
    "Jett" : "add6443a-41bd-e414-f6ad-e58d267f4e95",
    "Reyna" : "a3bfb853-43b2-7238-a4f1-ad90e9e46bcc",
    "Raze" : "f94c3b30-42be-e959-889c-5aa313dba261",
    "Yoru" : "7f94d92c-4234-0a36-9646-3a87eb8b5c89",
    "Phoenix" : "eb93336a-449b-9c1b-0a54-a891f7921d69",
    "Neon" : "bb2a4828-46eb-8cd1-e765-15848195d751"
}

list_initiators = {
    "Breach" : "5f8d3a7f-467b-97f3-062c-13acf203c006",
    "Skye" : "6f2a04ca-43e0-be17-7f36-b3908627744d",
    "Sova" : "320b2a48-4d9b-a075-30f1-1f93a9b638fa",
    "KAY/O" : "601dbbe7-43ce-be57-2a40-4abd24953621"
}

list_sentinels = {
    "Killjoy" : "1e58de9c-4950-5125-93e9-a0aee9f98746",
    "Cypher" : "117ed9e3-49f3-6512-3ccf-0cada7e3823b",
    "Sage" : "569fdd95-4d10-43ab-ca70-79becc718b46",
    "Chamber" : "22697a3d-45bf-8dd7-4fec-84a9e28c69d7"
}

list_controllers = {
    "Omen" : "8e253930-4c05-31dd-1b6c-968525494517",
    "Brimstone" : "9f0d8ba9-4140-b941-57d3-a7ad57c6b417",
    "Astra" : "41fb69c1-4189-7b37-f117-bcaf1e96f1bf",
    "Viper" : "707eab51-4836-f488-046a-cda6bf494859"
}

def deulists():
    return list_deulists

def initiators():
    return list_initiators

def sentinels():
    return list_sentinels

def controllers():
    return list_controllers

def returnAgents(role):
    if (role == 'deulists'):
        return list_deulists
    if (role == 'initiators'):
        return list_initiators
    if (role == 'sentinels'):
        return list_sentinels
    if (role == 'controllers'):
        return list_controllers
