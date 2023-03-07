from tree_json import tree
from os import system

def dfs ( startNode, searchId ) :
    print(f"visiting > {startNode['id']}")

    if startNode['id'] == searchId:
        return [startNode['id']]

    for child in startNode['children']:
        path = dfs(child, searchId)
        if path != None:
            return  path + [startNode['id']]

########   Main code ######################
system('cls')
path = dfs(tree[0], 'E')
print(f"path : {path}")
