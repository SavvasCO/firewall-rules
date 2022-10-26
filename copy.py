import os
import json

print("=== FIREWALL WALL COPY TOOL ===")

print()
subscription = input("Subscription: ")

os.system("az login")
os.system("az account set --name " + subscription)

print("SOURCE: (where to get the firewall rules from)")
source_resource_group = input("Resource group: ")
source_server = input("Server name: ")

print()
print("Getting firewall rules from " + source_resource_group + "/" + source_server)

output = os.popen("az mysql server firewall-rule list --resource-group " + source_resource_group + " --server-name " + source_server).read()
rules = json.loads(output)

print()
print("Got " + str(len(rules)) + " rules:")

print()
for rule in rules:
    print("* " + rule["name"])

print()
print("DESTINATION: (where to copy the firewall rules to)")
destination_resource_group = input("Resource group: ")
destination_server = input("Server name: ")

print()
print("Copying firewall rules to " + destination_resource_group + "/" + destination_server + "...")

for rule in rules:
    print()
    print("Copying " + rule["name"] + "...")
    os.system("az mysql flexible-server firewall-rule create --resource-group " + destination_resource_group + " --name " + destination_server + " --rule-name " + rule["name"] + " --start-ip-address " + rule["startIpAddress"] + " --end-ip-address " + rule["endIpAddress"])
    print("Done.")

print()
print("Successfully copied " + str(len(rules)) + " rules into " + destination_resource_group + "/" + destination_server)