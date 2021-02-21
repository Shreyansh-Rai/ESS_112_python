#!/usr/bin/python3

import sys
import subprocess
import random
from evaluate import *

@evaluate
def eval_1():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  from code import Q8
  from mycode import double
  l = list(range(10))
  random.shuffle(l)
  sub = lambda: Q8.double(l)
  ref = lambda: double.double(l)
  return eval_matfun(fname, sub, ref)

eval_tests = testsuite(
  tests = [
    (eval_1, 1),
  ])

if __name__ == "__main__":
  print(eval_tests())
