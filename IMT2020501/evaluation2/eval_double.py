#!/usr/bin/python

import sys
import subprocess
import random
from evaluate import *

@evaluate
def eval_1():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  marks = 1
  from code import Q8
  from mycode import double
  l = list(range(10))
  random.shuffle(l)
  o = Q8.double(l)
  e = double.double(l)
  if(equals(o, e)):
    return (1, fname)
  else:
    return (0, fname + ": wrong answer")

eval_tests = testsuite(
  tests = [
    (eval_1, 1),
  ])

if __name__ == "__main__":
  print(eval_tests())
