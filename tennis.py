# -*- coding: utf-8 -*-
constante_zero = 0
constante_one = 1
constante_two = 2
constante_three = 3
constante_for = 4

class Game:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = constante_zero
        self.p2points = constante_zero
        
    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.P1Score()
        else:
            self.P2Score()
    
    def score(self):
        result = ""
        if (self.p1points == self.p2points and self.p1points < constante_three):
            if (self.p1points==constante_zero):
                result = "Love"
            if (self.p1points==constante_one):
                result = "Fifteen"
            if (self.p1points==constante_two):
                result = "Thirty"
            result += "-All"
        if (self.p1points==self.p2points and self.p1points>constante_two):
            result = "Deuce"
        
        P1res = ""
        P2res = ""
        if (self.p1points > constante_zero and self.p2points==constante_zero):
            if (self.p1points==constante_one):
                P1res = "Fifteen"
            if (self.p1points==constante_two):
                P1res = "Thirty"
            if (self.p1points==constante_three):
                P1res = "Forty"
            
            P2res = "Love"
            result = P1res + "-" + P2res
        if (self.p2points > constante_zero and self.p1points==constante_zero):
            if (self.p2points==constante_one):
                P2res = "Fifteen"
            if (self.p2points==constante_two):
                P2res = "Thirty"
            if (self.p2points==constante_three):
                P2res = "Forty"
            
            P1res = "Love"
            result = P1res + "-" + P2res
        
        
        if (self.p1points>self.p2points and self.p1points < constante_for):
            if (self.p1points==constante_two):
                P1res="Thirty"
            if (self.p1points==constante_three):
                P1res="Forty"
            if (self.p2points==constante_one):
                P2res="Fifteen"
            if (self.p2points==constante_two):
                P2res="Thirty"
            result = P1res + "-" + P2res
        if (self.p2points>self.p1points and self.p2points < constante_for):
            if (self.p2points==constante_two):
                P2res="Thirty"
            if (self.p2points==constante_three):
                P2res="Forty"
            if (self.p1points==constante_one):
                P1res="Fifteen"
            if (self.p1points==constante_two):
                P1res="Thirty"
            result = P1res + "-" + P2res
        
        if (self.p1points > self.p2points and self.p2points >= constante_three):
            result = "Advantage " + self.player1Name
        
        if (self.p2points > self.p1points and self.p1points >= constante_three):
            result = "Advantage " + self.player2Name
        
        if (self.p1points>=constante_for and self.p2points>=constante_zero and (self.p1points-self.p2points)>=constante_two):
            result = "Win for " + self.player1Name
        if (self.p2points>=constante_for and self.p1points>=constante_zero and (self.p2points-self.p1points)>=constante_two):
            result = "Win for " + self.player2Name
        return result
    
    def SetP1Score(self, number):
        for i in range(number):
            self.P1Score()
    
    def SetP2Score(self, number):
        for i in range(number):
            self.P2Score()
    
    def P1Score(self):
        self.p1points +=constante_one
    
    
    def P2Score(self):
        self.p2points +=constante_one
