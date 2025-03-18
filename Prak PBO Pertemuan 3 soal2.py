import random

class Father:
    def __init__(self, blood_type):
        self.blood_type = blood_type.upper()
        self.alleles = self._get_alleles()

    def _get_alleles(self):
        if self.blood_type == "A":
            return ["A", "O"]  # Misalnya heterozigot
        elif self.blood_type == "B":
            return ["B", "O"]
        elif self.blood_type == "AB":
            return ["A", "B"]
        elif self.blood_type == "O":
            return ["O", "O"]
        else:
            raise ValueError("Golongan darah tidak valid!")

class Mother:
    def __init__(self, blood_type):
        self.blood_type = blood_type.upper()
        self.alleles = self._get_alleles()

    def _get_alleles(self):
        if self.blood_type == "A":
            return ["A", "O"]
        elif self.blood_type == "B":
            return ["B", "O"]
        elif self.blood_type == "AB":
            return ["A", "B"]
        elif self.blood_type == "O":
            return ["O", "O"]
        else:
            raise ValueError("Golongan darah tidak valid!")

class Child(Father, Mother):
    def __init__(self, father, mother):
        self.father_allele = random.choice(father.alleles)  # 50% probabilitas
        self.mother_allele = random.choice(mother.alleles)  # 50% probabilitas
        self.blood_type = self._determine_blood_type()

    def _determine_blood_type(self):
        alleles = sorted([self.father_allele, self.mother_allele])
        if alleles == ["A", "A"] or alleles == ["A", "O"]:
            return "A"
        elif alleles == ["B", "B"] or alleles == ["B", "O"]:
            return "B"
        elif alleles == ["A", "B"]:
            return "AB"
        elif alleles == ["O", "O"]:
            return "O"
        return "Unknown"

    def __str__(self):
        return f"Golongan darah anak adalah: {self.blood_type}.\nAnak mewarisi alel {self.father_allele} dari ayah dan {self.mother_allele} dari ibu."

# Pengujian
father = Father(input("Masukkan golongan darah ayah (A/B/AB/O): "))
mother = Mother(input("Masukkan golongan darah ibu (A/B/AB/O): "))
child = Child(father, mother)

print(f"Golongan darah ayah: {father.blood_type}")
print(f"Golongan darah ibu: {mother.blood_type}")
print(child)