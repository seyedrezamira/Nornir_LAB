from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
from rich import print as rprint


nr = InitNornir(config_file="config.yaml")

def show_interface_status(task):
    show_ip_result = task.run(task=send_command, command="show vlan")
    task.host["items"] = show_ip_result.scrapli_response.genie_parse_output()
    vlan_list = list(task.host["items"]["vlans"])
    for vlan_num in vlan_list:
        interface_per_vlan = task.host["items"]["vlans"][vlan_num]["interfaces"]
        if vlan_num  != "1":
            rprint (f"\nVLAN {vlan_num} is set on: {interface_per_vlan}")

    # for i in vlan_list:
        
        #
        #  print(f"the list of interfaces which are assigned to vlan {i} are {task.host["items"][i]["interfaces"]}")
            #print(f"The list of Vlan in {task.host} is --> {vlan_list}")

result = nr.run(task=show_interface_status)
#print_result(result)

# import ipdb
# ipdb.set_trace()

