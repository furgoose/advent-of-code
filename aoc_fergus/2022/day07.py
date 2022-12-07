from typing import Optional
from aocd import lines


class Node:
    def __init__(
        self,
        type: str,
        name: str,
        size: Optional[int] = None,
        parent: "Optional[Node]" = None,
    ):
        self.type = type
        self.name = name
        self.parent = parent
        self.children: dict[str, Node] = {}
        self._size = size

    def __repr__(self) -> str:
        return f"<Node type='{self.type}' name='{self.name}'>"

    def add(self, node: "Node"):
        self.children[node.name] = node

    def size(self):
        if self._size:
            return self._size
        return sum(node.size() for node in self.children.values())


root = Node("d", "/")
cwd = root
for line in lines:
    if line.startswith("$ "):
        command = line[2:].split()
        match command:
            case ["cd", "/"]:
                cwd = root
            case ["cd", ".."]:
                cwd = cwd.parent
            case ["cd", directory]:
                cwd = cwd.children[directory]
    elif line.startswith("dir "):
        directory = Node("d", line[4:], parent=cwd)
        cwd.add(directory)
    else:
        size, filename = line.split()
        file = Node("f", filename, size=int(size), parent=cwd)
        cwd.add(file)


def all_dirs():
    def children(node):
        child_nodes = []
        for n in node.children.values():
            child_nodes.extend(d for d in children(n) if d.type == "d")
        return [node, *child_nodes]

    return children(root)


print(
    "part a:",
    sum(size for node in all_dirs() if (size := node.size()) < 100000),
)

free_space = 70000000 - root.size()
needed = 30000000 - free_space

print("part b:", min(size for d in all_dirs() if (size := d.size()) >= needed))
