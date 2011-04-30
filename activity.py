#!/usr/bin/env python

import collections
Activity = collections.namedtuple("Activity",'name,calories')
def gen_search_arrays(activity_list):
    active = []
    for activity in activity_list:
        activity_name, activity_weight = activity.split(' ')
        active.append(Activity(activity_name,activity_weight))
    
class Blobular(object):
    def __init__(self,item_list,weight_function,weight_goal):
        self.positive_items = []
        self.negative_items = []
        for item in item_list:
            if weight_funtion(item) > 0:
                self.positive_items.append(item)
            else:
                self.negative_items.append(item)

        self.weighter = weight_funtion
        self.goal = weight_goal
        self.active_positives=[]
        self.active_negatives=[]
        self.first_blob=False
        self.negative_scores=dict()
        self.positive_scores=dict()
        self.new_scores=dict()
    
    def blob(self):
        if not self.first_blob:
            self._first_blob()
        else:
            self._reblob()
        return self._check_and_update_options()
    
    def _first_blob(self):
        pass
    
    def _reblob(self):
        pass

    def _check_and_update_options(self):
        pass


if __name__ == '__main__':
    al = ["free-lunch 802","mixed-nuts 421","orange-juice 143",
        "heavy-ddr-session -302","cheese-snacks 137","cookies 316",
        "mexican-coke 150","dropballers-basketball -611","coding-six-hours -466",
        "riding-scooter -42","rock-band -195","playing-drums -295"]
    
    search_array = gen_search_arrays(activity_list)
    b=Blobular(search_array,lambda n:n.calories,0)
    matches = b.blob()
    for i in range(0,7):#we'll do 4 iterations
        if matches != None:
            for item in matches:
                print item.name
            exit(0)
