# This enables to do, e.g. "python -m cfg aCFGfile.cfg v6r22p13 DIRACOS"

from __future__ import print_function

import sys
import re

from .cfg import CFG

if __name__ == '__main__':
  cfg_o = CFG()
  res = cfg_o.loadFromFile(sys.argv[1])

  if sys.argv[2] == 'latest':
    release = [x for x in list(res['Releases']) if re.match("v[0-9]r[0-9]", x[0:4])][0]
    print(release)
    if len(sys.argv) == 4 and sys.argv[3] == '--print-only':
      exit(0)
  else:
    release = sys.argv[2]

  if len(sys.argv) == 4:
    print(res['Releases'][release][sys.argv[3]])  # pylint: disable=unsubscriptable-object
  else:
    print(res['Releases'][release])  # pylint: disable=unsubscriptable-object
