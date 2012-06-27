class player:
    def __init__(self,firstname,lastname,team=None):
        self.first_name=firstname
        self.last_name=lastname
        self.scores=[]
        self.team=team
        self.sum = 0


    def add_score(self,date,score):
        self.scores.append(score)
        return self.scores

    
    def total_score(self):
        for i in range(len(self.scores)):
            self.sum+= self.scores[i]
            
        return self.sum


    def average_score(self):
        self.total_score()
        t= self.sum/len(self.scores)
        return t
new_player=player('fernando','torres')
new_player.add_score('01/02/20',0)
new_player.add_score('01/03/20',0)
new_player.add_score('02/03/20',1)
new_player.add_score('03/04/20',0)
new_player.add_score('02/03/20',1)
new_player.total_score()
new_player.average_score()
print 'average score of torres :' ,new_player.average_score()
        
        
        


        
