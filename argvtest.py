# LAB(begin solution)
def get_special_paths(dirname):
  import os
  import re
  """Given a dirname, returns a list of all its special files."""
  result = []
  paths = os.listdir(dirname)  # list of paths in that dir
  #print "paths", paths
  for fname in paths:
    #match = re.search(r'__(\w+)__', fname)
    match = re.search(r"(\w)+[.]png", fname)
    if match:
      result.append(os.path.abspath(os.path.join(dirname, fname)))
  return result


def main():
    import sys
    print sys.argv
    args = sys.argv[1:]
    todir = args[
            ]
    print "args", args


    paths = []
    for dirname in args:
        print dirname
        paths.extend(get_special_paths(dirname))
        print "paths", paths
        

if __name__=="__main__":
    main()
