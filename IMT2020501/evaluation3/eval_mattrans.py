#!/usr/bin/python3

import sys
import subprocess
import random
from evaluate import *

@evaluate
def eval_1():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q11
  from mycode import mattrans
  m = [[12, 14],[16, 18],[20, 22]]
  o = Q11.mattrans(m)
  e = mattrans.mattrans(m)
  if(equals(o, e)):
    return (1, fname)
  else:
    return (0, fname + ": wrong answer")

@evaluate
def eval_2():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q11
  from mycode import mattrans
  m = [[12, 14],[16, 18],[20, 22]]
  m = mattrans.mattrans(m)
  o = Q11.mattrans(m)
  e = mattrans.mattrans(m)
  if(equals(o, e)):
    return (1, fname)
  else:
    return (0, fname + ": wrong answer")


eval_tests = testsuite(
  tests = [
    (eval_1, 1),
    (eval_1, 1),
  ])

if __name__ == "__main__":
  print(eval_tests())
