from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
from pprint import pprint
from rich import print as rprint

nr = InitNornir(config_file="config.yaml")
dev_name_dic = {}
dev_vlan_dic = {}

def show_interface_status(task):
    show_interface_status = task.run(task=send_command, command="show interface status")
    task.host["items"] = show_interface_status.scrapli_response.genie_parse_output()
    int_list = list(task.host["items"]["interfaces"])
    for interface in int_list:
        vlan_id = task.host["items"]["interfaces"][interface]["vlan"]
        dev_vlan_dic[interface]= vlan_id
    dev_name_dic[task.host] = dev_vlan_dic

result = nr.run(task=show_interface_status)
rprint(dev_name_dic)
