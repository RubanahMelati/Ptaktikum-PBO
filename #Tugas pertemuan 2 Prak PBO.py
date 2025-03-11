#Tugas 2
import random

class Robot:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def attack_enemy(self, enemy):
        damage = self.attack - enemy.defense
        if damage < 0:
            damage = 0
        enemy.hp -= damage
        print(f"{self.name} menyerang {enemy.name} dan menyebabkan {damage} damage!")
        print(f"{enemy.name} memiliki {enemy.hp} HP tersisa.\n")

    def regen_health(self):
        heal_amount = random.randint(5, 15)
        self.hp += heal_amount
        print(f"{self.name} memulihkan {heal_amount} HP. HP sekarang: {self.hp}\n")

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name} [{self.hp}|{self.attack}]"


class Game:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2
        self.round = 1

    def start(self):
        print("Permainan dimulai!\n")
        while self.robot1.is_alive() and self.robot2.is_alive():
            self.print_round_info()
            self.player_turn(self.robot1, self.robot2)
            if not self.robot2.is_alive():
                break
            self.player_turn(self.robot2, self.robot1)
            self.round += 1

        self.declare_winner()

    def print_round_info(self):
        print(f"Round-{self.round} ==========================================================")
        print(self.robot1)
        print(self.robot2)
        print()

    def player_turn(self, attacker, defender):
        print(f"{attacker.name}, pilih aksi:")
        print("1. Attack     2. Regen Health     3. Giveup")
        choice = input("Pilihan: ")

        if choice == "1":
            attacker.attack_enemy(defender)
        elif choice == "2":
            attacker.regen_health()
        elif choice == "3":
            print(f"{attacker.name} menyerah! {defender.name} menang!\n")
            defender.hp = 0
        else:
            print("Pilihan tidak valid. Melewatkan giliran.\n")

    def declare_winner(self):
        if self.robot1.is_alive():
            print(f"{self.robot1.name} menang!")
        else:
            print(f"{self.robot2.name} menang!")


# Membuat dua robot
robot1 = Robot("Atreus", 500, 10, 2)
robot2 = Robot("Daedalus", 750, 8, 3)

# Memulai permainan
game = Game(robot1, robot2)
game.start()