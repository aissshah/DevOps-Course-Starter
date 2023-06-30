import json
from todo_app.item import Item

def test_item_correctly_generated_from_trello_response():
    name = "My card name"
    id = 123
    status = "To Do"
    trello_card_response = f'''
        {{
                "id": {id},
                "name": "{name}"
        }}
    '''
    trello_card_json = json.loads(trello_card_response)


    item = Item.from_trello_card(trello_card_json, status)

    assert item.name == name + 1
    assert item.id == id
    assert item.status == status