# Tugas 2
import random  # Mengimpor modul random untuk menghasilkan angka acak (digunakan untuk fitur regenerasi HP)

# Definisi kelas Robot untuk merepresentasikan robot dalam permainan
class Robot:
    # Fungsi inisialisasi (konstruktor) untuk mengatur atribut robot
    def __init__(self, name, hp, attack, defense):
        self.name = name  # Nama robot
        self.hp = hp  # Health Points (HP) atau nyawa robot
        self.attack = attack  # Nilai serangan robot
        self.defense = defense  # Nilai pertahanan robot

    # Fungsi untuk menyerang musuh
    def attack_enemy(self, enemy):
        # Menghitung damage: serangan robot dikurangi pertahanan musuh
        damage = self.attack - enemy.defense
        if damage < 0:  # Jika damage negatif, set damage menjadi 0
            damage = 0
        enemy.hp -= damage  # Mengurangi HP musuh berdasarkan damage
        # Menampilkan informasi serangan
        print(f"{self.name} menyerang {enemy.name} dan menyebabkan {damage} damage!")
        print(f"{enemy.name} memiliki {enemy.hp} HP tersisa.\n")

    # Fungsi untuk memulihkan HP robot
    def regen_health(self):
        # Menghasilkan jumlah pemulihan HP secara acak antara 5 hingga 15
        heal_amount = random.randint(5, 15)
        self.hp += heal_amount  # Menambahkan HP robot
        # Menampilkan informasi pemulihan HP
        print(f"{self.name} memulihkan {heal_amount} HP. HP sekarang: {self.hp}\n")

    # Fungsi untuk memeriksa apakah robot masih hidup (HP > 0)
    def is_alive(self):
        return self.hp > 0

    # Fungsi untuk menampilkan informasi robot dalam format string
    def __str__(self):
        return f"{self.name} [{self.hp}|{self.attack}]"


# Definisi kelas Game untuk mengatur logika permainan
class Game:
    # Fungsi inisialisasi untuk mengatur dua robot dan ronde awal
    def __init__(self, robot1, robot2):
        self.robot1 = robot1  # Robot pertama
        self.robot2 = robot2  # Robot kedua
        self.round = 1  # Ronde awal permainan

    # Fungsi utama untuk memulai permainan
    def start(self):
        print("Permainan dimulai!\n")
        # Loop permainan berjalan selama kedua robot masih hidup
        while self.robot1.is_alive() and self.robot2.is_alive():
            self.print_round_info()  # Menampilkan informasi ronde
            self.player_turn(self.robot1, self.robot2)  # Giliran robot pertama
            # Jika robot kedua sudah mati, keluar dari loop
            if not self.robot2.is_alive():
                break
            self.player_turn(self.robot2, self.robot1)  # Giliran robot kedua
            self.round += 1  # Menambah nomor ronde

        self.declare_winner()  # Menentukan dan menampilkan pemenang

    # Fungsi untuk menampilkan informasi ronde dan status kedua robot
    def print_round_info(self):
        print(f"Round-{self.round} ==========================================================")
        print(self.robot1)  # Menampilkan informasi robot pertama
        print(self.robot2)  # Menampilkan informasi robot kedua
        print()

    # Fungsi untuk mengatur giliran pemain (robot)
    def player_turn(self, attacker, defender):
        # Menampilkan opsi aksi yang bisa dipilih oleh pemain
        print(f"{attacker.name}, pilih aksi:")
        print("1. Attack     2. Regen Health     3. Giveup")
        choice = input("Pilihan: ")  # Meminta input dari pengguna

        # Logika untuk menangani pilihan pengguna
        if choice == "1":
            attacker.attack_enemy(defender)  # Robot menyerang musuh
        elif choice == "2":
            attacker.regen_health()  # Robot memulihkan HP
        elif choice == "3":
            # Robot menyerah, musuh dinyatakan menang
            print(f"{attacker.name} menyerah! {defender.name} menang!\n")
            defender.hp = 0  # Mengatur HP musuh menjadi 0 untuk mengakhiri permainan
        else:
            # Jika input tidak valid, giliran dilewati
            print("Pilihan tidak valid. Melewatkan giliran.\n")

    # Fungsi untuk menentukan dan menampilkan pemenang
    def declare_winner(self):
        if self.robot1.is_alive():
            print(f"{self.robot1.name} menang!")  # Robot pertama menang jika masih hidup
        else:
            print(f"{self.robot2.name} menang!")  # Robot kedua menang jika robot pertama mati


# Membuat dua objek robot dengan atribut nama, HP, attack, dan defense
robot1 = Robot("Atreus", 500, 10, 2)  # Robot pertama: Atreus
robot2 = Robot("Daedalus", 750, 8, 3)  # Robot kedua: Daedalus

# Membuat objek permainan dengan dua robot
game = Game(robot1, robot2)
# Memulai permainan
game.start()