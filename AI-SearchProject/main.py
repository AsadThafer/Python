with open('ff.txt','r') as f:
    matrix = [[int(num) for num in line.split(',')] for line in f]
    

with open('heuristics.txt','r') as h:
    heu = [[int(num) for num in line.split(',')] for line in h]

rows=len(matrix)
cols=len(matrix[0])

def alp(x):
    dict ={
        0:"Safed",
        1:"Eilat",
        2:"Acre",
        3:"Nazareth",
        4:"Tiberias",
        5:"Tulkarm",
        6:"Haifa",
        7:"Hadera",
        8:"Nablus",
        9:"Ramallah",
        10:"Jerusalem",
        11:"Bethlehem",
        12:"Jericho",
        13:"Jenin",
        14:"Jaffa",
        15:"Hebron",
        16:"Rafah",
        17:"Gaza",
        18:"Beersheba",
    }
    return(dict[x])

def returnalpha(p):
    dict ={
        0:"Safed",
        1:"Eilat",
        2:"Acre",
        3:"Nazareth",
        4:"Tiberias",
        5:"Tulkarm",
        6:"Haifa",
        7:"Hadera",
        8:"Nablus",
        9:"Ramallah",
        10:"Jerusalem",
        11:"Bethlehem",
        12:"Jericho",
        13:"Jenin",
        14:"Jaffa",
        15:"Hebron",
        16:"Rafah",
        17:"Gaza",
        18:"Beersheba",
    }
    pp=[]
    for rr in range(len(p)):
        pp.append(dict[p[rr]])
    return pp

def takeSecond(elem):
    return elem[1]


def returncost(pp,ss,gg):
    pathh=[gg]
    while gg!=ss:
        gg=pp[gg]
        pathh.insert(0,gg)
    costt=0
    for t in range(len(pathh)):
        try:
            costt+=matrix[pathh[t]][pathh[t+1]]
        except:
            pass
    
    return costt

def calculatepathcost(p):
    cost=0
    for i in range(len(p)):
        try:
            cost+=matrix[p[i]][p[i+1]]
        except:
            pass
    
    print("Path cost : ",cost)
    return cost

def printpath(p,s,g):
    k=0
    src=s
    gl=g
    path=[g]
    while g!=s:
        g=p[g]
        path.insert(0,g)
    print("Path from ",alp(src)," to ",alp(gl),"    : ",returnalpha(path))
    k=calculatepathcost(path)
    return k


def bfs(source,goal):
    bfscost=0
    parent = {}
    visited = []
    queue = []
    flag=0
    queue.append(source)
    visited.append(source)
    while queue:
        i=queue[0]
        x=0
        for x in range (cols):
            if matrix[i][x] != 0 and x not in visited:  
                visited.append(x)
                queue.append(x)
                bfscost+=matrix[i][x]
                parent[x]=i

            if goal in visited:
                flag=1
                break

        if flag==1:
            break    

        queue.pop(0)

    print("********** Breadth First Search **********")
    print ("Path traversed : ",returnalpha(visited))
    global bp
    bp=printpath(parent,source,goal)

def UniformCostSearch(source,goal):
    print("********** Uniform Cost Search **********")
    ucs=[]
    parent = {}
    visited = []
    queue = []
    queue.append((source,0))
    visited.append(source)
    while queue:
        goalcost=0
        i=queue[0][0]
        x=0
        bfscost=0
        ucs.append(i)
        for x in range (cols):
            if matrix[i][x] != 0 and x not in visited:
                visited.append(x)
                parent[x]=i
                bfscost=returncost(parent,source,x)
                queue.append((x,bfscost))
            if goal in visited:
                if goalcost>=bfscost:
                    goalcost=bfscost
                    # ucs.pop()
                    # ucs.append(x)
                    queue.pop()
                    visited.pop()
                break
        
        queue.sort(key=takeSecond)    
        queue.pop(0)
    print ("Path traversed : ",returnalpha(ucs))
    global upp
    upp=printpath(parent,source,goal)


def GreedyBFS(source,goal):
    print("********** Greedy Best First Search **********")
    ucs=[]
    flag=0
    parent = {}
    visited = []
    queue = []
    queue.append((source,heu[source]))
    visited.append(source)
    while queue:
        i=queue[0][0]
        x=0
        ucs.append(i)
        for x in range (cols):
            if matrix[i][x] != 0 and x not in visited:
                visited.append(x)
                parent[x]=i
                queue.append((x,heu[x]))
            if goal in visited:
                flag=1
                break
        
        if flag==1:
            break

        queue.pop(0)
        queue.sort(key=takeSecond)    
    # print ("Path traversed : ",ucs)
    global gp
    gp=printpath(parent,source,goal)

print("\n")
bfs(0,1)
print("\n")
UniformCostSearch(0,1)
print("\n")
GreedyBFS(0,1)
print("\n")
print("******** Path Cost in Ascending order obtained from : ")
numbers = [upp,bp,gp]
numbers.sort()
for r in range(len(numbers)):
    if (numbers[r]==upp):
        print("Uniform Cost Search : ",numbers[r])
        upp="-"
    elif (numbers[r]==bp):
        print("Breadth First Search : ",numbers[r])
        bp="-"
    elif (numbers[r]==gp):
        print("Greedy Best First Search : ",numbers[r])
        gp="-"