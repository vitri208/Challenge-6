print('*Kondisi akan benar jika angka yang dimasukkan ganjil dan diatas 20*')
Bilangan = int(input('Masukkan angka \t:'))
while Bilangan <= 20 :
  Bilangan = int(input('Masukkan angka \t:'))
if Bilangan > 20 :
  while Bilangan % 2 == 0 :
    Bilangan = int(input('Masukkan angka \t:'))
  if Bilangan % 2 == 1 : 
    print('Angka benar')