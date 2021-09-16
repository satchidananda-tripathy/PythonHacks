#Given a two dimensional list, for example [ [2,3],[3,4],[5]] person 2 is friends with 3 etc,
# find how many friends each person has. Note, one person has no friends

frnd_lst = [[2,3],[3,4],[5]]


for items in frnd_lst:
    if len(items)==2:
        print(f"Person {items[0]} has {items[1]} friends ")
    else:
        print(f"Friend {items[0]} has {0} friends")


