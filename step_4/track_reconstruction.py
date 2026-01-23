import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as cf

p = 100
q = 1
B = 1
r = p / q * B
theta_random = np.linspace(0, 360, 360)
theta = np.deg2rad(theta_random)
x_true = r * np.cos(theta)
y_true = r * np.sin(theta)
indices = np.random.choice(np.arange(len(x_true)), size=15, replace=False)
x = x_true[indices]
y = y_true[indices]
#Burada direkt ekleme yöntemimin yanlış olduğunu fark ettim çünkü rastgele seçtiği x ve y değerleri farklı anlara ait olabilir.
#Bu yüzden sıralarını aldım ve ona göre işlem yaptım.
x_meas = x + np.random.normal(0, 0.1, len(x))
y_meas = y + np.random.normal(0, 0.1, len(y))
#Burada kafamda oturtamadığım şey daireyi nasıl çizdireceğim.
#Çemberim merkezde olduğu için denklem x^2+y^2=r^2 gibi bir şey olacak.
def circle(data, x_c, y_c, r):
    x, y = data
    return np.sqrt((x-x_c)**2 + (y-y_c)**2) - r
#Artık ne yapacağımı bilemediğim zaman kodu yapay zekayaattım ve o da şunları söyledi:
#cf'e y değerini sıfır verdiğin için verilen değerlere bakarak fonksiyonu sıfıra yakınlaştırmaya çalışıyor.
#r değerini değiştiriyor fakat bu fonksiyonda yer almadığı için değer değişmiyor bu yüzden de hata veriyor.
#Ben de farkların sıfıra gitmesi gerektiğini düşündüm ve sorun çözüldü.

#Galiba r değerini çekerken hata yapıyorum.
popt, pcov = cf(circle, [x_meas, y_meas], np.zeros(len(x_meas)), 
                p0=[0, 0, 100])
#Şimdi bu fonksiyon x_meas ve y_meas değerlerini ayrı ayrı fonksiyona veriyor.
#Çember fonksiyonu da bu değerlerden bir yarıçap hesaplıyor.
#Bu yarıçapı geri veriyor. 
#Fakat burada y değeri ne olmalı?
#Tanımda y = f(xdata, parameters) gibi bir şey gördüm. Bu nedenle bunun r değerleri olması gerektiğini düşünüyorum.
#Bu değerleri eklemesi için de boş bir liste eklemem gerekli galiba.

x_fit, y_fit, r_fit = popt
p_fit = q * (B * r_fit)

print(p_fit)
