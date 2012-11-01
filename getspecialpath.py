# LAB(begin solution)
def get_special_paths(dirname):
  """Given a dirname, returns a list of all its special files."""
  result = []
  paths = os.listdir(dirname)  # list of paths in that dir
  for fname in paths:
    match = re.search(r'__(\w+)__', fname)
    if match:
      result.append(os.path.abspath(os.path.join(dirname, fname)))
  return result

