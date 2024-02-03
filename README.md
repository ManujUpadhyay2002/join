Install : 
pip install git+https://github.com/ManujUpadhyay2002/join.git

Example:
from join import Join

d1 = {
    'team': ['A', 'B', 'C', 'D', 'E', 'F'],
    'points': [4, 4, 6, 8, 9, 5]
}
d2 = {
    'team_name': ['A', 'P', 'C', 'Q', 'E', 'G'],
    'rebounds': [12, 7, 8, 8, 5, 11]
}

obj = Join(d1,d2,'team','team_name')
obj.innerJoin()
obj.leftJoin()
obj.rightJoin()
obj,outerJoin()
