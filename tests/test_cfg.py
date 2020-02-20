import os

from diraccfg.cfg import CFG


def test_load():
  rels = CFG().loadFromFile(os.path.join(os.path.dirname(__file__), 'releases.cfg'))
  assert rels['Releases']['v6r22']['DIRACOS'] == 'v1r2'  # pylint: disable=unsubscriptable-object