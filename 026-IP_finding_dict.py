from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
from rich import print as rprint
from pprint import pprint

nr = InitNornir(config_file="config.yaml")
IP_ADD = "192.168.111.1"

def find_ip(task):
    version_result = task.run(task=send_command, command="show interface")
    task.host["facts"] = version_result.scrapli_response.genie_parse_output()
    

results = nr.run(task=find_ip)

import ipdb
ipdb.set_trace()
