from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
from rich import print as rprint
from pprint import pprint

nr = InitNornir(config_file="config.yaml")

def find_ip(task):
    version_result = task.run(task=send_command, command="show licen usage")
    task.host["facts"] = version_result.scrapli_response.genie_parse_output()
    

results = nr.run(task=find_ip)
print_result(results)

# import ipdb
# ipdb.set_trace()
