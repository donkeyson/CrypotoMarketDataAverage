//크립토 퀀트

con = float(input('input value of Korea Premium Index'))

if (con >= 9):
  sum.append(-3)
elif (9 > con >= 6):
  sum.append(-2)
elif (6 > con >= 4):
  sum.append(-1)
elif (4 > con >= 2):
  print('')
elif (2 > con >= 0):
  sum.append(1)
elif (0 > con):
  sum.append(3)
  print('strong buy signal on Kimchi Premium')
