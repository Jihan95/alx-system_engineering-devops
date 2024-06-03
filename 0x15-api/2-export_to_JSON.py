#!/usr/bin/python3
""" using this a url, for a given employee ID,returns information about his/her
TODO list progress. and save information into json file """


import json
import requests
import sys


def main():
    """ main function """
    if sys.argv[1]:
        id = sys.argv[1]
        fixed = 'https://jsonplaceholder.typicode.com/'
        url = fixed + 'todos/?userId=' + sys.argv[1]
        url1 = fixed + 'users/?id=' + sys.argv[1]
        response = requests.get(url)
        user = requests.get(url1).json()[0]["username"]
        if response.status_code == 200:
            data = response.json()
            with open(f'{id}.json', 'w') as f:
                json_data = {
                        id: [
                            {
                                "task": i['title'],
                                "completed": i['completed'],
                                "username": user,
                                }
                            for i in data
                            ]
                        }
                json.dump(json_data, f)
    else:
        print('USAGE: 1-export_to_JSON.py EMPLOYEE_ID')


if __name__ == "__main__":
    main()
