import requests
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir.core.task import Result

nr = InitNornir(config_file="config.yaml")

requests.packages.urllib3.disable_warnings()

headers = {"Accept": "application/yang-data+json"}
def testconf(task):
    url = f"https://{task.host.hostname}:443/restconf/data/native/interface"
    response = requests.get(url= url, headers= headers, auth=(f"{task.host.username}", f"{task.host.password}"), verify=False)
    return Result(host=task.host, result=response.text)

result = nr.run(task=testconf)
print_result(result)
