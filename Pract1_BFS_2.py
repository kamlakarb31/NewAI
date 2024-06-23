from collections import deque

class MyGraph:
    def __init__(self, cmap, i, g):
        self.citymap = cmap
        self.init = i
        self.goal = g
    def goal_test(self,anode):
        if anode==self.goal:
            return True
        else:
            return False
    def getLinks(self, anode):
        return list(self.citymap[anode].keys())

def breadth_first_search(citygraph): # algorithm 3.11
    node = citygraph.init
    if citygraph.goal_test(node):
        return node
    frontier = deque([node])
    explored = set()
    while frontier:
        print("Frontier :", frontier)
        node = frontier.popleft()
        explored.add(node)
        for child in citygraph.getLinks(node):
            if child not in explored and child not in frontier:
                if citygraph.goal_test(child):
                    return child
                frontier.append(child)
    return None

cities = {'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
             'Bucharest': {'Urziceni': 85, 'Pitesti': 101, 'Giurgiu': 90, 'Fagaras': 211}, 
             'Craiova': {'Drobeta': 120, 'Rimnicu': 146, 'Pitesti': 138}, 
             'Drobeta': {'Mehadia': 75, 'Craiova': 120}, 
             'Eforie': {'Hirsova': 86}, 
             'Fagaras': {'Sibiu': 99, 'Bucharest': 211}, 
             'Hirsova': {'Urziceni': 98, 'Eforie': 86}, 
             'Iasi': {'Vaslui': 92, 'Neamt': 87}, 
             'Lugoj': {'Timisoara': 111, 'Mehadia': 70}, 
             'Oradea': {'Zerind': 71, 'Sibiu': 151}, 
             'Pitesti': {'Rimnicu': 97, 'Bucharest': 101, 'Craiova': 138}, 
             'Rimnicu': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97}, 
             'Urziceni': {'Vaslui': 142, 'Bucharest': 85, 'Hirsova': 98}, 
             'Zerind': {'Arad': 75, 'Oradea': 71}, 
             'Sibiu': {'Arad': 140, 'Fagaras': 99, 'Oradea': 151, 'Rimnicu': 80}, 
             'Timisoara': {'Arad': 118, 'Lugoj': 111}, 
             'Giurgiu': {'Bucharest': 90}, 
             'Mehadia': {'Drobeta': 75, 'Lugoj': 70}, 
             'Vaslui': {'Iasi': 92, 'Urziceni': 142}, 
             'Neamt': {'Iasi': 87}}
    


incities = MyGraph(cities, 'Arad','Bucharestt')
print("links of Arad :", incities.getLinks('Arad'))
finalnode = breadth_first_search(incities)

if(finalnode is not None):
    print("path exists")
else:
    print("path does not exist")


















'''cities  = {    
            'Jaipur':{'Mumbai':500, 'Nashik':650},
            'Mumbai': {'Jaipur':500, 'Pune' :150, 'Nashik':100, 'Ratnagiri':300},
            'Nashik': {'Jaipur':650, 'Mumbai':100, 'Pune':200},
            'Pune': {'Nashik':200, 'Mumbai':150, 'Ratnagiri':130},
            'Ratnagiri': {'Mumbai':300, 'Pune':130}    
        }
incities = MyGraph(cities, 'Jaipur','Ratnagirim') '''

