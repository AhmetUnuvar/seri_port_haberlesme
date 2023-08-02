from ekran import Ekransinifi
import time

# Ekran.py nin çalıştığı kısım.


if __name__ == "__main__":
    while True:
        e = Ekransinifi()
        e.hava_calistir()
        time.sleep(5)
        e.saat_calistir()
        time.sleep(5)
        e.close()


