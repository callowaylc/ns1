#!/usr/bin/env python
# List zones for a given domain argument
# Usage: ./example/list-zone.py purewhitesugar.se

# imports #######################################

import sys
import yaml
import logging
import functools
from nsone import NSONE

# constants #####################################

SUCCESS = 0

# func ##########################################

def domain():
	return sys.argv[1]

def config():
	with open('./config.yml', 'r') as f:
		return yaml.load(f)

@functools.lru_cache(maxsize=None)
def logger():
	l = logging.getLogger()
	h = logging.StreamHandler(sys.stderr)

	h.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
	l.setLevel(logging.DEBUG)
	l.addHandler(h)

	return l

def logs(message):
	l = logger()
	l.info(message)

def zone(domain):
	logs(domain)
	ns = NSONE(apiKey=config()['ns1']['api']['key'])
	return ns.loadZone(domain)

# main ##########################################

def main():
	z = zone(domain())

	return SUCCESS

if __name__ == '__main__':
  sys.exit(main())