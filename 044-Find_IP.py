from ipaddress import ip_address, ip_network
from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
from rich import print as rprint

nr = InitNornir(config_file="config.yaml")

target = input("Enter the target IP: ")
ipaddr = ip_address(target)
my_list = []


def get_routes(task):
    routes = task.run(task=send_command, command="show ip route")
    task.host["facts"] = routes.scrapli_response.genie_parse_output()
    prefixes = task.host["facts"]["vrf"]["default"]["address_family"]["ipv4"]["routes"]
    for prefix in prefixes:
        net = ip_network(prefix)
        # if ipaddr in net:
        #     print(f"{ipaddr} is present on device {task.host} (network: {net}")
        if ipaddr in net:
            source_proto = prefixes[prefix]["source_protocol"]
            if source_proto == "connected":
                try:
                    outgoing_intf = prefixes[prefix]["next_hop"]["outgoing_interface"]
                    for intf in outgoing_intf:
                        exit_intf = intf
                        my_list.append(f"{task.host} is connected to {target} via interface {exit_intf}")
                except KeyError:
                    pass
        else:
            try:
                next_hop_list = prefixes[prefix]["next_hop"]["next_hop_list"]
                for key in next_hop_list:
                    next_hop = next_hop_list[key]["next_hop"]
                    my_list.append(f"{task.host} can reach {target} via next hop {next_hop} ({source_proto})")
            except KeyError:
                pass

nr.run(task=get_routes)
if my_list:
    rprint(my_list)
else:
    print("This IP is not exist in the network")


