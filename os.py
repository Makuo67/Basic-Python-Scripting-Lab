import os 
import requests
import shutil
from datetime import datetime

# os.mkdir('Os_Module')
def download_file(url, local_file):
    response = requests.get(url)

    if response.status_code == 200:
        with open(local_file, "wb") as f:
            f.write(response.content)
        print("File downloaded successfully")
        return True
    else:
        print('File download error: ', response.status_code)
        return False

def directory_path(path):
    if not os.path.exists(path):
        os.mkdir(path)
        print(f'{path} directory created!')
    else:
        print(f'{path} directory already exists')

directory_path('/Users/Lenovo/Javascript Project/Os_Module')

def modify_file(file):
    filepath = os.rename(file, 'file.txt')

    user_input =  input("Describe what you have learned so far in a sentence: ")
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('file.txt', 'w') as f:
        f.write(user_input + '\n')
        f.write(f"Last modified on: {current_date}")

    print("File content modified successfully")

modify_file('file.txt')

def view_file(file):
    try:

        with open(file, 'r') as f:
            content = f.read()
            print("\nYou Entered: ", end=' ')
            print(content)
    except Exception as e:
        print(f'Error reading file: {e}')

view_file('file.txt')

url = 'https://github.com/Makuo67/resume/blob/master/README.md'
local_file = 'Makuo_Okeke'

# print(download_file(url, local_file))

