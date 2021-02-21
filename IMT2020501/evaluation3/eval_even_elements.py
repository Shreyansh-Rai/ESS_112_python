#!/usr/bin/python3

import sys
import subprocess
import random
from evaluate import *

@evaluate
def eval_1():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q9
  from mycode import even
  l = list(range(10))
  random.shuffle(l)
  o = Q9.even_elements(l)
  e = even.even_elements(l)
  if(equals(o, e)):
    return (1, fname)
  else:
    return (0, fname + ": wrong answer")

@evaluate
def eval_2():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q9
  from mycode import even
  l = [2, 4, 600]
  random.shuffle(l)
  o = Q9.even_elements(l)
  e = even.even_elements(l)
  if(equals(o, e)):
    return (1, fname)
  else:
    return (0, fname + ": wrong answer")

@evaluate
def eval_3():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q9
  from mycode import even
  l = [3, 5, 601]
  random.shuffle(l)
  o = Q9.even_elements(l)
  e = even.even_elements(l)
  if(equals(o, e)):
    return (1, fname)
  else:
    return (0, fname + ": wrong answer")


eval_tests = testsuite(
  tests = [
    (eval_1, 1),
    (eval_2, 1),
    (eval_3, 1),
  ])

if __name__ == "__main__":
  print(eval_tests())
