import math

dp = 3
num = math.pi


def print_round(num, dp):
  '''round a number to a given number of decimal places 
    using the simple method of rounding half up, 
    prints the closest number with a given number of decimal places'''
  st = str(num)  #
  index = st.find('.')
  if index == -1:
    print(st)
  else:
    int_part = st[0:index]
    if dp > 0:
      fract_part = st[index + 1:]
      head = fract_part[0:dp]
      val = int(head)
      digit = fract_part[dp:dp + 1]
      if digit >= '5':
        # need to round up in simple method
        val += 1
        print(int_part, '.', val, sep='')
    else:
      print(int_part, '.', sep='')


for dp in range(0, 10):
  print_round(num, dp)
