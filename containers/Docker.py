import docker
client = docker.from_env()
print(client.containers.run("popsv2", ["python3", "hello.py"]))