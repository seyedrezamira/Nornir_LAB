from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

commands = input("\nEnter commands you wish to send: ")
cmds = commands.split(",")  #this command convert input to List

def send_wish_command(task):
    for cmd in cmds:
        task.run(task=send_command, command= cmd)

results=nr.run(task=send_wish_command)
print_result(results)
