#!/usr/bin/python3

import sys
import subprocess
import random
from evaluate import *

@evaluate
def eval_1():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  marks = 1
  from code import Q12
  from mycode import matmul
  m1 = [[12, 14],[16, 18]]
  m2 = [[12, 14],[16, 18]]
  sub = lambda: Q12.matmul(m1, m2)
  ref = lambda: matmul.matmul(m1, m2)
  return eval_matfun(fname, sub, ref)

@evaluate
def eval_2():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  marks = 1
  from code import Q12
  from mycode import matmul
  m1 = [[12, 14],[16, 18], [20, 21]]
  m2 = [[12, 14],[16, 18]]
  sub = lambda: Q12.matmul(m1, m2)
  ref = lambda: matmul.matmul(m1, m2)
  return eval_matfun(fname, sub, ref)

@evaluate
def eval_3():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  marks = 1
  from code import Q12
  from mycode import matmul
  m1 = [[12, 14, 20],[16, 18, 34]]
  m2 = [[12, 14],[16, 18], [100, 100]]
  sub = lambda: Q12.matmul(m1, m2)
  ref = lambda: matmul.matmul(m1, m2)
  return eval_matfun(fname, sub, ref)

@evaluate
def eval_4():
  fname = __name__ + "." + sys._getframe().f_code.co_name

  marks = 1
  from code import Q12
  from mycode import matmul
  m1 = [[12, 14, 20],[16, 18, 34]]
  m2 = [[12, 14],[16, 18]]
  sub = lambda: Q12.matmul(m1, m2)
  ref = lambda: matmul.matmul(m1, m2)
  return eval_matfun(fname, sub, ref)

eval_tests = testsuite(
  tests = [
    (eval_1, 1),
    (eval_2, 1),
    (eval_3, 1),
    (eval_4, 1),
  ])

if __name__ == "__main__":
  print(eval_tests())
