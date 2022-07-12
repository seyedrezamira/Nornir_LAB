from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def pull_random_info(task):
    get_vlan = task.run(task=napalm_get, getters="get_vlans")
    task.host["items"]= get_vlan.result

results=nr.run(task=pull_random_info)
print_result(results)

import ipdb
ipdb.set_trace()

