from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
from pprint import pprint
from rich import print as rprint

nr = InitNornir(config_file="config.yaml")

def show_vlan(task):
    show_vlan = task.run(task=send_command, command="show interface status")
    task.host["items"] = show_vlan.scrapli_response.genie_parse_output()
    
    int_list = list(task.host["items"]["interfaces"])
    rprint (f"{task.host} interface list:")
    for interface in int_list:
        vlan_id = task.host["items"]["interfaces"][interface]["vlan"]
        rprint (f"{interface}: \"{vlan_id}\"")

   
result = nr.run(task=show_vlan)
