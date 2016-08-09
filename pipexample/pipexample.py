
class Foo:
  def __init__(self, x):
    self.x = x

def readme():
  import os
  CURDIR = os.path.dirname(os.path.abspath(__file__))
  fpath = os.path.join(CURDIR, "testfile.txt")
  with file(fpath, "r") as f:
    return f.read()