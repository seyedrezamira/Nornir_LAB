from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
from rich import print as rprint

nr = InitNornir(config_file="config.yaml")

with open("reader.txt", "r") as f:
    filelines = f.read().splitlines()

failed_list = []

def ping_result(task):
    for target in filelines:
        task_res = task.run(task=send_command, Command="ping" + target)
        response = task_res.result
        
        if not "!!!" in response:
            failed_list.append(f"{task.host} failed to ping {target}")

results = nr.run(task=ping_result)
if failed_list:
    sorted_list = sorted(failed_list)
    rprint(sorted_list)
else:
    print("All pings were successful")