import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.DiGraph()
        self._products = []
        self._idMapP = {}



    def buildGraph(self, cat, date1, date2):
        self._graph.clear()
        self._products = DAO.getProductsByCategory(cat)
        for p in self._products:
            self._idMapP[p.product_id] = p

        self._graph.add_nodes_from(self._products)

        allEdges = DAO.getAllEdges(cat, date1, date2, self._idMapP)
        for a in allEdges:
            self._graph.add_edge(a.p1, a.p2, weight = a.peso)

    def graphDetails(self):
        return len(self._graph.nodes), len(self._graph.edges)

    def getNodiPiuProfittevoli(self):
        #deve per ogni nodo associare la somma dei pesi uscenti meno la somma dei pesi entranti
        listNodesPesata = []
        for n in self._graph.nodes:
            score = 0
            for a in self._graph.out_edges(n, data = True): #arco uscente  #data = true : dammi gli attributi
                score += a[2]["weight"] #il peso perchè è una tupla
            for a in self._graph.in_edges(n, data = True): #entranti
                score -= a[2]["weight"]
            listNodesPesata.append((n, score))

        listNodesPesata.sort(key = lambda x: x[1], reverse = True)

        return listNodesPesata[0:5]




    def getDateRange(self):
        return DAO.getDateRange()

    def getCategories(self):
        return DAO.getCategories()


