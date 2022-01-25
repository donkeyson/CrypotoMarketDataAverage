#크립토 퀀트

con = float(input('input value of Net Unrealized Profit/Loss'))

if (con >= 0.5):
  sum.append(-2)
elif (0.5> con >= 0.4):
  sum.append(-1)
elif (0.4 > con >= 0.3):
  print('')
elif (0.3 > con >= 0.1):
  sum.append(1)
elif (0.1 > con):
  sum.append(2)
  print('strong buy signal')

con2 = input('다이버전스가 발생했는가? yes or no로 대답')
if con2 == yes:
  sum.append(-3)
  print('강력한 매도 신호')
else:
  print('')
