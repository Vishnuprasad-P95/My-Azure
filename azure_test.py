import subprocess
import sys
import os
subscription = "ec92f3dd-584e-4a42-9fb7-f85b6cadb9b8"


def az_login():
  command = "az login --service-principal -u %s -p %s --tenant %s" % (os.getenv("SPN-AZ-POC"), os.getenv("SPN-POC-PASS"), os.getenv("SPN-POC-TENENT"))
  command2 = "az account set --subscription %s" % subscription
  subprocess.check_call(command, shell=True, stdout=sys.stdout, stderr=subprocess.STDOUT)
  subprocess.check_call(command2, shell=True, stdout=sys.stdout, stderr=subprocess.STDOUT)


def create_resource_group(location, temp, param):
  az_login()
  command = "az deployment sub create --name RGDeployment --location %s --template-file %s --parameters %s" %(location, temp, param)
  subprocess.check_call(command, shell=True, stdout=sys.stdout, stderr=subprocess.STDOUT)


def delete_resource_group(resource_group):
  command = "az group delete -n %s --yes" % resource_group
  subprocess.check_call(command, shell=True, stdout=sys.stdout, stderr=subprocess.STDOUT)


template = "C:\\Users\\vishn\PycharmProjects\My-Azure\ARM\RG_temp.json"
parameter = "C:\\Users\\vishn\PycharmProjects\My-Azure\ARM\RG_param.json"
loc = "eastus"

create_resource_group(loc, template, parameter)
delete_resource_group("RG-VM-DEVOPS")