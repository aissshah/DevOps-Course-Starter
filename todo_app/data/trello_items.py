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
    todoBoardIndex = find_list_by_name('To Do', boardLists)
    newParams = dict(auth)
    newParams.update(idList=boardLists[todoBoardIndex]["id"], name=title)
    response = requests.post('https://trello.com/1/cards', params=newParams)
    return response.json()

def update_item_status(item):
    return ''

def get_lists():
    response = requests.get('https://trello.com/1/boards/{board}/lists'.format(board=os.getenv('TRELLO_BOARD')), params=auth)
    print(response.status_code, response.reason)
    return response.json()

def find_list_by_name(listName, boardList):
    for index, item in enumerate(boardList):
        if item['name'] == listName:
            return index
    return 0

def changeList_item(listName, itemID):
    boardLists = get_lists()
    doneListID = find_list_by_name(listName, boardLists)
    newParams = dict(auth)
    newParams.update(idList=boardLists[doneListID]["id"])
    response = requests.put('https://trello.com/1/cards/{itemID}'.format(itemID=itemID), params=newParams)
    return response
