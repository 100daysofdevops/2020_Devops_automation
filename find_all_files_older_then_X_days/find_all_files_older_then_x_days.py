import os
import sys
import datetime


deletion_age=3

dir_path=input("Please enter the required path: ")

if not os.path.exists(dir_path):
    print("Please provide the valid path")
    sys.exit()

if os.path.isfile(dir_path):
    print("Please enter the directory")
    sys.exit()
today_date=datetime.datetime.now()

for file in os.listdir(dir_path):
    complete_path = os.path.join(dir_path,file)
    if os.path.isfile(complete_path):
        file_creation_date=datetime.datetime.fromtimestamp(os.path.getctime(complete_path))
        file_age_difference=(today_date - file_creation_date).days
        if file_age_difference > deletion_age:
            print(complete_path,)





