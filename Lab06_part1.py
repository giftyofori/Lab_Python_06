"""
Lab_Python_06
Part 1
"""

"""
Whatever the datastructure you choose,
it should represent the following data:

player		| date		| score
_______________________________________
rooney		| 6/23/2012	| 2
rooney		| 6/25/2012	| 2
ronaldo		| 6/19/2012	| 0
ronaldo		| 6/20/2012	| 3
torres		| 6/21/2012	| 0
torres		| 6/21/2012	| 1
"""

## create the player_stats data structure
'''import datetime
player_stats = {'rooney':[(datetime.date(2012,6,23),2),(datetime.date(2012,6,25),2)],'ronaldo':[(datetime.date(2012,6,19),3),(datetime.date(2012,6,20),0)],'torres':[(datetime.date(2012,6,21),0),(datetime.date(2012,6,21),1)]}
for  key,value in player_stats.iteritems():
    print key, value'''
## implement highest_score
highest_score=[4,3,18,9, 5,4,3,2]
a=0
'''for n in range(0,len(highest_score)):
    if highest_score[n]>a:
        a= highest_score[n]
print a'''
        



## implement highest_score_for_player

'''def highest_score_for_player(a,b):
    score=max(b)
    print a+"'s" + '  ' ,   'maximum score is ',max(b)'''



## implement highest_scorer
highest_scorer={'rooney':[2,2],'ronaldo':[0,3],'torres':[0,1]}
for a, b in highest_scorer.iteritems():
    max(b)
    print a,max(b)





