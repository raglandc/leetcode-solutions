'''
Creating a book class
'''

CHARS_PER_PAGE = 62

class User:
  def __init__(self, id, name):
    self.id = id
    self.name = name
    self.books = Library()


class Book:
  def __init__(self, id, auth, title, content):
    self.id = id
    self.author = auth
    self.title = title
    self.content = content
    self.pages = len(content) // CHARS_PER_PAGE 
    self.current_page = 0
  
  def next_page(self):
    if self.current_page + 1 < self.pages:
      self.current_page += 1
    return 
  
  def prev_page(self):
    if self.current_page > 0:
      self.current_page -= 1
    return
  
  def display_page(self):
    content_range = len(self.content)
    start = self.current_page * CHARS_PER_PAGE 
    end = self.current_page * CHARS_PER_PAGE + CHARS_PER_PAGE
    if start >= content_range or end >= content_range:
      return
    print(f"Current Page: {self.current_page}")
    print(self.content[start:end])
    return


class Library:
  def __init__(self):
    self.items = {}

  def add_item(self, item):
    item_id = item.id
    if item_id not in self.items:
      self.items[item_id] =item 
      print("Successfully added to library")
    return
  
  def remove_item(self, item_id):
    if item_id in self.items:
      del self.books[item_id]
    return 
  
  def get_item(self, item_id):
    if item_id in self.items:
      return self.books[item_id]
    return None
  

if __name__ == '__main__':
  # Create book
  book1 = Book(0, 'Chris Ragland', 'Leet coders', 'Late Thursday into Friday, reports began to emerge of IT problems wherein Windows computers were getting stuck with the infamous “blue screen of death” — a bright blue error screen with a message that displays when Windows encounters a critical failure, crashes or cannot load. The outages were first noticed in Australia early on Friday, and reports quickly came in from the rest of Asia and Europe as the regions began their day, as well as the United States. Within a short time, CrowdStrike confirmed that a software update for Falcon had malfunctioned and was causing Windows computers that had the software installed to crash. Falcon lets CrowdStrike remotely analyze and check for malicious threats and malware on installed computers.')

  # Create user
  user = User(0, 'Christopher')
  user.books.add_item(book1)

  # Reading book 1
  book1.display_page()
  book1.next_page()
  book1.display_page()
  book1.next_page()
  book1.display_page()
  book1.prev_page()
  book1.display_page()






  
