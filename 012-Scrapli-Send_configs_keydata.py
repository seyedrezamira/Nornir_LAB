from nornir import InitNornir
from nornir_scrapli.tasks import send_configs
from nornir_utils.plugins.functions import print_result




nr = InitNornir(config_file="config.yaml")

def send_config_test(task):
#        task.run(task=send_configs, configs= ["int loopback 0",f"ip address {task.host['loopback0']}/32", "copy run start"])
        task.run(task=send_configs, configs= ["feature ospf",f"router ospf 1", f"router-id {task.host['loopback0']}"])

results = nr.run(task=send_config_test)
print_result(results)