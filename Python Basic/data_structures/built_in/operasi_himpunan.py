set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
set1.add(0)

#union : gabungan semua elemen unik dari kedua set
print(set1.union(set2), '-----', set1 | set2)

#intersection: irisan, hanya elemen yang sama di kedua set
print(set1.intersection(set2), '-----', set1 & set2)

#difference: elemen yang ada di set1 tetapi tidak ada di set2
print(set1.difference(set2), '-----', set1 - set2)

#symmetric_difference: elemen yang ada di set1 atau set2 tetapi tidak ada di keduanya
print(set1.symmetric_difference(set2), '-----', set1 ^ set2)

set1.clear()
print(set1)
