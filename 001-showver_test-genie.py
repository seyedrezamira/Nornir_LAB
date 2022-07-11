from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command
from getpass import getpass
from pprint import pprint


nr = InitNornir(config_file="config.yaml")

hosts_dict = {}

def show_command(task):
    showver = task.run(task=netmiko_send_command, command_string="sho license usage", use_genie=True)
    task.host["items"] = showver.result
    # version = task.host["items"]["platform"]["software"]["system_version"]
    # hosts_dict[task.host] = version


result = nr.run(task=show_command)
print_result(result)
#pprint(hosts_dict)

# import ipdb
# ipdb.set_trace()
