#This document is for defining the class monsters and defining all objects-> monsters
class Monster:
    def __init__ (self, name: str, moves: dict, monID: int, 
                  attack_stat: int, defense_stat: int, health_stat: int, monType: str):
        self.name = name
        self.moves = moves
        self.monID = monID
        self.attack_stat = attack_stat
        self.defense_stat = defense_stat
        self.health_stat = health_stat
        self.monType = monType
        
    def Mondex(self):
        print("==========MONDEX==========")
        print("ID:", self.monID)
        print("Monster:", self.name)
        print("Moves:\n", list(self.moves.values())[0][0]," --> ", list(self.moves.values())[1], "Type\n")
        print("Attack Stat:", self.attack_stat)
        print("Defense stat:", self.defense_stat)
        print("Health stat:", self.health_stat)
        print("Typing:", self.monType)
        


Orgo = Monster("Orgo", {"Moves": ["Punch"], "Type": "Fire"}, monID=1, attack_stat=10, defense_stat=11, health_stat=12, monType="Fire")
Borg = Monster("Borg", {"Moves": ["Smack"], "Type": "Water"}, monID=2, attack_stat=10, defense_stat=11, health_stat=12, monType="Water")

Orgo.Mondex()