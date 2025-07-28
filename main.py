class Weapon:
    
    def __init__(self, name: str, demage: float):
        self.name = name
        self.demage = demage


class Player:
    
    def __init__(self, name, team, weapon):
        self.name = name
        self.team = team
        self.weapon = weapon
        self.health = 100

    def shoot(self, target):
        print(f"{self.name} has shooted {target.name}")
        target.health -= self.weapon.demage


weapons = [
    Weapon('AK-47', 30),
    Weapon('Scout', 80),
    Weapon('Deagle', 10)
]

player01 = Player('ali', 'Counter-Terrorist', weapons[0])
player02 = Player('vali', 'Terrorist', weapons[1])

player01.shoot(player02)
print(player02.health)

