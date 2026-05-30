from kubernetes import client, config

config.load_incluster_config()


def get_pods():
    v1 = client.CoreV1Api()

    pods = v1.list_pod_for_all_namespaces()

    output = "| Namespace | Pod |\n"
    output += "|-----------|-----|\n"

    for pod in pods.items:

        output += (
            f"| {pod.metadata.namespace} "
            f"| {pod.metadata.name} |\n"
        )

    return output


def create_deployment(name, image="nginx"):
    return f"Create deployment requested: {name}"


def delete_deployment(name):
    return f"Delete deployment requested: {name}"
