#!/usr/bin/env python

class TrieTree(object):
    def __init__(self):
        self.root = _TrieNode('')
    
    def __getitem__(self,key):
        result = self.root.find(key)
        if result == None:
            raise KeyError
        else:
            return result
    
    def __setitem__(self,key,data):
        self.root.add_child(key,data)
    
    def __delitem__(self,key):
        self.root.delete(key)
        
    def __contains__(self,key):
        result = self.root.find(key)
        if result == None:
            return False
        return True
    
        

class _TrieNode(object):
    def __init__(self,key):
        self.key = key
        self.data = None
        self.children = list()
    
    def add_child(self,key,data):
        if key == "":
            self.data = data
            return
        
        for child in self.children:
            if child.key == key[:1:]:
                child.add_child(key[1::],data)
                return
        
        t=_TrieNode(key[:1:])
        self.children.append(t)
        t.add_child(key[1::],data)
        
        
        

    def find(self,key):
        if key == "":
            return self.data
        
        else:
            for child in self.children:
                if child.key == key[:1:]:
                    return child.find(key[1::])
            return None
    
    #returns true if the node can be destroyed, false otherwise
    def delete(self,key):
        if key == "":
            return True
        
        for child in self.children:
            if child.key == key[:1:]:
                if child.delete(key[1::]):
                    del(self.children[self.children.index(child)])
                    if self.children == []:
                        return True
        
        return False

class BplusTree(object):
    def __init__(self,node_loading=4):
        self.root = _BplusRoot(node_loading)
    
    def __setitem__(self,key,data):
        pass
    
    def __getitem__(self,key):
        pass
    
    def __delitem__(self,key):
        pass
    
    def __contains__(self,key):
        pass

class _BplusRoot(object):
    def __init__(self,loading):
        self.limit=loading
        self.nodes = []
        self.node_starts = []
        self.add_item = self.add_item_single
    

    def add_item(self,key,data):
        pass
    
    def add_item_single(self,key,data):
        if len(self.nodes) == self.limit:
            node_one = _BplusNode(self.limit,self)
            node_two = _BplusNode(self.limit,self)
            
            s_l = self.limit / 2
            node_one.items = self.nodes[s_l::]
            node_two.items = self.nodes[:s_l:]
            node_one.item_data = self.node_starts[s_l::]
            node_two.item_data = self.node_starts[:s_l:]
            
            self.node_starts = [node_two.items[0]]
            self.nodes = [node_one,node_two]
            
            self.add_item = self.add_item_multi
            self.add_item(key,data)
            
        else:
            pass
    
    def add_item_multi(self,key,data):
        pass
    
    def new_node(self,new_node,old_node_start):
        if len(self.node_starts) == self.limit:
            pass
        else:
            self.node_starts.insert(self.node_starts.index(old_node_start)+1,new_node.items[0])
            self.nodes.insert(self.node_starts.index(old_node_start)+1,new_node)
            
    
    def change_start(self,new,old):
        pass

class _BplusNode(object):
    def __init__(self,loading,parent,leaf=True):
        self.limit = loading
        self.items = list()
        self.parent = parent
        self.item_data = list()
        self.leaf = leaf
    
    def add_item(self,key,data):
        if self.leaf:
            if key < self.items[0]:
                self.items.insert(0,key)
                self.item_data.insert(0,data)
                self.parent.change_start(self.items[0],self,items[1])
            for i in range(1,len(self.items)):
                if key < self.items[i]:
                    self.items.insert(i,key)
                    self.item_data.insert(i,data)
                    if len(self.items) > self.limit:
                        self.split()
                    return
                elif key == self.items[i]:
                    self.item_data[i]=data
            self.items.append(key)
            self.item_data.append(data)
            if len(self.items) > self.limit:
                self.split()
        
        else:
            for i in range(0,len(self.items)):
                if key < self.items[i]:
                    self.item_data[i].add_item(data)
                    return
            self.item_data[len(self.items)].add_item(data)
    
    def split(self):
        split_level = self.limit / 2
        new_node = _BplusNode(self.limit,self.parent)
        new_node.items = self.items[split_level::]
        new_node.item_data = self.item_data[split_level::]
        self.items = self.items[:split_level:]
        self.item_data = self.item_data[:split_level:]
        
        self.parent.new_node(new_node,self.items[0])
    
    def new_node(self,new_node,brother):
        self.items.insert(self.items.index(brother)+1,new_node.items[0])
        self.item_data.insert(self.items.index(brother)+1,new_node)
        if len(self.items) > self.limit:
            newer_node = _BplusNode(self.limit,self.parent,False)
            split_level = self.limit / 2
            newer_node.items = self.items[split_level::]
            newer_node.item_data = self.item_data[split_level::]
            self.items = self.items[:split_level:]
            self.item_data = self.item_data[:split_level:]
            
            self.parent.new_node(newer_node,self.items[0])
        

    def change_start(self,new,old):
        self.items[self.items.index(old)]=new
        if self.items.index(new)==0:
            self.parent.change_start(new,old)

class RebBlackTree(object):
    pass

def trie_tree_test():
    print "Beginning Trie Tree Test"
    trie = TrieTree()
    trie['test']="Hello"
    print trie['test']
    trie['test']="World"
    print trie['test']
    del(trie['test'])
    try:
        print trie['test']
    except KeyError:
        print "KeyError"

def b_tree_test():
    pass
if __name__ == '__main__':
    trie_tree_test()
    b_tree_test()