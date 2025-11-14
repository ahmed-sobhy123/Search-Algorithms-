from queue import Queue as qu
def bfs(graph, start, goal):
    frontier=qu()
    frontier.put(start)
    
    explored_set=[]
    
    while not frontier.empty():
        curr=frontier.get()
        
        if curr == goal:
            print(f"{goal}\nThe goal {goal} is reached.")
            return True
        
        
        if curr not in explored_set:
            print(curr,end=" => ")
            explored_set.append(curr)
            
            for neighbour in graph[curr]:
                if neighbour not in explored_set:
                    frontier.put(neighbour)

graph = {
    "A": ["B"],
    "B": ["C", "D"],
    "C": ["E"],
    "E": ["G"],
    "G": [],
    "D": ["F"],
    "F": [],
}

start = "A"
goal = "E"

print("Visited order:",end=" ")
bfs(graph, start, goal)

