# evildork👁️

- Dork only one specific domain or all subdomains available
- Dork targeting a general target (likely to be a person)
- Produce an html output result page with all the dorks links 
- Be aware that Google after some tries will add some captcha to check if you're a bot or not.


## Installation 📥

- `git clone https://github.com/Fricciolosa-Red-Team/evildork.git`
- `cd evildork`
- `python3 evildork.py`

## Usage 🚀

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

## Examples ⚙️

- `python3 evildork.py -d target.example`
- `python3 evildork.py -d target.example -s`
- `python3 evildork.py -t username`

## Contributing 🤝

If you want to submit new dorks, just open an [issue](https://github.com/Fricciolosa-Red-Team/evildork/issues) / [pull request](https://github.com/Fricciolosa-Red-Team/evildork/pulls).

## License 📜

This repository is under [MIT License](https://github.com/Fricciolosa-Red-Team/evildork/blob/master/LICENSE).
