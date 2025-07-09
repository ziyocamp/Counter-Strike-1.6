from termcolor import colored


class Weapon:
    def __init__(self, name: str, price: float, damage: int) -> None:
        self.name = name
        self.price = price
        self.damage = damage

    def shoot(self) -> None:
        print(colored(f"{self.name} fired!", "yellow"))


class Player:
    def __init__(self, name: str, team: str) -> None:
        self.name = name
        self.team = team
        self.health = 100
        self.money = 700
        self.weapon = Weapon("Knife", 0, 15)

        self.join_info()

    def join_info(self) -> None:
        print(colored(f"{self.name} joined {self.team}", "green"))

    def pick_weapon(self, weapen: Weapon) -> None:
        if self.money >= weapen.price:
            self.money -= weapen.price
            self.weapon = weapen
            print(colored(f"{self.name} picked up {weapen.name}", "blue"))
        else:
            print(colored(f"{self.name} has not enough money", "red"))

    def shoot(self, target) -> None:
        self.weapon.shoot()
        target.take_damage(self.weapon.damage)

    def take_damage(self, amount: int) -> None:
        if self.health <= 0:
            self.health = 0
            print(f'{self.name} is already DIED!')
        self.health -= amount
        if self.health <= 0:
            print(colored(f"{self.name} DEAD!", "red"))


def main() -> None:
    weapon01 = Weapon("Knife", 0, 5)
    weapon02 = Weapon("AK-47", 300, 30)
    weapon03 = Weapon("AWP", 500, 100)
    weapon04 = Weapon("Pistol", 150, 100)

    player01 = Player('Sardor', 'Counter-Terrorist')
    player02 = Player('Eldor', 'Counter-Terrorist')
    player03 = Player('Aloxiddin', 'Terrorist')
    player04 = Player('Nodir', 'Terrorist')

    player01.pick_weapon(weapon02)

    player02.pick_weapon(weapon02)

    player03.pick_weapon(weapon01)

    player01.shoot(player03)
    player01.shoot(player03)

    player03.shoot(player01)


if __name__ == '__main__':
    main()
