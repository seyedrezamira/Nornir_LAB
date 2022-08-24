from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
from rich import print as rprint
from pprint import pprint 

nr = InitNornir(config_file="config.yaml")


def show_vlan(task):
    vlan_list = []
    int_dic = {}
    int_list = []
    vlan_status = task.run(task=send_command, command="show vlan")
    task.host["vlan"] = vlan_status.scrapli_response.genie_parse_output()
    vlan_nums = task.host["vlan"]["vlans"]
    for vlan in vlan_nums:
        vlan_list.append(vlan)

    interface_status = task.run(task=send_command, command="show interface")
    task.host["int"] = interface_status.scrapli_response.genie_parse_output()
    interfaces = task.host["int"]
    for int in interfaces:
        if str(int).startswith("E") or str(int).startswith("p"):
            int_list.append(int)
            admin_state = interfaces[int]["admin_state"]
            oper_state = interfaces[int]["oper_status"]
            int_dic[int] = [admin_state,oper_state]
    # for intnum in int_list:
        interface_status = task.run(task=send_command, command=f"show mac address interface {int}")
        task.host["mac"] = interface_status.scrapli_response.genie_parse_output()
        mac_list = []
        if task.host["mac"] != []:
            test = task.host["mac"]["mac_table"]["vlans"]
            for vlan in test:
                test1 = test[vlan]["mac_addresses"]
                for macmac in test1:
                    mac_list.append(macmac)
            rprint(f"Learnt MAC address under {int} is\n {mac_list}")
            # for mac in test:
            #     mac_list = test["mac"]["vlan"]["mac_addresses"]
            #     for macmac in mac_list:
            #         print(macmac)
                # rprint(f"information for {int} is {mac_list}")
                # for mac in test:
        #     if mac :
        #         rprint(f"information for {intnum} is {mac}")

    # rprint(f"\n[red]The list of vlans for [bold]{task.host}[/bold] is {vlan_list}[/red]\n interface status are {int_dic}")

    # interface_status = task.run(task=send_command, command="show mac address int e1/20 ")
    # task.host["mac"] = interface_status.scrapli_response.genie_parse_output()
        


    # vlan_list = list(task.host["vlan"]["vlans"])
    
    # vlan_num_dic = {}
    # int_status_dic = {}
    # output_dic = {}
    # vlan_list_dic = {}
    
    # vlan_list_dic[task.host]=vlan_list
    # rprint(f"[red]{vlan_list_dic}")


#     output_dic[task.host]=vlan_num_dic
#     for vlan_num in vlan_list:
#         if (vlan_num != "1"):

#             interface_per_vlan = task.host["vlan"]["vlans"][vlan_num]["interfaces"]
            
#             int_status_dic = {}
#             for int in interface_per_vlan:
#                 # vlan_status = task.run(task=send_command, command=f"sho mac address-table inter {int}")
#                 # task.host["mac"] = vlan_status.scrapli_response.genie_parse_output()
#                 if not str(int).startswith("Port") and task.host["int"][int]["port_mode"]=="access":
#                     admin_state= task.host["int"][int]["admin_state"]
#                     oper_state= task.host["int"][int]["oper_status"]
#                     int_status_dic[int]=[admin_state,oper_state]
#             vlan_num_dic[vlan_num]=int_status_dic
#     rprint(output_dic)

# def show_int(task):
#     interface_status = task.run(task=send_command, command="show interface")
#     task.host["int"] = interface_status.scrapli_response.genie_parse_output()


nr.run(task=show_vlan)
# nr.run(task=int_stat)

# print_result(result)

import ipdb
ipdb.set_trace()
