#!/usr/bin/env python

import collections,sys

Activity = collections.namedtuple("Activity",'name,calories')
def gen_search_arrays(activity_list):
    active = []
    for activity in activity_list:
        activity_name, activity_weight = activity.split(' ')
        active.append(Activity(activity_name,activity_weight))
    return active
    
class Blobular(object):
    '''
    Blobular: a class that can match items against other items
    with the goal that the weight of item subsets matching the
    goal weight. It is assumed that weights are additive, that
    is the weight of a and b is the same as the weight of a and
    the weight of b added together.
    '''
    def __init__(self,item_list,weight_function):
        self.positive_items = []
        self.negative_items = []
        for item in item_list:
            if weight_function(item) > 0:
                self.positive_items.append(item)
            else:
                self.negative_items.append(item)
        if len(self.positive_items)==0 or len(self.negative_items)==0:
            print "no solution"
            exit(0)
        
        self.weighter = weight_function
        self.active_positives=[]
        self.active_negatives=[]
        self.first_blob=False
        self.negative_scores=dict()
        self.positive_scores=dict()
        self.new_positives=dict()
        self.new_negatives=dict()
    
    def blob(self):
        if not self.first_blob:
            self._first_blob()
        else:
            self._reblob()
        return self._check_and_update_options()
    
    def _first_blob(self):
        for i in range(0,len(self.positive_items)):
            self.active_positives.append(([i]))
            self.new_positives[self.weighter(self.positive_items[i])]=[i]
        
        for i in range(0,len(self.negative_items)):
            self.active_negatives.append(([i]))
            self.new_negatives[self.weighter(self.negative_items[i])]=[i]
        
        self.first_blob=True
            
    
    def _reblob(self):
        if len(self.active_positives)!=1:
            self.active_positives.pop()
            for i in range(0,len(self.active_positives)):
                to_be_expanded = self.active_positives.pop(0)
                for i in range(max(to_be_expanded),len(self.positive_items)):
                    self.active_positives.append(to_be_expanded+[i])
                    self.new_positives[reduce(lambda x,y:x+self.weighter(self.positive_items[y]),to_be_expanded+[i],0)]=to_be_expanded+[i]

        
        if len(self.active_negatives)!=1:
            self.active_negatives.pop()
            for i in range(0,len(self.active_negatives)):
                to_be_expanded = self.active_negatives.pop(0)
                for i in range(max(to_be_expanded),len(self.negative_items)):
                    self.active_negatives.append(to_be_expanded+[i])
                    self.new_negatives[reduce(lambda x,y:x+self.weighter(self.negative_items[y]),to_be_expanded+[i],0)]=to_be_expanded+[i]
            

    def _check_and_update_options(self):
        for new_positive in self.new_positives:
            if -new_positive in self.negative_scores:
                return (self.new_positives[new_positive],self.negative_scores[-new_positive])
            
            if -new_positive in self.new_negatives:
                return (self.new_positives[new_positive],self.new_negatives[-new_positive])


        for new_negative in self.new_negatives:
            if -new_negative in self.positive_scores:
                return (self.positive_scores[-new_negative],self.new_negatives[new_negative])
        
        self.negative_scores.update(self.new_negatives)
        self.positive_scores.update(self.new_positives)
        self.new_negatives = dict()
        self.new_positives = dict()

if __name__ == '__main__':
    activity_list = []
    inputs = int(sys.stdin.readline().strip())
    for i in range(0,inputs):
        activity_list.append(sys.stdin.readline().strip())
    
    search_array = gen_search_arrays(activity_list)
    b=Blobular(search_array,lambda n:int(n.calories))

    for i in range(0,7):#we'll do 4 iterations
        
        #matches returns a tuple of (positive items, negative items) or None
        matches = b.blob()
        if matches != None:
            outputs = []
            for item in matches[0]:
                outputs.append(b.positive_items[item].name)
            for item in matches[1]:
                outputs.append(b.negative_items[item].name)
            outputs.sort()
            for output in outputs:
                print output
            exit(0)
    
    print "no matches"
