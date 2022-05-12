import os
import subprocess

def StartContainer(image,script,ip):
    result = os.popen(f'sudo docker run {image} python3 ./{script} {ip}').read()
    return result
def StartQueue():

    subprocess.call('python3 /home/azureuser/project/QueueHandler/queueHandler.py', shell=True)