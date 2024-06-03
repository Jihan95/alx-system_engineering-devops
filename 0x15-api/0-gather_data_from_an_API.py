#!/usr/bin/python3
""" using this a url, for a given employee ID,returns information about his/her
TODO list progress. """


import requests
import sys

if __name__ == '__main__':
    if sys.argv[1]:
        fixed = 'https://jsonplaceholder.typicode.com/'
        url = fixed + 'todos/?userId=' + sys.argv[1]
        url1 = fixed + 'users/?id=' + sys.argv[1]
        response = requests.get(url)
        completed_tasks = []
        emp_name = requests.get(url1).json()[0]["name"]
        if response.status_code == 200:
            data = response.json()
            tot_tasks = len(data)
            for item in data:
                if item['completed'] is True:
                    completed_tasks.append(item['title'])
            n = len(completed_tasks)
            print(f"Employee {emp_name} is done with tasks({n}/{tot_tasks}):")
            for task in completed_tasks:
                print(f"\t {task}")
    else:
        print('USAGE: 0-gather_data_from_an_API.py EMPLOYEE_ID')
