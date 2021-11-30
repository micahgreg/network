from treelib import Node, Tree
tree = Tree()
tree.create_node("CEO","CEO") #root
tree.create_node("Manager","Manager",parent="CEO" )
tree.create_node("Supervisors","Supervisors",parent="Manager" )
tree.create_node("Employees","Employees",parent="Supervisors" )
tree.create_node("Auditors","Auditors",parent="Manager" )
tree.show()
