import subprocess
import sys
import os
subscription = "409e504e-1926-4120-b7ae-64139d44a951"


def run_process(command):
  p = subprocess.Popen(command, shell=True, stdout=sys.stdout, stderr=sys.stderr)
  p.communicate()


def az_login():
  command = "az login --service-principal -u %s -p %s --tenant %s" % (os.getenv("SPN-AZ-ID"), os.getenv("SPN-POC-PASS"), os.getenv("SPN-POC-TENENT"))
  command2 = "az account set --subscription %s" % subscription
  run_process(command)
  run_process(command2)


def create_resource_group(location, temp, param):
  az_login()
  command = "az deployment sub create --name RGDeployment --location %s --template-file %s --parameters %s" %(location, temp, param)
  run_process(command)


def delete_resource_group(resource_group):
  az_login()
  command = "az group delete -n %s --yes" % resource_group
  run_process(command)


def create_resource_arm_deploy(rg, temp, parm):
  az_login()
  command = "az deployment group create --resource-group %s --template-file %s --parameters %s" % (rg, temp, parm)
  run_process(command)


def delete_vm(rg, vm_name):
  az_login()
  command = "az vm delete -g %s -n %s --yes" % (rg, vm_name)
  run_process(command)


RG_template = "C:\\Users\\vishn\PycharmProjects\My-Azure\ARM\RG_temp.json"
RG_parameter = "C:\\Users\\vishn\PycharmProjects\My-Azure\ARM\RG_param.json"
VM_template = "C:\\Users\\vishn\PycharmProjects\My-Azure\ARM\\vm_temp.json"
VM_parameter = "C:\\Users\\vishn\PycharmProjects\My-Azure\ARM\\vm_param.json"
WA_template = "C:\\Users\\vishn\PycharmProjects\My-Azure\ARM\Web_App_temp.json"
WA_parameter = "C:\\Users\\vishn\PycharmProjects\My-Azure\ARM\Web_App_param.json"
linux_VM_template = "C:\\Users\\vishn\PycharmProjects\My-Azure\ARM\linux_vm_temp.json"
linux_VM_parameter = "C:\\Users\\vishn\PycharmProjects\My-Azure\ARM\linux_vm_param.json"
loc = "eastus"
RG = "RG-VM-DEVOPS"
vm_name = "devopsvm"
# create_resource_group(loc, RG_template, RG_parameter)
delete_resource_group(RG)
# create_resource_arm_deploy(RG, VM_template, VM_parameter)
# delete_vm(RG, vm_name)
# create_resource_arm_deploy("RG-WEBAPP-DEVOPS", WA_template, WA_parameter)
# create_resource_arm_deploy(RG, linux_VM_template, linux_VM_parameter)
