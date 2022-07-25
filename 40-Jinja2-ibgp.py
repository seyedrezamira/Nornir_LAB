from nornir import InitNornir
from nornir_scrapli.tasks import send_configs
from nornir_utils.plugins.functions import print_result
from nornir_jinja2.plugins.tasks import template_file
from nornir_utils.plugins.tasks.data import load_yaml


nr = InitNornir(config_file="config.yaml")

def load_vars(task):
    data = task.run(task=load_yaml, file=f"./host_vars/{task.host}.yaml")
    task.host["vars"] = data.result
    bgp(task)

def bgp(task):
    template = task.run(task=template_file, template="bgp.j2", path="templates")
    task.host["bgp_config"] = template.result
    rendered = task.host["bgp_config"]
    config_list = rendered.splitlines()
    task.run(task=send_configs, configs=config_list)


results = nr.run(task=load_vars)
print_result(results)


