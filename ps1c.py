x = float(input('Enter your annual salary:'))
x /= 3
t = x
r = 0.04
r /= 12
r += 1
temp = 0
y = float (0.5)
xy = x*y
inc = float (1.07)
low = float (0)
high = float (1)
z = 1000000
cnt = 0



while cnt != z:
  temp += 1
  v = float(0)
  x = t
  xy = x*y
  for i in range(0, 37):
    v *= r 
    v += xy
    if i % 6 == 0:
      x *= inc
      xy = float(x*y)
  #print(y,' ',low,' ',high,' ',v)
  cnt = v
  if z+100 > v and z < v:
    cnt = z
  elif z-100 < v and z > v:
    cnt = z
  elif v > z:
   high = y
   y = high + low
   y /= 2
  elif z > v:
   low  = y
   y = high + low
   y /= 2
  if y == 1:
    cnt = z
if y !=1:
  print ('Best savings rate:', y)
  print('Steps in bisection search:', temp)
else:
  print('It is not possible to obtain the down payment in three years')