from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
from rich import print as rprint
from pprint import pprint 
nr = InitNornir(config_file="config.yaml")

def learned_mac(task):
    vlan_status = task.run(task=send_command, command="show mac address-table")
    task.host["items"] = vlan_status.scrapli_response.genie_parse_output()
 

result = nr.run(task=learned_mac)

import ipdb
ipdb.set_trace()