# NAMA KELOMPOK :
# 5200411064 - Abid Taufiqur Rohman
# 5200411002 - Elga Yuan Saputra
# 5200411059 - Dedy gusrianto
# 5200411065 - Alvian Andhi gunawan

# ISTILAH VARIABLE DALAM CODE PROGRAM
# kapRam    = Kapasitas RAM
# disini kita menggunakan 3 inputan kapasitas program:
# proStu    = Kapasitas Program 1
# proDua    = Kapasitas Program 2
# proTga    = Kapasitas Program 3
# disini kita sudah menentukan kapasitas sistem oprasi jadi user tidak usah menginputkan
# os        = Kapasitas Sistem Oprasi
# totalPro  = Total kapasitas program
# sisaRam   = Kapasitas RAM tersisa

print ("===============================================")
print ("|      MANAJEMEN MEMORI MULTIPROGRAMMING      |")
print ("===============================================")

#inputan user

kapRam = int(input("Masukkan kapasitas RAM (dalam MBps)       : "))
proStu = int(input("Masukkan Kapasitas Program 1 (dalam MBps) : "))
proDua = int(input("Masukkan Kapasitas Program 2 (dalam MBps) : "))
proTga = int(input("Masukkan Kapasitas Program 3 (dalam MBps) : "))

#Kapasitas sistem oprasi
os = 2000

#Rumus Perhitungan
#kapasitas program total
totalPro = proStu+proDua+proTga
#kapasitas sisa RAM
sisaRam = kapRam-os-totalPro

#output program
print ("----------------------------------------------")
print ("Kapasitas RAM                   : %d MBps"%kapRam)
print ("Kapasitas Sistem Oprasi (OS)    : %d MBps"%os)
print ("Kapasitas Program 1             : %d MBps"%proStu)
print ("Kapasitas Program 2             : %d MBps"%proDua)
print ("Kapasitas Program 3             : %d MBps"%proTga)
print ("Total Kapasitas Program         : %d MBps"%totalPro)
print ("==============================================")
print ("Kapasitas RAM tersisa           : %d MBps"%sisaRam)
print ("==============================================")

