#!/usr/bin/python3

import sys
import subprocess
from evaluate import *

sys.path.append(".")
@evaluate
def eval_1():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  marks = 1
  from code import Q7
  from mycode import hello
  o = Q7.hello("SKC")
  e = hello.hello("SKC")
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
