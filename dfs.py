def dfs(graph,start,goal):
    frontier=[start]
    explored_set=[]
    
    while frontier:
        curr=frontier.pop()
        
        if curr == goal:
            print (f"{curr}\nThe goal {goal} is reached.")
            return True
        
        
        if curr not in explored_set:
            print(curr, end=" => ")
            explored_set.append(curr)
            
            for neighbour in graph[curr]:
                if neighbour not in explored_set:
                    frontier.append(neighbour)



graph={
    'A':['B'],
    'B':['C','D'],
    'C':['E'],
    'E':['G'],
    'G':[],
    'D':['F'],
    'F':[]
}

start='A'
goal='E'

dfs(graph,start,goal)