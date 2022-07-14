from nornir import InitNornir
from nornir_scrapli.tasks import send_command,send_configs
from nornir_utils.plugins.functions import print_result
from pprint import pprint
from rich import print as rprint

nr = InitNornir(config_file="config.yaml")

def show_interface_status(task):
    show_interface_status = task.run(task=send_command, command="show cdp neighbor")
    task.host["items"] = show_interface_status.scrapli_response.genie_parse_output()
    cdp = task.host["items"]["cdp"]["index"]
    for neighbor in cdp:
        local_int = cdp[neighbor]["local_interface"]
        remote_port = cdp[neighbor]["port_id"]
        remote_dev = cdp[neighbor]["device_id"]
        config_commands = [f"interface {local_int}",f"desc connected to {remote_dev} via {remote_port}"]
        task.run(send_configs, configs=config_commands)


result = nr.run(task=show_interface_status)
