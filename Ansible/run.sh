#! /bin/sh
cd /home/master/master_software/ResultHandler/ && nohup uvicorn ResultHandler:app --host 0.0.0.0 --reload --port 9000 &
cd /home/master/master_software/api/app/ && nohup uvicorn main:app --host 0.0.0.0 --reload --port 8000 &
python3 /home/master/master_software/QueueHandler/master.py
