from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")


def show_command_test(task):
        task.run(task=netmiko_send_config, config_file="configs.txt")


results = nr.run(task=show_command_test)
print_result(results)
