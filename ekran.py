import serial
import datetime
from hava import Weather
class Ekransinifi:

    def __init__(self):

        self.ser = serial.Serial(port="COM4", baudrate=9600, timeout=0.1)


    def saat_calistir(self):

        x = datetime.datetime.now()
        h = x.hour
        m = x.minute
        x1 = int(h/10)
        h1 = str(x1)
        x2 = (h % 10)
        bh = str(x2)
        x3 = int(m/10)
        m1 = str(x3)
        x4 = (m % 10)
        mh = str(x4)
        saat = bytes.fromhex('2A 32 31 3'+h1+' 3'+bh+' 3'+m1+' 3'+mh+'31 31 38 35 37 39 34 39 37 38 33 33 0D')


        self.ser.write(saat)

# ------------------ Hava Sıcaklığı -------------------------------

    def hava_calistir(self):

        w = Weather()

        if w.temp_celsius >0 :
            a = bytes.fromhex(
                '2A 33 31 3' + str(w.c2) + ' 3' + str(w.c4) + ' 3B 3C 31 31 35 37 39 34 39 37 38 33 33 31 0D')
        elif w.temp_celsius <0:
            k =str(w.c2)

            k2=k[1:2]
            k3=str(w.c4)
            a = bytes.fromhex('2A 33 31 3D 3'+k2+' 3'+k3+' 3B 31 31 35 32 34 37 33 34 31 37 32 39 0D')

        self.ser.write(a)

    def close(self):

        self.ser.close()


