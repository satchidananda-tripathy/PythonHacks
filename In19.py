#Count the neighbors of each node in a graph. Input graph is a multi dimensional list
#input (list of list): [[A, B], [B, C], [B, D], [E]],
#output (dict): {A:1, B: 3, C:1, D:1, E:0}
#assume you won't get a repeat pair like [A,B] and [B,A], and neither will there be more than 2 people in a relationship.

graph =[['A','B'], ['B', 'C'], ['B', 'D'], ['E']]
list_node=[]
output ={}
for nodes in graph:
    if len(nodes)==1:
        output[nodes[0]]=0 # Add the items whose occurance is just once into the dictionary
        graph.remove(nodes)

for x,y in graph:
    list_node.append(x)
    list_node.append(y)

def count_nodes(lst):

    for items in lst:
        if items in output:
            output[items]=output[items]+1
        else:
            output[items]=1
    return output

print(count_nodes(list_node))
## Method 2
friends = [['A','B'], ['B', 'C'], ['B', 'D'], ['E'],['F']]
# Here E and F has zero friends where B has 3 friends.
friend_ge_1 =[]
frnd_cnt ={}
for friend in friends :
    if len(friend)==1:
        frnd_cnt[friend[0]]=0
    else:
        friend_ge_1.append(friend[0])
        friend_ge_1.append(friend[1])
for f in friend_ge_1:
    if f in frnd_cnt:
        frnd_cnt[f] +=1
    else:
        frnd_cnt[f] =1

print(frnd_cnt)


