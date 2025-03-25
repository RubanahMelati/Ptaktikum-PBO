from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nama, usia):
        if not nama or usia <= 0:
            raise ValueError("Nama tidak boleh kosong dan usia harus positif!")
        self.__nama = nama
        self.__usia = usia

    def get_nama(self):
        return self.__nama
    
    def set_nama(self, nama):
        if not nama:
            raise ValueError("Nama tidak boleh kosong!")
        self.__nama = nama

    def get_usia(self):
        return self.__usia
    
    def set_usia(self, usia):
        if usia <= 0:
            raise ValueError("Usia harus positif!")
        self.__usia = usia

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def aktivitas(self):
        pass

class Anjing(Animal):
    def make_sound(self):
        return "Woof Woof!"

    def aktivitas(self):
        return f"{self.get_nama()} sedang berlari-lari."

class Kucing(Animal):
    def make_sound(self):
        return "Meow Meow!"

    def aktivitas(self):
        return f"{self.get_nama()} sedang tidur."

class Zoo:
    def __init__(self):
        self.hewan = []

    def tambah_hewan(self, hewan):
        self.hewan.append(hewan)
        print(f"{hewan.get_nama()} berhasil ditambahkan ke kebun binatang.")

    def tampilkan_semua(self):
        if not self.hewan:
            print("Kebun binatang kosong.")
        else:
            print("\nDaftar Hewan di Kebun Binatang:")
            for hewan in self.hewan:
                print(f"- {hewan.get_nama()} ({hewan.__class__.__name__}), Usia: {hewan.get_usia()}")
                print(f"  Suara: {hewan.make_sound()}")
                print(f"  Aktivitas: {hewan.aktivitas()}")

def main():
    zoo = Zoo()
    while True:
        print("\n1. Tambah Hewan")
        print("2. Tampilkan Semua Hewan")
        print("3. Keluar")
        try:
            pilihan = int(input("Pilih aksi (1/2/3): "))
            if pilihan == 1:
                jenis = input("Masukkan jenis hewan (Anjing/Kucing): ").lower()
                nama = input("Masukkan nama hewan: ")
                usia = int(input("Masukkan usia hewan: "))
                
                if jenis == "anjing":
                    hewan = Anjing(nama, usia)
                elif jenis == "kucing":
                    hewan = Kucing(nama, usia)
                else:
                    raise ValueError("Jenis hewan tidak valid!")
                zoo.tambah_hewan(hewan)
            elif pilihan == 2:
                zoo.tampilkan_semua()
            elif pilihan == 3:
                print("Keluar dari program.")
                break
            else:
                print("Pilihan tidak valid!")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

main()