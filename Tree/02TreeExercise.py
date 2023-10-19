class TreeNode:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.children = []
        self.parent = None

    def add_child(self, children):
        self.children.append(children)
        children.parent = self

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, type="both"):
        if type.lower() == "name":
            level_prefix = "  " * self.get_level() + "|--" if self.parent else ""
            print(level_prefix+self.name)
            if self.children:
                for child in self.children:
                    child.print_tree(type)
        elif type.lower() == "position":
            level_prefix = "  " * self.get_level() + "|--" if self.parent else ""
            print(level_prefix+self.position)
            if self.children:
                for child in self.children:
                    child.print_tree(type)
        elif type.lower() == "both":
            level_prefix = "  " * self.get_level() + "|--" if self.parent else ""
            print(level_prefix+f"{self.name} ({self.position})")
            if self.children:
                for child in self.children:
                    child.print_tree(type)


def build_employee_tree():
    ceo = TreeNode("Dixanta Nath Shrestha", "CEO")
    cto = TreeNode("Ram Karki", "CTO")
    hr = TreeNode("Manish Thapa", "HR Head")

    ceo.add_child(cto)
    ceo.add_child(hr)

    infra_head = TreeNode("Jeeya Shrestha", "Infrastructure Head")
    app_head = TreeNode("Prizma Sharma", "Application Head")

    cto.add_child(infra_head)
    cto.add_child(app_head)

    cloud_manager = TreeNode("Neha Basnet", "Cloud Manager")
    network_manager = TreeNode("Riya Sharma", "Network Manager")

    infra_head.add_child(cloud_manager)
    infra_head.add_child(network_manager)

    recruitment_manager = TreeNode("Alisha Basnet", "Recruitment Manager")
    policy_manager = TreeNode("Aakash Bhandari", "Policy Manager")

    hr.add_child(recruitment_manager)
    hr.add_child(policy_manager)

    return ceo


if __name__ == '__main__':
    root_node = build_employee_tree()
    root_node.print_tree("name")  # prints only name hierarchy
    root_node.print_tree("position") # prints only position hierarchy
    root_node.print_tree("both") # prints both (name and designation) hierarchy
