from nornir import InitNornir
from nornir_scrapli.tasks import send_command,send_configs
from nornir_utils.plugins.functions import print_result
from pprint import pprint
from rich import print as rprint

nr = InitNornir(config_file="config.yaml")

def show_version(task):
    show_ver = task.run(task=send_command, command="show version")
    clock_result = show_ver.scrapli_response.textfsm_parse_output()
    task.host["facts"] = show_ver.scrapli_response.textfsm_parse_output()
    print(clock_result)


result = nr.run(task=show_version)

import ipdb
ipdb.set_trace()
