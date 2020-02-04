# cfg
DIRAC cfg file parser


# installation

pip install git+https://github.com/DIRACGrid/cfg.git#egg=cfg

# usage

The simplest way is by doing:

```
python -m aDIRACCFGFile.cfg something something
```

e.g. if you want to parse the releases.cfg file:

```
python -m cfg ../DIRAC/releases.cfg v6r22
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
python -m cfg ../DIRAC/releases.cfg v6r22 Externals
v6r6p8
```
