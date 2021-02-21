#!/usr/bin/python3
import sys
# sys.path.append("/home/sujit/IIITB/projects/evaluate/evaluate/")

import evaluate

import eval_sop
import eval_mathop
import eval_matrices


eval_all = evaluate.evaluator(
  evals = [
    (eval_sop.eval_tests, 10),
    (eval_mathop.eval_tests, 8),
    (eval_matrices.eval_tests, 47),
  ])

if __name__ == "__main__":
  if(len(sys.argv) > 1):
    roll_number = sys.argv[1]
  else:
    roll_number = ""
  marks = eval_all()
  total = sum(marks)
  print(roll_number + " marks = " + str(marks) + " total = " + str(total))
