from sys import stdout
from math import sqrt, log
def is_pm(n):
     if p ==2:
         return True
      else:
           m_p = (1 << p) - 1
           s = 4
           for i in range(3, p + 1):
                s = ((s ** 2)-2) % m_p
            return( s==0 )
print(is_pm(37))
print(37)
