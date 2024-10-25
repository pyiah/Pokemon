from dmoncl import *

class Player:
    def __init__(self,  username: str, p_monsters: list):
        self.username = username
        self.p_monsters = p_monsters

    def Fight(self):
        mon_list = []
        for x in self.p_monsters:
            mon_list.append(x.name)
        return "-----BEGIN FIGHT-----", self.username, "--".join(mon_list)
    
    def Moves(self):
        choice = input("pick your move " + "--".join(self.p_monsters[0].moves["Moves"]))
        if choice == ""

class Opponent:
    def __init__(self,  username: str, o_monsters: list):
        self.username = username
        self.o_monsters = o_monsters

player = Player("Zachary", [Orgo, Borg])
opponent = Opponent("Oliver", [Borg, Orgo])

print(player.Fight())

while True:
    if player.p_monsters[1].speed_stat > opponent.o_monsters[1].speed_stat:
        print(player.p_monsters[1].speed_stat)
    else:
        player.Moves()
        break