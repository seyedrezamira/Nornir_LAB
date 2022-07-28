from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
from rich import print as rprint
from tqdm import tqdm

nr = InitNornir(config_file="config.yaml")

def learned_mac(task, progress_bar):
    vlan_status = task.run(task=send_command, command=f"sho mac address-table dynamic")
    task.host["items"] = vlan_status.scrapli_response.genie_parse_output()
    progress_bar.update()


with tqdm(total=len(nr.inventory.hosts)) as progress_bar:
    result = nr.run(task=learned_mac, progress_bar=progress_bar)
    
print_result(result)
