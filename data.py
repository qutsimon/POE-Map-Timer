'''
How to store date and time - two seperate lists? dict? - what keys, index key with date time list?
two dimensional array, date and time, dict key date only with time list
- If they are stored in two seperate lists sorting will be hard?
'''

#Dict with date key and time list value
class Data:

    #Dict key is date and time is in seconds format
    def __init__(self, cat_name, dict=None):
        if dict is None:
            self.dict = {}
        else:
            self.dict = dict
        self.cat_name = cat_name

    #try catch is more efficient?
    def add_to_dict(self,  date, time):
        if date in self.dict.keys():
            self.dict[date].append(time)
        else:
            self.dict[date] = []
            self.dict[date].append(time)

    #Need to consider the same time values 
    def remove_from_dict(self, date, time):
        try:
            self.dict[date].remove(time)
        except:
            print("Time does not exist.")
    
    def return_cat_name(self):
        return self.cat_name
