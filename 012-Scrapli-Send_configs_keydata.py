from nornir import InitNornir
from nornir_scrapli.tasks import send_configs
from nornir_utils.plugins.functions import print_result




nr = InitNornir(config_file="config.yaml")

def send_config_test(task):
        task.run(task=send_configs, configs= ["no int loo0","int loopback 0",f"ip address {task.host['loopback0']}/32"])
#        task.run(task=send_configs, configs= [f"router bgp {task.host['bgp']}", f"router-id {task.host['loopback0']}"])

results = nr.run(task=send_config_test)
print_result(results)