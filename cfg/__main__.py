# __main__.py

import sys

from .cfg import CFG

if __name__ == '__main__':
  cfg_o = CFG()
  res = cfg_o.loadFromFile(sys.argv[1])
  if len(sys.argv) == 4:
    print(res['Releases'][sys.argv[2]][sys.argv[3]])
  else:
    print(res['Releases'][sys.argv[2]])
