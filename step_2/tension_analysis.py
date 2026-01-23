#Yapay zeka burada ipin, telin veya çubukların bir sistemde ayakta kalıp kalmayacaklarını söyleyen bir kod yazmamı istedi.
#Burada bazı kabuller ve hazır bilgiler kullanacağız.

import numpy as np
import math
force = 577.35
#Bu değer üç çubuklu bir sistemde daha önceki kodda bulduğum bir değer.
radius = 0.002
#Bu değer yapy zekanın bana verdiği bir değer, çubukların yarıçapı.
limit = 355
#Bu değer de yapay zekanın bana verdiği kullandığım çubuğun en fazla 355 megapascal'a dayanacağını söylüyor.
#İlk önce alan hesaplamam gerek.
area = math.pi * (radius**2)
#Gerilimi hesaplamam gerek, o da kuvvet bölü alan.
tension = force / area
tension_mp = tension / 1000000

if tension_mp <= 350:
    print("System will work.")
    print(tension_mp)
else:
    print("Force is too much.")

#bir de katsayı bulmamı istedi.
coefficient = limit / tension_mp
print(coefficient)