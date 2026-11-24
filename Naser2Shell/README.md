# Naser2Shell

Finding-driven security validation tool based on the ZeroDay Library findings.

## Installation (Linux)

```
git clone <repo>
cd Naser2Shell
chmod +x naser2shell.py
```

## Installation (Termux)

```
pkg install python
cd Naser2Shell
chmod +x naser2shell.py
```

## Start (Linux)

```
python3 naser2shell.py --list
python3 naser2shell.py --finding 003
python3 naser2shell.py --finding 008 --verify
python3 naser2shell.py --all --target /path/to/app
```

## Start (Termux)

```
python naser2shell.py --list
```

## Options

- `--list` list findings
- `--finding ID` run one module
- `--verify` verification pass
- `--all` run all modules for configured profile
- `--target PATH` target application root
