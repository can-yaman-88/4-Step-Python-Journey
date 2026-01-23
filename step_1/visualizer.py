import matplotlib.pyplot as plt
Ax, Ay = 0, 0
Bx, By = 2, 0
Cx, Cy = 1, 1.732

plt.figure(figsize=(8, 8))

# AC Çubuğu (Basma - Mavi)
plt.plot([Ax, Cx], [Ay, Cy], color='blue', linewidth=3, label='Basma (577N)')
# BC Çubuğu (Basma - Mavi)
plt.plot([Bx, Cx], [By, Cy], color='blue', linewidth=3, label= 'Basma (577N)')
# AB Çubuğu (Çekme - Kırmızı)
plt.plot([Ax, Bx], [Ay, By], color='red', linewidth=3, label = 'Çekme (289N)')

plt.text((Ax+Cx)/2, (Ay+Cy)/2, "577 N", color='blue', fontsize=12, ha='center')
plt.text((Bx+Cx)/2, (By+Cy)/2, "577 N", color='blue', fontsize=12, ha='center')
plt.text((Ax+Bx)/2, (Ay+By)/2, "289 n", color='blue', fontsize=12, ha='center')

plt.title("Üçgen Kafes Sistemi Analizi")
plt.legend()
plt.grid(True)
plt.xlim(-1, 3)
plt.ylim(-1, 3)

plt.show()

plt.savefig("bridge_analiz.png")