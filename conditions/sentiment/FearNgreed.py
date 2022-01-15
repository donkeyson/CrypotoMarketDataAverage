//알터네이티브

con = int(input('input value of Fear & Greed Index'))

if (con >= 80):
  sum -= 3
  print('strong sell signal in Fear and Greed Index')
elif (80 > con >= 60):
  sum -= 2
elif (60 > con >= 40):
  sum -= 1
elif (40 > con >= 30):
  print('')
elif (30 > con >= 20):
  sum += 1
elif (20 > con)
  sum += 2
  print('strong buy signal on Fear and Greed Index')
