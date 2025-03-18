class kalkulator:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        return kalkulator(self.value + other.value)
    
    def __sub__(self, other):
        return kalkulator(self.value - other.value)
    
    def __mul__(self, other):
        return kalkulator(self.value * other.value)
    
    def __truediv__(self, other):
        if other.value == 0:
            raise ValueError("Pembagian dengan nol tidak diperbolehkan!")
        return kalkulator(self.value / other.value)
    
    def __pow__(self, other):
        return kalkulator(self.value ** other.value)
    
    def log(self):
        import math
        if self.value <= 0:
            raise ValueError("Logaritma hanya untuk bilangan positif!")
        return kalkulator(math.log(self.value))
    
    def __str__(self):
        return str(self.value)

# Fungsi untuk meminta input pengguna dan menangani error
def angka(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Input tidak valid! Silakan masukkan angka.")

# Fungsi untuk menampilkan menu dan memilih operasi
def menu():
    print("\nPilih operasi yang ingin dilakukan:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Eksponen")
    print("6. Logaritma")
    print("7. Keluar")

# Program utama
while True:
    # Pengambilan input dari pengguna
    num1_value = angka("Masukkan angka pertama: ")
    num2_value = angka("Masukkan angka kedua: ")

    num1 = kalkulator(num1_value)
    num2 = kalkulator(num2_value)

    # Menampilkan menu operasi kalkulator
    menu()

    try:
        # Meminta input pilihan operasi
        choice = int(input("Masukkan pilihan (1-7): "))

        if choice == 1:
            print(f"Penjumlahan: {num1 + num2}")      # Penjumlahan
        elif choice == 2:
            print(f"Pengurangan: {num1 - num2}")      # Pengurangan
        elif choice == 3:
            print(f"Perkalian: {num1 * num2}")        # Perkalian
        elif choice == 4:
            print(f"Pembagian: {num1 / num2}")        # Pembagian
        elif choice == 5:
            print(f"Eksponen: {num1 ** num2}")        # Eksponen
        elif choice == 6:
            print(f"Logaritma dari {num1}: {num1.log()}")  # Logaritma dari angka pertama
        elif choice == 7:
            print("Terima kasih! Program dihentikan.")
            break  # Keluar dari loop utama
        else:
            print("Pilihan tidak valid! Silakan pilih angka antara 1-7.")
    except ValueError as e:
        print(e)