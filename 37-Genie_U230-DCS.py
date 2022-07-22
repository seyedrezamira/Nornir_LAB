from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
from rich import print as rprint
from pprint import pprint 
nr = InitNornir(config_file="config.yaml")

def U230_DCS(task):
    vlan_status = task.run(task=send_command, command="show vlan")
    task.host["items"] = vlan_status.scrapli_response.genie_parse_output()
    
    interface_status = task.run(task=send_command, command="show interface")
    task.host["attr"] = interface_status.scrapli_response.genie_parse_output()
    
    vlan_list = list(task.host["items"]["vlans"])
    dic = {task.host:vlan_list}
    
    # rprint(dic)

    # rprint(f"\nThe list of Vlan in {task.host} is --> {vlan_list}")
        
    for vlan_num in vlan_list:
        if vlan_num  != "1":
            interface_per_vlan = task.host["items"]["vlans"][vlan_num]["interfaces"]
            dic[vlan_num] = interface_per_vlan
            # rprint (f"\nVLAN {vlan_num} is set on: {interface_per_vlan}")
    rprint(dic)
            # for int in interface_per_vlan:
            #     if not str(int).startswith("Port"):
            #         admin_state= task.host["attr"][int]["admin_state"]
            #         oper_state= task.host["attr"][int]["oper_status"]
            #         rprint (f"\n{int}:\nadmin state is {admin_state}\noperation status is {oper_state}\n")


result = nr.run(task=U230_DCS)

# import ipdb
# ipdb.set_trace()