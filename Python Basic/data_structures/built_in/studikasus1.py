from collections import defaultdict

data = [("Akmal", 85), ("Budi", 90), ("Akmal", 78), ("Citra", 88)] #Kelompokkan nilai berdasarkan nama, Hitung rata-rata tiap mahasiswa

# kelompokan nilai berdasarkan nama
nilai_per_mahasiswa = defaultdict(list)
for nama, nilai in data:
    nilai_per_mahasiswa[nama].append(nilai)
    
# hitung rata-rata tiap mahasiswa
rata_rata = {nama: sum(nilai) / len(nilai) for nama, nilai in nilai_per_mahasiswa.items()}

print(dict(nilai_per_mahasiswa))
print(rata_rata)
