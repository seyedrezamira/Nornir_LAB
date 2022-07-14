from nornir import InitNornir
from nornir_scrapli.tasks import send_command,send_configs
from nornir_utils.plugins.functions import print_result
from pprint import pprint
from rich import print as rprint

nr = InitNornir(config_file="config.yaml")

def test_clock(task):
    clock_check = task.run(task=send_command, command="show clock")
    str_output = clock_check.scrapli_response.textfsm_parse_output()
    rprint(f"Time information on {task.host} is {str_output}")


result = nr.run(task=test_clock)
