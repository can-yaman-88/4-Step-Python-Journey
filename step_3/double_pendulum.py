import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint as od

L1 = 1.0
L2 = 1.0
m1 = 1.0
m2 = 1.0
g = 9.81

def derive(state, t):
    Q1, w1, Q2, w2 = state
    #Burada her bir değişken sırasıyla listeye ekleniyor.
    #Ters eşitlik olmasının bir güzel yanı da ayrı ayrı yazmaya gerek kalmıyor.
    delta = Q2 - Q1
    denominator = L1*(2*m1+m2-m2*np.cos(2*Q1-2*Q2))
    w1_dot = (-g*(2*m1 + m2)*np.sin(Q1) - m2*g*np.sin(Q1-2*Q2)
              -2*np.sin(Q1-Q2)*m2*(w2**2*L2+w1**2*L1*np.cos(Q1-Q2))) / denominator
    w2_dot = 2*np.sin(Q1-Q2)*(w1**2*L1*(m1+m2)+g*(m1+m2)*np.cos(Q1)+w2**2*L2*m2*np.cos(Q1-Q2)) / denominator
    return w1, w1_dot, w2, w2_dot
#Formülleri yapay zekadan aldım. Enerji korunumundan yola çıkarak elde edildiğini anlattı.

t = np.arange(0, 20, 0.05)
y0 = [np.pi/2, 0.0, np.pi/2, 0.0]
#İlk konumalarını yatay olacak şekilde ayarla dedi.
#Hm, burada açıyı ve hızı veriyor. 
#Yani bu sarkaçlar yatay konumdan ilk hızsız şekilde bırakılacalar.

y = od(derive, y0, t)
Q1 = y[:, 0]
#Burada 4 değişkenli y matrisinden ilk sütunu alıyorum ki bu da theta1'e denk geliyor.
Q2 = y[:, 2]
#Burada da 3. sütunu alıyorum.

x1 = L1 * np.sin(Q1)
y1 = -L1 * np.cos(Q1)
x2 = x1 + L2 * np.sin(Q2)
y2 = y1 - L2 * np.cos(Q2)
#Açıkçası burada neden böyle bir şey yaptığımızı anlayamadım. 
#Şimdi anladım.
#İkinci sarkaç ilk sarkacın ucuna bağlı.
#Bu yüzden de ikinci sarkacın bileşenlerini ilk sarkacın ucunun bileşenleriyle toplamam gerek.

plt.plot(x2, y2)
plt.title("Double Pendulum")
plt.xlabel("x position")
plt.ylabel("y position")
plt.show()
plt.savefig("double_pendulum")