# Nama Kelompok :
# 5200411002 - Elga Yuan Saputra
# 5200411059 - Dedy gusrianto
# 5200411064 - Abid Taufiqur Rohman
# 5200411065 - Alvian Andhi gunawan


print ("===============================")
print ("   SIMULASI MENEJEMEN MEMORI   ")
print ("-------------------------------")
#inputan
totalRam = int(input("Masukkan Kapasitas RAM = "))
terpakai = int(input("Program Terpakai = "))

#kapasitas Sistem Oprasi
os = 2

#rumus perhitungan
takter = totalRam - os - terpakai

#hasil akhir
print ("-------------------------------")
print ("Total RAM              = %d GB"% totalRam)
print ("Sistem Optasi (Os)     = %d GB"% os)
print ("Program Terpakai       = %d GB"% terpakai)
print ("Program Tidak Terpakai = %d GB"% takter)


