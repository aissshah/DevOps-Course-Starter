import requests
import os

from todo_app.item import Item

def get_auth():
    return {
        'key': os.getenv('TRELLO_KEY'),
        'token': os.getenv('TRELLO_TOKEN'),
    }

def get_items():
    response = requests.get('https://trello.com/1/boards/{board}/lists?cards=open'.format(board=os.getenv('TRELLO_BOARD')), params=get_auth())
    lists = response.json()
    items = []
    for a_list in lists:
        for card in a_list['cards']:
            item = Item.from_trello_card(card, a_list['name'])
            items.append(item)
    return items

def add_item(title):
    boardLists = get_lists()
    todoBoardIndex = find_list_by_name('To Do', boardLists)
    newParams = dict(get_auth())
    newParams.update(idList=boardLists[todoBoardIndex]["id"], name=title)
    response = requests.post('https://trello.com/1/cards', params=newParams)
    return response.json()

def get_lists():
    response = requests.get('https://trello.com/1/boards/{board}/lists'.format(board=os.getenv('TRELLO_BOARD')), params=get_auth())
    return response.json()

def find_list_by_name(listName, boardList):
    for index, item in enumerate(boardList):
        if item['name'] == listName:
            return index
    return 0

def changeList_item(listName, itemID):
    boardLists = get_lists()
    doneListID = find_list_by_name(listName, boardLists)
    newParams = dict(get_auth())
    newParams.update(idList=boardLists[doneListID]["id"])
    response = requests.put('https://trello.com/1/cards/{itemID}'.format(itemID=itemID), params=newParams)
    return response
