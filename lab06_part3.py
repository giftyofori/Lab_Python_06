class team:
    def __init__(self,name,league,manager_name,point=None):
        self.name=name
        self.league=league
        self.manager_name=manager_name
        self.point=[]
        self.player=[]

    def add_player(self,player):
        self.player.append(player)
        return self.player
    def __str__(self):
        return self.name,self.league,self.manager_name
spain=team('spain','UEFA','del bosque')
portugal=team('portugal','UEFA','paulo bento')
spain.add_player('torress')
spain.add_player('messi')
print spain.player
portugal.add_player('ronaldo')
print portugal.player


class player:
    def __init__(self,firstname,lastname,team):
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
new_player=player('fernando','torres','spain')
new_player2=player('christiano','ronaldo','portugal')
new_player.add_score('01/02/20',0)
new_player.add_score('01/03/20',0)
new_player.add_score('02/03/20',1)
new_player2.add_score('03/04/20',0)
new_player.add_score('02/03/20',1)
new_player.total_score()
new_player.average_score()
print 'average score of torres :' ,new_player.average_score()
        
        
class match:
    def __init__(self,home_team,away_team,date=None):
        self.home_team=home_team
        self.away_team=away_team
        self.home_scores={}
        self.away_scores={}

    def home_score(self):
        total =0
        for value in self.home_scores.itervalues():
            total= total+value
        return total

    def away_score(self):
        total=0
        for value in self.away_scores.itervalues():
            total= total+value
            return total

    def winner(self):
        if self.home_score()>self.away_score():
            return self.home_team
        elif self.home_score()<self.away_score():
            return self.away_team
        else:
            return 'draw'
            
        
        
            
    def add_score(self,player,score):
        player.team
        home_team={player:score}
        self.home_scores[player]=score
        player_team=player.team
        if player_team==self.home_team:
            if player.last_name not in self.home_scores:
                self.home_scores[player.last_name]=score
            else:
                    self.home_score[player.last_name]+=score
        else:
            if player.last_name not in self.away_scores:
                self.away_scores[player.last_name]
            else:
                self.away_scores[player.last_name]+=score
        return team
        
    
        
