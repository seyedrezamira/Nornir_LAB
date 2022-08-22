from ipaddress import ip_address, ip_network
from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

target = input("Enter the target IP: ")
ipaddr = ip_address(target)


def get_routes(task):
    routes = task.run(task=send_command, command="show ip route")
    task.host["facts"] = routes.scrapli_response.genie_parse_output()
    prefixes = task.host["facts"]["vrf"]["default"]["address_family"]["ipv4"]["routes"]
    for prefix in prefixes:
        net = ip_network(prefix)
        if ipaddr in net:
            print(f"{ipaddr} is present on device {task.host} (network: {net}")

nr.run(task=get_routes)

