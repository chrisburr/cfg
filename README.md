# diraccfg
DIRAC cfg file parser


# installation

pip install git+https://github.com/DIRACGrid/cfg.git#egg=diraccfg

# usage

The simplest way is by doing:

```
python -m diraccfg a_dirac_cfg_file.cfg something something
```

e.g. if you want to parse the releases.cfg file:

```
# python -m diraccfg ../DIRAC/releases.cfg v6r22
Modules = DIRAC
Modules += VMDIRAC:v2r4-pre2
Modules += RESTDIRAC:v0r6
Modules += COMDIRAC:v0r17
Modules += WebAppDIRAC:v4r0p5
Modules += OAuthDIRAC:v0r1-pre1
Externals = v6r6p8
DIRACOS = v1r2
```

or:

```
# python -m diraccfg ../DIRAC/releases.cfg v6r22 Externals
v6r6p8
```

for finding the latest release (e.g. no "integration"):

```
# python -m diraccfg ../DIRAC/releases.cfg latest --print-only
v7r0-pre15
```
