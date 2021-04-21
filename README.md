# evildork🐍

- dork only one specific domain or all subdomains available
- produce an html output result page with all links

## Installation

- `git clone https://github.com/Fricciolosa-Red-Team/evildork.git`
- `cd evildork`
- `python3 evildork.py`

## Usage

```
usage: evildork.py [-h] [-d DOMAIN] [-s] [-t TARGET] [-v]

Evildork targeting your fiancee

optional arguments:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        Set the target (a domain)
  -s, --subdomain       Search also for subdomains
  -t TARGET, --target TARGET
                        Set the target (general)
  -v, --version         Show the version of evildork
```

## Examples

- `python3 evildork.py -d target.example`
- `python3 evildork.py -d target.example -s`
- `python3 evildork.py -t random_username`
