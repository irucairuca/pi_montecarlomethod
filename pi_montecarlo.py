#モンテカルロ法による円周率の近似
import time
import random
import matplotlib.pyplot as plt

n = int(input("何桁レベルの精度で計算しますか？"))
start = time.time()
i=10**n# 乱数で用いたランダムな点の生成数
x=[]
y=[]
c=0

for t in range(i):
  x_f = random.uniform(0,1)
  y_f = random.uniform(0,1)
  if (x_f**2+y_f**2<1):
    x.append(x_f)
    y.append(y_f)
    c=c+1

goal = time.time()
time= goal-start
print("計算処理時間"+str(time)+"[s]")
print(4*c/i)

plt.scatter(x,y)