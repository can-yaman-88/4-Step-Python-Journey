import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as cf

df = pd.read_csv("physic_lab_data.csv")
df = df[(df["Time"] >= 0) & (df["Time"] < 10)]
#Alternatif olarak bir diğer yöntem de aşağıdakiymiş.
#df.drop
#df.insert(4, column="Time_Square", value=df["Time"]**2)
#Bunun da yeni bir yolunu öğrendim:
df["Time_Square"] = df["Time"]**2

def ff_model(t_square, g):
    h = 0.5 * g * t_square
    return h

popt, pcov = cf(ff_model, df["Time_Square"], df["Height"])
g_c = popt
error = np.absolute((g_c-9.81)/9.81*100)
plt.scatter(df["Time_Square"], df["Height"],
            color='blue')
plt.title(f"Calculated g: {g_c[0]:.2} m/s^2 (Hata: %{error[0]})")
#Burada öğrendim ki .2 kısmı ondalık kısımda 2 tane basamak olmasını sağlıyor.

#plt.plot(df["Time_Square"], g_c[0])
#İlk önce bunu denedim fakat df kısmı 9 elemanlı, g kısmı tek eleman olduğundan hata verdi.
#Hatayla daha önce karşılaşmadığım için yapay zekaya sordum ve o da fonksiyonun içine koyup 9 elemana çıkarmamı söyledi.
y_fit = ff_model(df["Time_Square"], g_c[0])
#Burada aslında kodun yaptığı şey t^2 değerlerini fonksiyon içine koyuyor.
#Ve bu değerler bir vektör, liste, olduğundan sonuç da bir liste oluyor.
plt.plot(df["Time_Square"], y_fit,
         color='red')
plt.xlabel("Time^2")
plt.ylabel("Height(m)")
plt.savefig("report")