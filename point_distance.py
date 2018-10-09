import math

class Point(object):
    
    def __init__(self, x , y):
        
        self.x = x
        self.y = y
        
        
    def get_distance(self, another_point):
        return math.sqrt(pow(another_point.x - self.x, 2) + pow(another_point.y - self.y, 2))
        
        
    def is_within_distance(self, another_point, distance):
        return self.get_distance(another_point) <= distance
        
    def __repr__(self):
        return "({}, {})".format(self.x, self.y)