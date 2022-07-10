from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
from pprint import pprint
from rich import print as rprint

nr = InitNornir(config_file="config.yaml")
dic = {}

def show_command_test(task):
    version_result = task.run(task=send_command, command="show version")
    task.host["facts"] = version_result.scrapli_response.genie_parse_output()
    model = task.host["facts"]["platform"]["hardware"]["model"]
    if model == "Nexus9000 C9300v":
        rprint(f"{task.host}: [green]Version Checked Passed[green]")
    else:
        rprint(f"{task.host}: [red]Not accessible[red]")
    dic[task.host] = model
    #print(f"the device model of {task.host} is {model}")

results = nr.run(task=show_command_test)
pprint (dic)

# print_result(results)

# import ipdb
# ipdb.set_trace()
