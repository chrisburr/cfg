from cfg.cfg import CFG

cfg_o = CFG()


def test_load():
  rels = cfg_o.loadFromFile('tests/releases.cfg')
  assert rels['Releases']['v6r22']['DIRACOS'] == 'v1r2'
