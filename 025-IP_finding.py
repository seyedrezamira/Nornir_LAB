from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
from rich import print as rprint
from pprint import pprint

nr = InitNornir(config_file="config.yaml")
IP_ADD = input("\nPlease type the IP address which you are looking for: ")

def find_ip(task):
    version_result = task.run(task=send_command, command="show interface")
    task.host["facts"] = version_result.scrapli_response.genie_parse_output()
   
    intname = list(task.host["facts"].keys())
    for intnum in intname:
        list1 = list(task.host["facts"][intnum]["ipv4"].values())
        if (list1[0]["ip"] == IP_ADD):
            rprint(f"\n {IP_ADD} is blong to [green]{task.host}[green] --> {intnum} \n")
        
    
results = nr.run(task=find_ip)
