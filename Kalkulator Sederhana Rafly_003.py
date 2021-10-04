# Muhammad Rafly Arjasubrata 1301213488
"""
Kalkulator sederhana ini saya buat untuk memenuhi tugas webinar beberapa minggu lalu
(belum memakai fungsi)
"""

# Soal No.3
"""
Buatlah kalkulator sederhana dengan 2 input dan operasi pertambahan, pengurangan,
perkalian, dan pembagian
"""

"""
Contoh Testcase yang benar

Masukkan angka ke - 1 : 10
Masukkan operasi hitung : *
Masukkan angka ke - 2 : 5
Hasil : 50
"""

print ("Pilih Operasi")
print ("1. Tambah = + ")
print ("2. Kurang = - ")
print ("3. Kali = * ")
print ("4. Bagi = / ")

inputX = int(input("Masukkan angka ke - 1 : "))
operasi = (input("Masukkan Operasi Hitung : "))
inputY = int(input("Masukkan angka ke - 2 : "))

if operasi == "+" :
  result = inputX + inputY
elif operasi == "-" :
  result = inputX - inputY
elif operasi == "*" :
  result = inputX * inputY
elif operasi == "/" :
  result = inputX / inputY

print (f"Hasil : {result}")