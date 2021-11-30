from treelib import Node, Tree
tree = Tree()
tree.create_node("GrandParents","GrandParents") #root
tree.create_node("GrandPa","GrandPa",parent="GrandParents" )
tree.create_node("GrandMa","Grandma",parent="GrandParents" )
tree.create_node("Papa","Papa",parent="Grandma" )
tree.create_node("Mama","Mama",parent="Grandma" )
tree.show()
