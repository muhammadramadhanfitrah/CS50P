list_item = {}

while True:
     try:
          item = input().strip().upper()
     except EOFError:
          print()
          break
     if item in list_item:
          list_item[item] += 1
     else:
          list_item[item] = 1

for i in sorted(list_item.keys()):
     print(list_item[i], i)
