import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("run_data.csv")
#print(df.head(10))

sv = df.rolling(window=20).mean()

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
#ilk sayı satır sayısını ikinci sayı da sütun sayısını ifade ediyor.
#sharex=True demek tüm grafikler aynı x eksenini kullanıyor.

ax1.fill_between(sv["Zaman_sn"], sv["Yukseklik_m"], 0, color='red', alpha=.2)
#fill_between diyerek yükseklik grafiği ile x ekseni arasındaki alanı boyuyor.
ax1.set(ylabel="Elevation(m)")
ax1.set_ylim(95, 155)
#Burada maksimum ve minimum değerler belirliyorum ki grafik daha okunabilir olsun.

ax2.plot(sv["Zaman_sn"], sv["Hiz_ms"], color='green')
ax2.set(xlabel="Time(s)",
        ylabel="Velocity(m/s)")

ax_right = ax2.twinx()
ax_right.plot(sv["Zaman_sn"], sv["Nabiz_bpm"], color='blue')
ax_right.set(xlabel="Time(s)",
             ylabel="Heart Rate(bpm)")

plt.show()
plt.savefig("run.png")
maxhr = sv["Nabiz_bpm"].idxmax()
#Maksimum nabzın index numarasını buluyorum ki oradaki verilere ulaşabileyim.
print("Max heart rate is shown at: ", sv.loc[maxhr, ["Zaman_sn"]],
      "\nOther values at highest heart rate: ", sv.loc[maxhr, ["Hiz_ms", "Yukseklik_m"]])