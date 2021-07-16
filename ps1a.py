x = float(input('Enter your annual salary:'))
x /= 3
r = 0.04
r /= 12
r += 1
y = float(input('Enter the percent of your salary to save, as a decimal:'))
z = float(input('Enter the cost of your dream home:'))
v = float(0)
xy = x*y
cnt = 0
while v < z:
  cnt += 1
  v *= r 
  v += xy
print('Number of months:', cnt)
#x annual salary
#y savings percent
#z house cost
#r return
#v current savings
#cnt counter