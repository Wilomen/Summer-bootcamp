height = int(input())
amount = int(input())
tree_height = int(input())

trees = 0
metres = height * amount

rashod = 0 # value for counting how many stacks we can get from one tree
while True:
    if tree_height - height >= 0:
        rashod += height
        tree_height -= height
    else:
        break

while True:
    if metres >= rashod:      # 50 AND 20 WHEN ONLY 10 METRES LEFT - ???
        metres -= rashod
        trees += 1
    elif metres == 0:
        break
    else:
        trees += 1
        break

print(trees)