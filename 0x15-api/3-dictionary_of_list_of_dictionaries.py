#!/usr/bin/python3
""" using this a url, for a given employee ID,returns information about his/her
TODO list progress. and save information into json file """


import json
import requests
import sys


def main():
    """ main function """
    ids = range(1, 11)
    fixed = 'https://jsonplaceholder.typicode.com/'
    all_users_data = {}
    for id in ids:
        url_todo = fixed + 'todos/?userId=' + str(id)
        url_u = fixed + 'users/?id=' + str(id)
        response_todo = requests.get(url_todo)
        user = requests.get(url_u).json()[0]["username"]
        todos = response_todo.json()
        user_tasks = []
        for todo in todos:
            task_info = {
                    "task": todo['title'],
                    "completed": todo['completed'],
                    "username": user
                    }
            user_tasks.append(task_info)
        all_users_data[id] = user_tasks
    with open('todo_all_employees.json', 'w') as f:
        json.dump(all_users_data, f)


if __name__ == "__main__":
    main()
