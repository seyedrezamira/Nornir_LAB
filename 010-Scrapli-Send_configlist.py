from nornir import InitNornir
from nornir_scrapli.tasks import send_config
from nornir_utils.plugins.functions import print_result




nr = InitNornir(config_file="config.yaml")
config_list = ["feature ospf","router ospf 1","network 0.0.0.0 255.255.255.255 area 0"]

def send_config_test(task):
        for conf in config_list:
            task.run(task=send_config, config= conf)

results = nr.run(task=send_config_test)
print_result(results)

