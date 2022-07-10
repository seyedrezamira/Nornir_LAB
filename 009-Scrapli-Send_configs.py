from nornir import InitNornir
from nornir_scrapli.tasks import send_configs
from nornir_utils.plugins.functions import print_result




nr = InitNornir(config_file="config.yaml")

def send_config_test(task):
        task.run(task=send_configs, configs= ["feature ospf""router ospf 1","network 0.0.0.0 255.255.255.255 area 0"])

results = nr.run(task=send_config_test)
print_result(results)

