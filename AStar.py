from pyamaze import maze,agent,textLabel,COLOR
from queue import PriorityQueue

def AStar(m):
    OPEN = PriorityQueue()
    CLOSED = []

    goal = (1,1)
    initial = (m.rows, m.cols)

    g = {initial: 0}
    h_cost = m.rows+m.cols - initial[0] - initial [1]
    h = {initial: h_cost}
    f = {initial: g[initial]+h[initial]}
    
    OPEN.put((f[initial],initial))
    parent ={}

    while(OPEN.empty()!=True):

        
        current = OPEN.get()
        CLOSED.append(current[1])

        if(current[1] == (goal[0], goal[1])):
            break
            
        else:
            y = current[1]
            for x in m.maze_map[y[0], y[1]]:
                if(x=='E'):
                    node = (y[0], y[1]+1)
                if(x=='W'):
                    node = (y[0], y[1]-1)
                if(x=='N'):
                    node = (y[0]-1, y[1])
                if(x=='S'):
                    node = (y[0]+1, y[1])


                if(m.maze_map[y[0], y[1]][x]!=0 and node not in CLOSED):
                    g_temp = y[0]+y[1] - node[0] - node[1]
                    h_temp = node[0] + node[1] - goal[0] - goal[1]
                    f_temp = g_temp + h_temp

                    if(f_temp < f.get(node, float('inf')) or not any(node in item for item in OPEN.queue)):
                        
                        
                        g[node] = g_temp
                        h[node] = h_temp
                        f[node] = f_temp
                        parent[node]= (y[0], y[1])                     
                        if(not any(node in item for item in OPEN.queue)):
                            OPEN.put((f[node], node))

                   
    path={}
    goal=(1,1)
    start = (50,50)
    while goal!=start:
        path[parent[goal]]=goal
        goal=parent[goal]

    return path



if __name__=='__main__':
    m=maze(50,50)
    m.CreateMaze(theme=COLOR.light)
    path=AStar(m)
    ## Animate the solution
    a=agent(m,filled=True,footprints=True)
    m.tracePath({a:path},delay=10)
    l=textLabel(m,'A* path length',len(path)+1)
    m.run()  