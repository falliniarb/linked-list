class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def insert(start, data):
  llt1 = Node(data)
  llt1.next = start
  return llt1

def printList(n):
  while n:
    print(n.data, end=" ")
    n = n.next
  print()

def swap(llt1, llt2):
  temp = llt2.data
  llt2.data = llt1.data
  llt1.data = temp

def bubbleSort(head):
  swapped = True
  while swapped:
    swapped = False
    current = head
    while current.next:
      if current.data > current.next.data:
        swap(current, current.next)
        swapped = True
      current = current.next

def search(head, x):
  current = head
  while current:
    if current.data == x:
      return True
    current = current.next
  return False

if __name__ == '__main__':
  arr = [7, 8, 4, 3, 9, 2,6,0,1]
  head = None
  for i in range(len(arr) - 1, -1, -1):
    head = insert(head, arr[i])

  bubbleSort(head)
  printList(head)

  x = int(input("Enter the element to search: "))
  if search(head, x):
    print("Element present")
  else:
    print("Element not present")
