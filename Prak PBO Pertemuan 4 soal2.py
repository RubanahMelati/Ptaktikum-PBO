class TodoList:
    def __init__(self):
        self.daftar_tugas = []

    def tambah_tugas(self, tugas):
        if not tugas.strip():
            raise ValueError("Tugas tidak boleh kosong!")
        self.daftar_tugas.append(tugas)
        print("Tugas berhasil ditambahkan!")

    def hapus_tugas(self, nomor):
        if not isinstance(nomor, int) or nomor < 1 or nomor > len(self.daftar_tugas):
            raise IndexError(f"Error: Tugas dengan nomor {nomor} tidak ditemukan.")
        del self.daftar_tugas[nomor - 1]
        print("Tugas berhasil dihapus!")

    def tampilkan_tugas(self):
        if not self.daftar_tugas:
            print("Daftar tugas kosong.")
        else:
            print("Daftar Tugas:")
            for i, tugas in enumerate(self.daftar_tugas, 1):
                print(f"{i}. {tugas}")

def main():
    todo = TodoList()
    while True:
        print("\nPilih aksi:")
        print("1. Tambah tugas")
        print("2. Hapus tugas")
        print("3. Tampilkan daftar tugas")
        print("4. Keluar")
        
        try:
            pilihan = int(input("Masukkan pilihan (1/2/3/4): "))
            if pilihan == 1:
                tugas = input("Masukkan tugas yang ingin ditambahkan: ")
                todo.tambah_tugas(tugas)
            elif pilihan == 2:
                nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))
                todo.hapus_tugas(nomor)
            elif pilihan == 3:
                todo.tampilkan_tugas()
            elif pilihan == 4:
                print("Keluar dari program.")
                break
            else:
                print("Pilihan tidak valid. Masukkan angka 1-4.")
        except ValueError as e:
            if "tugas" in str(e).lower():
                print(e)
            else:
                print("Input tidak valid. Harap masukkan angka.")
        except IndexError as e:
            print(e)

# Jalankan program
main()