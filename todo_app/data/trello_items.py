import requests
import os

auth = {
      'key': os.getenv('TRELLO_KEY'), 
      'token': os.getenv('TRELLO_token'),
    }

def get_items():
    response = requests.get('https://trello.com/1/boards/{board}/cards'.format(board=os.getenv('TRELLO_BOARD')), params=auth)
    return response.json()

def add_item(title):
    boardLists = get_lists()
    todoBoardIndex = find_todo_list(boardLists)
    newParams = dict(auth)
    newParams.update(idList=boardLists[todoBoardIndex]["id"], name=title)
    response = requests.post('https://trello.com/1/cards', params=newParams)
    return response.json()

def update_item_status(item):
    return ''

def get_lists():
    response = requests.get('https://trello.com/1/boards/{board}/lists'.format(board=os.getenv('TRELLO_BOARD')), params=auth)# why is it getting 400 bad request???
    print(response.status_code, response.reason)
    return response.json()

def find_todo_list(boardList):
    for index, item in enumerate(boardList):
        if item['name'] == 'To Do':
            return index
    return 0