import numpy as np  
import matplotlib.pyplot as plt  
  
# 定义要求解的微分方程  
def f(t, y):  
    # 这里以 dy/dt = y 为例  
    return y  
  
# 四阶龙格-库塔法  
def runge_kutta_4(f, t0, y0, h, n):  
    t = np.linspace(t0, t0 + n * h, n + 1)  
    y = np.zeros_like(t)  
    y[0] = y0  
      
    for i in range(n):  
        k1 = h * f(t[i], y[i])  
        k2 = h * f(t[i] + h / 2, y[i] + k1 / 2)  
        k3 = h * f(t[i] + h / 2, y[i] + k2 / 2)  
        k4 = h * f(t[i] + h, y[i] + k3)  
          
        y[i + 1] = y[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6  
      
    return t, y  
  
# 参数设置  
t0 = 0  
y0 = 1  
h = 0.1  # 步长  
n = 100  # 步数  
  
# 求解并绘图  
t, y = runge_kutta_4(f, t0, y0, h, n)  
plt.plot(t, y, label='y(t)')  
plt.xlabel('t')  
plt.ylabel('y')  
plt.legend()  
plt.grid(True)  
plt.show()