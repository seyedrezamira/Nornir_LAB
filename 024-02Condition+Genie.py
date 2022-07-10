from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
from rich import print as rprint

nr = InitNornir(config_file="config.yaml")
dic = {}

def show_command_test(task):
    version_result = task.run(task=send_command, command="show interface")
    task.host["facts"] = version_result.scrapli_response.genie_parse_output()
    ip = list(task.host["facts"]["Ethernet1/1"]["ipv4"].values())
    ip_add = ip[0]["ip"]
    if ip_add == "192.168.111.1":
        rprint(f"the requested ip address is belong to {task.host}")
    
results = nr.run(task=show_command_test)
#pprint (dic)

# print_result(results)

import ipdb
ipdb.set_trace()
