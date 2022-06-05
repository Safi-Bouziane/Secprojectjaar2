import os
import subprocess

def StartContainer(image,script,ip):
    result = os.popen(f'sudo docker run {image} python3 ./{script} {ip}').read()
    return result
def StartQueue():

    subprocess.call('python3 /home/azureuser/project/QueueHandler/queueHandler.py', shell=True)


#/***************************************************************
#*
#* Copyright (Wouter Weemaes, Safi Bouziane, Kamil Grielens, Robbe Willeme) - All rights reserved. 
#*
#* Unauthorized use, copy, modify, merge, publish, distribute, sublicense, 
#* and/or sell any parts of the software/source code is strictly prohibited.
#* Proprietary and confidential
#* License: No license. 
#* Written by: (Wouter Weemaes) (wouterweemaes@outlook.com), (06/2022)
#*
#****************************************************************/
