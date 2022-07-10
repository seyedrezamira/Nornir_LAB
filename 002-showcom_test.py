from nornir import InitNornir
import pprint
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command
from getpass import getpass


nr = InitNornir(config_file="config.yaml")

def show_command(task):
    showver = task.run(netmiko_send_command, command_string="show version")


result = nr.run(task=show_command)
print_result(result)