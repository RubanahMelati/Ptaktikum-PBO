import math

def hitung_akar_kuadrat():
    while True:
        try:
            angka = input("Masukkan angka: ")
            angka = float(angka)  # Konversi ke float
            if angka < 0:
                print("Input tidak valid. Harap masukkan angka positif.")
            elif angka == 0:
                raise ValueError("Error: Akar kuadrat dari nol tidak diperbolehkan.")
            else:
                hasil = math.sqrt(angka)
                print(f"Akar kuadrat dari {angka} adalah {hasil}")
                break
        except ValueError as e:
            if "nol" in str(e):
                print(e)
            else:
                print("Input tidak valid. Harap masukkan angka yang valid.")

# Jalankan program
hitung_akar_kuadrat()