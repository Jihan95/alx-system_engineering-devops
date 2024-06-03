#!/usr/bin/python3
""" using this a url, for a given employee ID,returns information about his/her
TODO list progress. and save information into csv file """


import csv
import requests
import sys


def main():
    """ main function """
    if sys.argv[1]:
        fixed = 'https://jsonplaceholder.typicode.com/'
        url = fixed + 'todos/?userId=' + sys.argv[1]
        url1 = fixed + 'users/?id=' + sys.argv[1]
        response = requests.get(url)
        user = requests.get(url1).json()[0]["username"]
        if response.status_code == 200:
            data = response.json()
            with open(f'{sys.argv[1]}.csv', 'w', newline='') as f:
                for i in data:
                    row = f'"{sys.argv[1]}","{user}","{i["completed"]}",'
                    f.write(row + f'"{i["title"]}"\n')
    else:
        print('USAGE: 1-export_to_CSV.py EMPLOYEE_ID')


if __name__ == "__main__":
    main()
