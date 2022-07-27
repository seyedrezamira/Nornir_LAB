from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
from rich import print as rprint
from pprint import pprint 
nr = InitNornir(config_file="config.yaml")

vlan_list = ["e1/10","e1/20"]

def learned_mac(task):
    # for vlan in vlan_list:
    vlan_status = task.run(task=send_command, command=f"sho mac address-table")
    task.host["items"] = vlan_status.scrapli_response.genie_parse_output()


result = nr.run(task=learned_mac)
print_result(result)

import ipdb
ipdb.set_trace()