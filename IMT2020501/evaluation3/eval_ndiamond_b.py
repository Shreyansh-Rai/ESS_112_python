#!/usr/bin/python3

import sys
import subprocess
from evaluate import *

@evaluate
def eval_1():
  fname = __name__ + "." + sys._getframe().f_code.co_name
  subprocess.call(["cp", "drivers/ndiamond_b_driver.py", "code/"])

  o = subprocess.check_output(["python3", "code/ndiamond_b_driver.py"])
  e = subprocess.check_output(["python3", "mycode/ndiamond_b_driver.py"])
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
