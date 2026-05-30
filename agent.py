from agents.k8s_tools import (
    create_deployment,
    get_pods,
    delete_deployment
)

from agents.azure_tools import (
    list_storage_accounts,
    create_storage_account,
    delete_storage_account,
    list_acr,
    create_acr,
    delete_registry
)


def run_agent(user_input):

    text = user_input.lower().strip()

    # Kubernetes Commands

    if "create deployment" in text:

        name = text.split()[-1]

        return create_deployment(name)

    elif "check cluster" in text:

        return get_pods()

    elif "delete deployment" in text:

        name = text.split()[-1]

        return delete_deployment(name)

    # Azure Storage Commands

    elif "list storage" in text:

        return list_storage_accounts()

    elif "create storage account" in text:

        name = text.split()[-1]

        return create_storage_account(name)

    elif "delete storage account" in text:

        name = text.split()[-1]

        return delete_storage_account(name)

    # Azure ACR Commands

    elif "list registries" in text:

        return list_acr()

    elif "create registry" in text:

        name = text.split()[-1]

        return create_acr(name)

    elif "delete registry" in text:

        name = text.split()[-1]

        return delete_registry(name)

    else:

        return f"Command not supported: {user_input}"