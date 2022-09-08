import os
import json

subscription = input("Subscription: ")
print("COPY FROM:")
source_resource_group = input("Resource group: ")
source_server = input("Server name: ")
print("TO:")
destination_resource_group = input("Resource group: ")
destination_server = input("Server name: ")

os.system("az login")
os.system("az account set --name " + subscription)

output = os.popen("az mysql server firewall-rule list --resource-group " + source_resource_group + " --server-name " + source_server).read()
rules = json.loads(output)

for rule in rules:
    os.system("az mysql server firewall-rule create --resource-group " + destination_resource_group + " --server-name " + destination_server + " --name " + rule["name"] + " --start-ip-address " + rule["startIpAddress"] + " --end-ip-address " + rule["endIpAddress"])