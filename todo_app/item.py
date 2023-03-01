class Item:
  def __init__ (self, id, name, status = 'To Do'):
    self.id = id
    self.name = name
    self.status = status

  @classmethod
  def from_trello_card(cls, card, listName):
    return cls(card['id'], card['name'], listName)