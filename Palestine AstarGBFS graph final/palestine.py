# Asad Thafer Asad
# Kholoud Yazeed Thabet
import queue
import matplotlib.pyplot as plt

# getting heuristics from file
def getHeuristics():
    heuristics = {}
    f = open("heuristics.txt")
    for i in f.readlines():
        node_heuristic_val = i.split()
        heuristics[node_heuristic_val[0]] = int(node_heuristic_val[1])
    return heuristics


# getting cities location from file
def getCity():
    city = {}
    citiesCode = {}
    f = open("cities.txt")
    j = 1
    for i in f.readlines():
        node_city_val = i.split()
        city[node_city_val[0]] = [int(node_city_val[1]), int(node_city_val[2])]

        citiesCode[j] = node_city_val[0]
        j += 1

    return city, citiesCode


# creating cities graph from file
def createGraph():
    graph = {}
    file = open("citiesGraph.txt")
    for i in file.readlines():
        node_val = i.split()

        if node_val[0] in graph and node_val[1] in graph:
            c = graph.get(node_val[0])
            c.append([node_val[1], node_val[2]])
            graph.update({node_val[0]: c})

            c = graph.get(node_val[1])
            c.append([node_val[0], node_val[2]])
            graph.update({node_val[1]: c})

        elif node_val[0] in graph:
            c = graph.get(node_val[0])
            c.append([node_val[1], node_val[2]])
            graph.update({node_val[0]: c})

            graph[node_val[1]] = [[node_val[0], node_val[2]]]

        elif node_val[1] in graph:
            c = graph.get(node_val[1])
            c.append([node_val[0], node_val[2]])
            graph.update({node_val[1]: c})

            graph[node_val[0]] = [[node_val[1], node_val[2]]]

        else:
            graph[node_val[0]] = [[node_val[1], node_val[2]]]
            graph[node_val[1]] = [[node_val[0], node_val[2]]]

    return graph
    return cost


# Greedy Best First Search Algorithm
def GBFS(startNode, heuristics, graph, goalNode="Eilat"):
    priorityQueue = queue.PriorityQueue()
    distance = 0
    path = []

    priorityQueue.put((heuristics[startNode] , [startNode, 0]))

    while priorityQueue.empty() == False:
        current = priorityQueue.get()[1]
        path.append(current[0])
        distance += int(current[1])

        if current[0] == goalNode:
            break

        priorityQueue = queue.PriorityQueue()

        for i in graph[current[0]]:
            if i[0] not in path:
                priorityQueue.put((heuristics[i[0]] , i))
                
    
    global costGBFS
    costGBFS=distance
    return path


# Astar Algorithm
def Astar(startNode, heuristics, graph, goalNode="Eilat"):
    priorityQueue = queue.PriorityQueue()
    priorityQueue.put((heuristics[startNode], startNode))
    parent = {}
    dist = {}
   
    #parent -> parent[i] -> the node before me in the path from start_node to node i
    #dist - > dist[i] -> the distance from startnode to node i
   
   # i'm parent of me
    parent[startNode] = startNode
    # 0 to reach from startNode to startNode 
    dist[startNode] = 0
   
    while priorityQueue.empty() == False:
       current = priorityQueue.get()[1]
       if current == goalNode:
           break
       for i in graph[current]:         
           cur_dist = dist[current] + int(i[1])
           
           #cur_dist -> distance to reach node i[1] from start node 
           
           # if I didn't reach this node before or I have a better distance 
           if i[0] not in dist or cur_dist < dist[i[0]]:
               dist[i[0]] = cur_dist
               parent[i[0]] = current
               # g = dist[i[0]]
               # h = heuristics[i[0]]
               priorityQueue.put((dist[i[0]] + heuristics[i[0]], i[0]))
   
    global costAstar
    costAstar=dist[goalNode]

   
   #read the path using parent dic, and reverse the path since we take it from the end to start
   
    path = []
    while goalNode != startNode:
       path.append(goalNode)
       goalNode = parent[goalNode]
    path.append(startNode)
    path.reverse()

    return path	
    



# drawing map of answer
def drawMap(city, gbfs, astar, graph):
    plt.figure(figsize=(6, 16),clear=True,num='Palestine Map Search - By : Asad & Kholoud')
    for i, j in city.items():
        plt.plot(j[0], j[1], "ro")         # o     circle     r     red
        plt.annotate(i, (j[0] + 5, j[1])) 

        for k in graph[i]:
            n = city[k[0]]
            plt.plot([j[0], n[0]], [j[1], n[1]], "gray" )        #edit linewidth using ,linewidth=10

    for i in range(len(gbfs)):
        try:
            first = city[gbfs[i]]
            secend = city[gbfs[i + 1]]

            plt.plot([first[0], secend[0]], [first[1], secend[1]], "green")
        except:
            continue

    for i in range(len(astar)):
        try:
            first = city[astar[i]]
            secend = city[astar[i + 1]]

            plt.plot([first[0], secend[0]], [first[1], secend[1]], "blue")
        except:
            continue

    plt.errorbar(1, 1, label="GBFS", color="green")
    plt.errorbar(1, 1, label="ASTAR", color="blue")
    plt.legend(loc="lower left")
    plt.show()
    


# running the program
def main():
    heuristic = getHeuristics()
    graph = createGraph()
    city, citiesCode = getCity()

    for i, j in citiesCode.items():
        print(i, j)

    while True:
        inputCode = int(input("Please enter your desired city's number (0 for exit): "))

        if inputCode == 0:
            break

        cityName = citiesCode[inputCode]

        gbfs = GBFS(cityName, heuristic, graph)
        astar = Astar(cityName, heuristic, graph)
        print("GBFS => ", gbfs)
        print("Cost GBFS = ",costGBFS)
        print("ASTAR => ", astar)
        print("Cost ASTAR = ",costAstar)

        drawMap(city, gbfs, astar, graph)


main()
