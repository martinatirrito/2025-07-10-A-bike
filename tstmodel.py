from model.category import Category
from model.model import Model

mymdl = Model()

c = Category(7, "Electric Bikes")
mymdl.buildGraph(c)
n, e = mymdl.graphDetails()

print("N nodi:", n, "N archi", e)