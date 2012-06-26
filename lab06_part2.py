class player:
    def __init__(self,firstname,lastname,team=None):
        self.first_name=firstname
        self.last_name=lastname
        self.scores=[]
        self.team=team


    def add_score(self,date,score):
        self.scores.append(score)
        return self.scores

    
    def total_score(self,score):
       new_score = self.scores +score
       return new_score
