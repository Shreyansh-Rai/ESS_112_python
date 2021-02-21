import subprocess
import functools

mypython = "python3"

def equals(x, y):
  tx = type(x)
  ty = type(y)
  if((tx == int or tx == float) and (ty == int or ty == float)):
    return (abs(x - y) < 1.0)
  if(tx != ty):
    return False
  if(tx == list and ty == list):
    if(len(x) != len(y)):
      return False
    z = zip(x, y)
    tfs = [equals(a, b) for a, b in z]
    return functools.reduce(lambda a, b: a and b, tfs, True)
  elif(tx == tuple and ty == tuple):
    if(len(x) != len(y)):
      return False
    z = zip(x, y)
    for a, b in z:
      if(equals(a, b) == False):
        return False
    return True
  else:
    return x == y

def evaluate(f):
  def g():
    try:
      return f()
    except (
        KeyError,
        SyntaxError,
        NameError,
        AttributeError,
        TypeError,
        ImportError,
        IndexError,
        subprocess.CalledProcessError,
        UnboundLocalError,
        KeyboardInterrupt,
        ZeroDivisionError,
        ValueError) as e:
      return (0, f.__name__ + ": " + str(e))
  return g

def testsuite(tests):
  def eval_tests():
    result = [f() for (f, _) in tests]
    weights = [w for (_, w) in tests]
    test_results = [tr for (tr, _) in result]
    res_w = zip(test_results, weights)
    test_marks = [r * w for (r, w) in res_w]
    marks = sum(test_marks) 
    success_rate = marks / sum(weights)
    return (success_rate, result)

  return eval_tests

def evaluator(evals):
  def eval_all():

    marks = []
    for (test, qm) in evals:
      success_rate, result = test()
#      print(result)
      individual_test_results = [m for (m, _) in result]
      print(individual_test_results)
      marks.append(success_rate * qm)
    return marks

  return eval_all

def eval_matfun(fname, sub, ref):
  o = sub()
  e = ref()
  if(equals(o, e)):
    return (1, fname)
  else:
    return (0, fname + ": wrong answer")

def eval_named_proc_1(fname, driver):
  subprocess.call(["cp", "drivers/" + driver, "code/"])
  o = subprocess.check_output([mypython, "code/" + driver])
  e = subprocess.check_output([mypython, "mycode/" + driver])
  if(equals(o, e)):
    return (1, fname)
  else:
    return (0, fname + ": wrong answer")
