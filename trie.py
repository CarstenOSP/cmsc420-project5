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

    def insert(self,word,value):
        print("This is space-filler just so it runs. Delete this when you fill in the code.")


    # Delete the word and the associated value.
    def delete(self,word):
        print("This is space-filler just so it runs. Delete this when you fill in the code.")

    # Search for the word and print the associated value.
    def search(self,word):
        print("Replace this so the value is printed instead!")