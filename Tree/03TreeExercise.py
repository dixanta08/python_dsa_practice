class TreeNode:
    def __init__(self,location):
        self.location = location
        self.children = []
        self.parent = None

    def add_child(self,children):
        self.children.append(children)
        children.parent = self

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, level=5):
        if self.get_level() > level:
            return
        else:
            level_prefix = "  " * self.get_level() + "|--" if self.parent else ""
            print(level_prefix + self.location)
            if self.children:
                for child in self.children:
                    child.print_tree(level)

def build_location_tree():
    node_global = TreeNode("Global")

    india = TreeNode("India")
    usa = TreeNode("USA")

    node_global.add_child(india)
    node_global.add_child(usa)

    gujrat = TreeNode("Gujrat")
    karnatak = TreeNode("Karnataka")

    india.add_child(gujrat)
    india.add_child(karnatak)

    ahmedabad = TreeNode("Ahmedabad")
    baroda = TreeNode("Baroda")

    gujrat.add_child(ahmedabad)
    gujrat.add_child(baroda)

    bangluru = TreeNode("Bangluru")
    mysore = TreeNode("Mysore")

    karnatak.add_child(bangluru)
    karnatak.add_child(mysore)

    newjersey = TreeNode("New Jersey")
    california = TreeNode("California")

    usa.add_child(newjersey)
    usa.add_child(california)

    princeton = TreeNode("Princeton")
    tenton = TreeNode("Tenton")
    newjersey.add_child(princeton)
    newjersey.add_child(tenton)

    sanfrancisco = TreeNode("San Francisco")
    mountainview = TreeNode("Mountain View")
    paloalto = TreeNode("Palo alto")

    california.add_child(sanfrancisco)
    california.add_child(mountainview)
    california.add_child(paloalto)

    return node_global

if __name__ == "__main__":
    root = build_location_tree()
    root.print_tree(0)
    root.print_tree(1)
    root.print_tree(2)
    root.print_tree()

