#!/usr/bin/env python
import argparse
import os, os.path, time
import datatime
import shutil
from shutil import copyfile

ansible = '/path-to-the/ansible/playbooks'
inv_dir = '/path-to-the/inventories'
parser = argparse.ArgumentParser(description='Runer for Ansible playbooks.')
playbook = parser.add_argument("-pl, --playbook", help="Which ansible playbook would you like to run? ", type=str, dest="pbName")
inventory = parser.add_argument("-in, --inventory" help="Inventory to run from", type=str, dest="invName")
group = parser.add_argument("-gr, --group", help="Select the group name from ansible var goup", type=str, dest="gName")
app_verion = parser.add_argument("-ap, --app-version", help="AppVersion to build from", type=str, dest="vName")
serv_verion = parser.add_argument("-se, --serv-version", help="ServiceVersion to build from", type=str, dest="sName")
dev_version = parser.add_argument("-de, --dev-version", help="DevVersion to build from", type=str, dest="dName")
args = parser.parse_args()


if os.path.isfile(f"{ansible}/{playbook}") and os.access(ansible, os.R_ok):
    print(f"{playbook} exist")
if os.path.isdir(f"{inv_dir}/{inventory}"):
    print(f"{inventory} exist")
if os.path.isfile(f"{inventory}/group_vars/{group}.yml"):
    print (f"{gropu} exist")
    cmd = os.system(f"ansible-playbook -i {inventory} -l {group} {playbook} -e app_version={app_version} serv_version={serv_version} dev_version={dev_version}")
    date = datatime.datatime.now().strftime("%Y-%m-%d.%H-%M-%S")
    script_dir = '/path/to/script'
    ansible_log = '/path/to/log'
    dest_log = f'/path/to/ansible-log/deplotmeny-{date}.log'
else:
    print(f"{playbook} not found!")