from __future__ import annotations
from typing import List
import json
import os

verbose = False

# The class for a particular Node in the tree.
# None-leaf nodes have:
#     value = None (the Python None)
#     branches = List of branches.
#                Each branch is an object with keys 'label' and 'child',
#                Here 'label' is the branch label.
#                Here 'child' points to the corresponding child Node.
# Leaf nodes have:
#     value = the value associated to that branch path.
#     branches = Empty list.
#
# Note: You do not need to sort the list of branches.  The dump function takes care of this for printing.
# DO NOT MODIFY!
class Node():
    def  __init__(self,
                  value      : int = None,
                  branches   : List[None] = None):
        self.value      = value
        self.branches   = branches

class Trie():
    def __init__(self,
                 root: Node = None):
         self.root = None

    # DO NOT MODIFY!
    def dump(self):
        def _to_dict(node) -> dict:
            st = []
            node.branches.sort(key=lambda x:x['label'])
            for b in node.branches:
                st.append({'label':b['label'],'child':_to_dict(b['child'])})
            return {
                "value"      : node.value,
                "branches"   : st
            }
        if self.root == None:
            dict_repr = {}
        else:
            dict_repr = _to_dict(self.root)
        print(json.dumps(dict_repr,indent = 2))

    def find_prefix(self, word, label):
        i = 1
        while word.startswith(label[:i]) and i <= len(label):
            i += 1
        return label[:(i-1)]
    
    def insert_aux(self, node, word, value):
        i = 0
        branch = node.branches[0]
        while not (prefix := self.find_prefix(word, branch["label"])) \
              and i < len(node.branches):
            branch = node.branches[i]
            i += 1

        if not prefix:
            node.branches.append({"label": word, "child": \
                    Node(None, [{"label": "$", "child": Node(value, [])}])})
        elif prefix == branch["label"]:
            self.insert_aux(branch["child"], word[len(prefix):], value)
        else:
            i = 1 if i == 0 else i
            branch1 = {"label": word[len(prefix):], "child":
                        Node(None, [{"label": "$", "child": Node(value, [])}])}
            branch2 = {"label": branch["label"][len(prefix):], "child":
                        branch["child"]}
            node.branches.pop(i - 1)
            node.branches.append({"label": prefix, "child": \
                    Node(None, [branch1, branch2])})
            
    def insert(self,word,value):
        # self.dump()
        # print(word)
        if not self.root:
            self.root = Node(None, [{"label": word, "child": \
                        Node(None, [{"label": "$", "child": Node(value, [])}])}])
        else:
            self.insert_aux(self.root, word, value)

    def delete_aux(self, node, parent, node_index, word, node_two_child, 
                   parent_two_child, index_node_two_child, index_two_child):
        if node.value:
            # print(index_node_two_child)
            # print(index_two_child)
            node_two_child.branches.pop(index_two_child)
            if len(node_two_child.branches) == 1:
                label = parent_two_child.branches[index_node_two_child]["label"] + \
                        node_two_child.branches[0]["label"]
                child = node_two_child.branches[0]["child"]

                parent_two_child.pop(index_node_two_child)
                parent_two_child.branches.append({"label": label, "child": child})
        else:
            i = 0
            branch = node.branches[0]
            while not (prefix := self.find_prefix(word, branch["label"])):
                i += 1
                branch = node.branches[i]

            if len(node.branches) > 1:
                node_two_child = node
                parent_two_child = parent
                index_node_two_child = node_index
                index_two_child = i
            
            self.delete_aux(branch["child"], node, i, word[len(prefix):],
                            node_two_child, parent_two_child,
                            index_node_two_child, index_two_child)

    # Delete the word and the associated value.
    def delete(self,word):
        self.delete_aux(self.root, None, None, word + "$", None, None, None, None)

    def search_aux(self, node, word):
        if node.value:
            print(node.value)
        else:
            i = 0
            branch = node.branches[0]
            while not (prefix := self.find_prefix(word, branch["label"])):
                branch = node.branches[i]
                i += 1

            self.search_aux(branch["child"], word[len(prefix):])

    # Search for the word and print the associated value.
    def search(self,word):
        self.search_aux(self.root, word + "$")
