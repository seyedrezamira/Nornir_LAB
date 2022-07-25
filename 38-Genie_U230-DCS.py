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
    
    
    vlan_num_dic = {}
    int_status_dic = {}
    output_dic = {}
    vlan_list_dic = {}
    
    vlan_list_dic[task.host]=vlan_list
    rprint(vlan_list_dic)

    output_dic[task.host]=vlan_num_dic
    for vlan_num in vlan_list:
        if (vlan_num != "1"):
            interface_per_vlan = task.host["items"]["vlans"][vlan_num]["interfaces"]
            
            int_status_dic = {}
            for int in interface_per_vlan:
                if not str(int).startswith("Port") and task.host["attr"][int]["port_mode"]=="access":
                    admin_state= task.host["attr"][int]["admin_state"]
                    oper_state= task.host["attr"][int]["oper_status"]
                    int_status_dic[int]=[admin_state,oper_state]
            vlan_num_dic[vlan_num]=int_status_dic
    rprint(output_dic)


result = nr.run(task=U230_DCS)

import ipdb
ipdb.set_trace()