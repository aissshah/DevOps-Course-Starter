import requests
import os

from todo_app.item import Item

auth = {
      'key': os.getenv('TRELLO_KEY'), 
      'token': os.getenv('TRELLO_TOKEN'),
    }

def get_items():
    response = requests.get('https://trello.com/1/boards/{board}/cards'.format(board=os.getenv('TRELLO_BOARD')), params=auth)
    cards = response.json()
    items = []
    for card in cards:
        item = Item.from_trello_card(card, map_list_id_to_name(card['idList']))
        items.append(item)
    return items

def map_list_id_to_name(listID):
    lists = get_lists()
    for list in lists:
        if listID == list['id']:
            return list['name']
    return ''

def add_item(title):
    boardLists = get_lists()
    todoBoardIndex = find_list_by_name('To Do', boardLists)
    newParams = dict(auth)
    newParams.update(idList=boardLists[todoBoardIndex]["id"], name=title)
    response = requests.post('https://trello.com/1/cards', params=newParams)
    return response.json()

def get_lists():
    response = requests.get('https://trello.com/1/boards/{board}/lists'.format(board=os.getenv('TRELLO_BOARD')), params=auth)
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
