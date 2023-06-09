from hashlib import sha256

class ConsistentHashing:

    def __init__(self, nodes):
        self.nodes = nodes
        self.hash_ring = {}

        for node in self.nodes:
            self.hash_ring[hash(sha256(node.encode()))] = node

    def get_node(self, key):
        hash_value = hash(sha256(key.encode()))

        for node in self.hash_ring:
            if hash_value < node:
                return self.hash_ring[node]

        return self.hash_ring[list(self.hash_ring.keys())[0]]

    def add_node(self, new_node):
        self.nodes.append(new_node)
        self.hash_ring[hash(sha256(new_node.encode()))] = new_node
    

nodes = ["node1", "node2", "node3"]
hashing = ConsistentHashing(nodes)


key = "key1"
node = hashing.get_node(key)
print(node)

new_node = "node4"
hashing.add_node(new_node)

key = "key1"
node = hashing.get_node(key)
print(node)

