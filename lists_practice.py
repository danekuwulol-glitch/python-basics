"""
Lists Practice - Solutions
Author: Danil
Date: 13.12.2025 (RU)
"""
def demonstrate_lists_methods():
  """Shows all list methods I've learned"""

  # 1. Creating and modifying
  fruits = ['banana', 'apple', 'pineapple', 'kiwi'] # new list
  vegetables = ['carrot', 'potatoes', 'cucumbers', 'garlic']
  # 1.1 Adding
  fruits.append('melon') # adding new fruit
  fruits.extend(vegetables) # adding list
  fruits.insert(0, 'watermelon') # adding new fruit at index (0 - first)
  # 1.2 Deleting
  fruits.pop() # deleting last element
  fruits.pop(1) # deleting second element
  fruits.remove('pineapple') # deleting first element with same value
  fruits.clear() # deleting all

  # 2. Searching
  tech = ['pc', 'mobile', 'ps'] # new list
  tech_index = tech.index('pc') # searching and return first element with same value
  tech_count = tech.count('mobile') # searching and return quantity of same value

  # 3. Sorting
  data = [1, 3, 66, 2] # new list
  data.sort() # sorting list but changes himself
  data2 = [1, 4, 77, 3] # new list
  sorted_data2 = sorted(data2) # make new sorted list ( save first) 
  data2.sort(reverse=True) # sort and reversing
  list1 = ['1', '11', '3', '2']
  list1.sort(key=int) # sorting strings likes num
  list1.sort(key=len) # sorting on length 
  list1.sort(key=str) # sorting like string

  # 4. Reverse
  items = ['chair', 'table', 'sofa', 'toy'] # new list
  items.reverse() # reverse list and changes him
  items_reversed = list(reversed(items)) # make copy of items and reverve him (don't changes original) ( first way )
  for num in reversed(items): # cycle ( second way )
    print(num, end=' ') # printing with add end

  # You can also reverse with cross:
  items_revers = items[::-1] # don't changes original too

  # 5. Copies
  Originals = [1, 6, 3, 10] # new list
  originals_cop1 = Originals # it's link on originals, not copy
  originals_cop1[0] = 111 # changes both
  # The true way
  originals_cop2 = Originals.copy() # make new copy
  originals_cop2[0] = 111
  # OR with cross
  originals_cop3 = Originals[:]
  originals_cop3[0] = 111




Commit directly to the main branch
Commit message: "Add lists practice with methods demonstration"

  
  
  
    
