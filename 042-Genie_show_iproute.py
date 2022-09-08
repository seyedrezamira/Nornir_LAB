from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
from rich import print as rprint
from pprint import pprint 

nr = InitNornir(config_file="config.yaml")

def routing_infor(task,test):
    route_status = task.run(task=send_command, command=f"{test}")
    task.host["items"] = route_status.scrapli_response.genie_parse_output()
    routes = task.host["items"]["vrf"]["default"]["address_family"]["ipv4"]["routes"]
    for key in routes:
        try:
            process_id = routes[key]["process_id"]
            rprint(f"process_id of {key} is {process_id}")
        except KeyError:
            pass



result = nr.run(task={routing_infor, "show ip route"})

# import ipdb
# ipdb.set_trace()