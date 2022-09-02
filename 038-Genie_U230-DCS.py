from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from rich import print as rprint


def update_dictionary(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = value
    elif type(dictionary[key]) == list:
        dictionary[key].append(value)
    else:
        dictionary[key] = [dictionary[key], value]


nr = InitNornir(config_file="config.yaml")

def show_vlan(task):
    vlan_list = []
    int_dic = {}
    new_dic = {}
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
            admin_state = interfaces[int]["admin_state"]
            oper_state = interfaces[int]["oper_status"]
            int_dic[int] = [admin_state,oper_state]
    for vlan in vlan_list:
        interface_status = task.run(task=send_command, command=f"show mac address vlan {vlan}")
        task.host["mac"] = interface_status.scrapli_response.genie_parse_output()
        vlans_dic = task.host["mac"]
        mac_dic = {}
        if vlans_dic != []:
            mac_vlan = vlans_dic["mac_table"]["vlans"][vlan]["mac_addresses"]
            mac_list = []
            vlan_dic = {}
            for mac in mac_vlan:
                if mac_vlan[mac]["entry"] == "*":
                    mac_list.append(mac)
                    mac_int = mac_vlan[mac]["interfaces"]
                    for macs in mac_int:
                        interf = mac_int[macs]["interface"]
                    vlan_dic[vlan] = mac_list
                    mac_dic[interf] = vlan_dic

        if mac_dic !={}:
            for k,v in mac_dic.items():
                update_dictionary(new_dic,k,v)

    rprint(f"The list of vlans for [red][bold]{task.host}[/bold][/red] is {vlan_list}")
    rprint(f"\n\nThe status of interfaces on [red][bold]{task.host}[/bold][/red] is {int_dic}")
    rprint(f"\n\nLearnt MAC list on [red][bold]{task.host}[/bold][/red] is {new_dic}")


nr.run(task=show_vlan)

