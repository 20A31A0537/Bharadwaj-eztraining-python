graph ={
    '5' :['3','7'],
    '3' :['2','4'],
    '7' :['8'],
    '2' :[],
    '4' :['8'],
    '8' :[]
}

#bfs-we use Queue
visited=[] #list for visted nodes
queue=[]

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)

    while queue:
        m=queue.pop(0)
        print (m,end="")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

bfs(visited, graph, '5')
