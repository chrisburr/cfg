# This enables to do, e.g. "python -m cfg aCFGfile.cfg v6r22p13 DIRACOS"

import sys

from .cfg import CFG

if __name__ == '__main__':
  cfg_o = CFG()
  res = cfg_o.loadFromFile(sys.argv[1])
  if len(sys.argv) == 4:
    print(res['Releases'][sys.argv[2]][sys.argv[3]])  # pylint: disable=unsubscriptable-object
  else:
    print(res['Releases'][sys.argv[2]])  # pylint: disable=unsubscriptable-object
