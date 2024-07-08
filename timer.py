import time
import sys

def mengetik(text, speed=0.13):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)

nama = ["Yogi Ario Pratama", '2313020004', "Timer Sederhana"]
for i in nama:
    print(i)


timer = int(input("Masukkan waktu dalam detik: "))

for a in range (timer, 0, -1):
    detik = a % 60
    menit = int(a/60) % 60
    jam = int(a/3600) % 24
    print(f"{jam:02}:{menit:02}:{detik:02}")
    time.sleep(1)

print(" ")
mengetik("Waktu Habis")