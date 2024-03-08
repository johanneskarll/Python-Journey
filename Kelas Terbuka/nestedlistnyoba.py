N = int(input())
nilai = []
nama = []
nilaiurut = []
listorangterendah = []
for i in range (N):
    name = input()
    grade = input()
    nama.append(name)
    nilai.append(grade)
nilaiurut = nilai.copy()
nilaiurut.sort()

nilaiterendah = nilaiurut.pop()
for i in range(N):
    if nilaiterendah == nilai[i]:
        nilaiurut.pop()
nilaiterendahkedua = nilaiurut.pop()

for i in range(N):
    if nilaiterendahkedua == nilai[i]:
        listorangterendah.append(i)
for i in listorangterendah:
    print(nama[i])
    