con = input('Is Leverage Ratio growing? say it yes or no')
con2 = input('Is Price trend low? say it yes or no')

if ((con == 'yes') and (con2 == 'yes')):
  sum.append(1)
elif ((con == 'yes') and (con2 == 'no')):
  sum.append(-1)
elif ((con == 'no') and (con2 == 'yes')):
  print('')
elif ((con == 'no') and (con2 == 'no')):
  print('')
else:
  print('say it yes or no')
