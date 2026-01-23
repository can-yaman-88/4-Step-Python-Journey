import sympy as sp
sp.init_printing(use_unicode=True)

m, g, l, t = sp.symbols('m g l t')
#Sabitlerin sembollerini tanımlıyorum.
theta = sp.Function('theta')(t)
#Theta'yı zamanın bir fonksiyonu olarak tanımlıyorum.
theta_dot = theta.diff(t)
#Theta'nın zamana göre türevini belirliyorum.

v = l * theta_dot

T = 0.5 * m * v**2
V = m * g * l * (1-sp.cos(theta))

L = T - V

L_Q  = L.diff(theta)
L_Qdot = L.diff(theta_dot)
d_dt = L_Qdot.diff(t)

eq = sp.Eq(d_dt - L_Q, 0)
eq1 = sp.simplify(eq)
eq2 = sp.Eq(d_dt / (m*l**2), L_Q / (m*l**2))
solution = sp.solve(eq, theta.diff(t, t))
#Theta'nın ikinci için çözüyor.

#sp.pprint(eq)
#sp.pprint(eq1)
#sp.pprint(eq2)
sp.pprint(solution[0])