from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result


nr = InitNornir(config_file="config.yaml")

def show_interface_status(task):
    show_ip_result = task.run(task=send_command, command="show interface")
    task.host["items"] = show_ip_result.scrapli_response.genie_parse_output()

result = nr.run(task=show_interface_status)

import ipdb
ipdb.set_trace()
