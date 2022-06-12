#! /bin/sh
cd /home/master/master_software/ResultHandler/ && nohup uvicorn ResultHandler:app --host 0.0.0.0 --reload --port 9000 &
cd /home/master/master_software/api/app/ && nohup uvicorn main:app --host 0.0.0.0 --reload --port 8000 &
cd /home/master/master_software/QueueHandler/ && nohup python3 master.py &


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
