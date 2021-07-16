x = float(input('Enter your annual salary:'))
y = float(input('Enter the percent of your salary to save, as a decimal:'))
z = float(input('Enter the cost of your dream home:'))
v = float(0)
x /= 3
r = 0.04
r /= 12
r += 1
inc = float(input('Enter the percentage of your semi anual raise, as a decimal:'))
xy = float(x*y)
cnt = 0
inc += 1
while v < z:
  cnt += 1
  v *= r 
  v += xy
  if cnt % 6 == 0:
    x *= inc
    xy = float(x*y)
print('Number of months:', cnt)
#x annual salary
#y savings percent
#z house cost
#r return
#v current savings
#cnt counter
#inc increment