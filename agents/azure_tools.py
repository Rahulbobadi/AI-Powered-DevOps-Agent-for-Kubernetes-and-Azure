import subprocess
import json

RESOURCE_GROUP = "ai-self-healing-rg"
LOCATION = "centralindia"


def list_storage_accounts():

    result = subprocess.run(
        [
            "az",
            "storage",
            "account",
            "list",
            "-o",
            "json"
        ],
        capture_output=True,
        text=True
    )
    
    return f"""
RETURN CODE:
{result.returncode}

STDOUT:
{result.stdout}

STDERR:
{result.stderr}
"""

def create_storage_account(name):

    result = subprocess.run(
        [
            "az",
            "storage",
            "account",
            "create",
            "--name",
            name,
            "--resource-group",
            RESOURCE_GROUP,
            "--location",
            LOCATION,
            "--sku",
            "Standard_LRS"
        ],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return result.stderr

    data =json.loads(result.stdout)

    return f"""

✅ Storage Account Created

Name: {data['name']}
Resource Group: {data['resourceGroup']}
Location: {data['location']}
SKU: {data['sku']['name']}
Status: {data['provisioningState']}

Blob Endpoint:
{data['primaryEndpoints']['blob']}
"""

def list_acr():

    result = subprocess.run(
        [
            "az",
            "acr",
            "list",
            "-o",
            "table"
        ],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        return result.stdout

    return result.stderr

def delete_storage_account(name):

    result = subprocess.run(
        [
            "az",
            "storage",
            "account",
            "delete",
            "--name",
            name,
            "--resource-group",
            RESOURCE_GROUP,
            "--yes"
        ],
        capture_output=True,
        text=True
    )

    return (
        f"Return Code: {result.returncode}\n\n"
        f"STDOUT:\n{result.stdout}\n\n"
        f"STDERR:\n{result.stderr}"
    )

def delete_registry(name):

    result = subprocess.run(
        [
            "az",
            "acr",
            "delete",
            "--name",
            name,
            "--resource-group",
            RESOURCE_GROUP,
            "--yes"
        ],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        return f"✅ Registry {name} deleted"

    return result.stderr

def create_acr(name):

    result = subprocess.run(
        [
            "az",
            "acr",
            "create",
            "--name",
            name,
            "--resource-group",
            RESOURCE_GROUP,
            "--sku",
            "Basic"
        ],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        return result.stdout

    return f"""
✅ Container Registry Created

Name: {data['name']}
Location: {data['location']}
SKU: {data['sku']['name']}
Login Server: {data['loginServer']}
"""
