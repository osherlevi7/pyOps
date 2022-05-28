#!/usr/bin/env python

import argparse
import yaml
import sys
import json

def menu():
    parser = argparse.ArgumentParser(description="Read a YAML file and parse it")
    parser.add_argument("-v, --version", required=False, default=None, type=str, help="")
    return parser

def read_yaml():
    with open("list.yaml", "r") as infile:
        try: 
            yaml_file = yaml.safe_load(infile)
        except yaml.YAMLError as exc:
            print(exc)
            raise exc
    return yaml_file

def main(args):
    release_info = read_yaml()
    if args['version']:
        versions = json.dumps(release_info[args['version']])
        print(versions)
    else: 
        k = list(release_info.keys())
        string_out = json.dumps(k)
        print(string_out)
if __name__ == '__main__':
    args = vars(manu().parse_args())
    main(args=args)