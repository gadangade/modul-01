#OPERATOR ARITMATIKA
var_a = 10
var_b = 7
var_c = input("masukan nilai variabel c: ")
var_d = input("masukan nilai variabel d: ")
var_e = input("masukan nilai variabel e: ")
#pengoperasian sederhana
Jum = var_a + var_b
Sub = var_a - var_b
Kali = var_a * var_b
Bagi = var_a / var_b
print("a = ", var_a)
print("b = ", var_b)
print(var_c, var_d, var_e)
print("----------------------------------------")
print(f"Hasil jumlah {var_a} dan {var_b}, adalah {Jum}")
### berikan print untuk Sub, Kali dan Bagi dengan cara yang sama
#Pangkat dan Akar
Pangkat = var_a ** var_b
Akar = var_a ** (1 / var_b)
### berikan print untuk Pangkat dan Akar dengan cara yang sama
#Penanganan Error 1
Jum2 = var_c + var_d
print("Jum2 = ", Jum2)
### apakah Jum2, memberikan hasil penjumlahan yang BENAR ?
### perbaiki dengan menambahkan fungsi int sebelum dijumlahkan
### menjadi :
var_c = int(var_c)
var_d = int(var_d)
Jum2 = (var_c + var_d)
print("Jum2 = ", Jum2)
### lalu print, bahas hal ini dalam laporan
#Penanganan Error 2
Kali3 = 3 * var_d
print("Kali3 = ", Kali3)
### apakah Kali3, memberikan hasil perkalian yang BENAR ?
### perbaiki seperti cara sebelumnya(Jum2), bahas dalam laporan
# Sisa Bagi (Modulus)
bilangan1 = 25
bilangan2 = 4
Modulus = bilangan1 % bilangan2
print("Operasi Sisa Bagi")
print("Sisa bagi dari bilangan ", bilangan1, " dan ", bilangan2,
" adalah ", Modulus)
print("----------------------------------------------")
# Pembagian Bulat
a = 12
b = 5
Hasil = a//b
print("Operasi Pembagian Bulat")
print(f"Pembagian bilangan bulat dari {a} dan {b} adalah {Hasil}")
print("--------------------------------------------------")