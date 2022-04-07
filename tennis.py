# -*- coding: utf-8 -*-
constante_zero = 0
constante_one = 1
constante_two = 2
constante_three = 3
constante_for = 4

class Game:
    def __init__(self, player1Name, player2Name):
        self.__player1Name = player1Name
        self.__player2Name = player2Name
        self.__player1points = constante_zero
        self.__player2points = constante_zero
        
    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.Player1Score()
        else:
            self.Player2Score()
            
    def get_Player1Name(self):
        return self.__player1Name
    
    def get_Player2Name(self):
        return self.__player2Name
    
    def get_p1points(self):
        return self.__player1points
    
    def get_p2points(self):
        return self.__player2points
    
    def empatando():
        result = ""
        if (self.get_player1points()==constante_zero):
                result = "Love"
        if (self.get_player1points()==constante_one):
                result = "Fifteen"
        if (self.get_player1points()==constante_two):
                result = "Thirty"
            result += "-All"       
        return result  
    
    def player1Vencendo():
        P1res = ""
        P2res = ""
        if (self.get_player1points()==constante_one):
            P1res = "Fifteen"
        if (self.get_player1points()==constante_two):
            P1res = "Thirty"
        if (self.get_player1points()==constante_three):
            P1res = "Forty"
                
        P2res = "Love"
        result = P1res + "-" + P2res
        return result
        
     def player2Vencendo():
        if (self.get_player2points()==constante_one):
                P2res = "Fifteen"
        if (self.get_player2points()==constante_two):
                P2res = "Thirty"
        if (self.get_player2points()==constante_three):
                P2res = "Forty"
            
        P1res = "Love"
        result = P1res + "-" + P2res
        
    def player1venceu():
        if (self.get_player1points()==constante_two):
                P1res="Thirty"
        if (self.get_player1points()==constante_three):
                P1res="Forty"
        if (self.get_player2points()==constante_one):
                P2res="Fifteen"
        if (self.get_player2points()==constante_two):
                P2res="Thirty"
        result = P1res + "-" + P2res
        
    def player2venceu():
        if (self.get_player2points()==constante_two):
            P2res="Thirty"
        if (self.get_player2points()==constante_three):
            P2res="Forty"
        if (self.get_player1points()==constante_one):
            P1res="Fifteen"
        if (self.get_player1points()==constante_two):
            P1res="Thirty"
        result = P1res + "-" + P2res
    
    def score(self):
        
        if (self.get_player1points() == self.get_player2points() and self.get_player1points() < constante_three):
            self.empatando()
            
  
        if (self.get_player1points()> constante_zero and self.get_player2points()==constante_zero):
            self.player1Vencendo()  
            
          
        if (self.get_player2points() > constante_zero and self.get_player1points()==constante_zero):
            self.player2Vencendo()
        
        
        if (self.get_player1points()>self.get_player2points() and self.get_player1points() < constante_for):
           self.player1venceu()
        
        
        if (self.get_player2points()>self.get_player1points() and self.get_player2points() < constante_for):
            self.player2venceu()
            
            
        if (self.get_player1points()==self.get_player2points() and self.get_player1points()>constante_two):
            result = "Deuce"
        
        if (self.get_player1points() > self.get_player2points() and self.get_player2points() >= constante_three):
            result = "Advantage " + get_Player1Name()
        
        if (self.get_player2points() > self.get_player1points() and self.get_player1points() >= constante_three):
            result = "Advantage " + get_Player2Name()
        
        if (self.get_player1points()>=constante_for and self.get_player2points()>=constante_zero and (self.get_player1points()-self.get_player2points())>=constante_two):
            result = "Win for " + get_Player1Name()
        if (self.get_player2points()>=constante_for and self.get_player1points()>=constante_zero and (self.get_player2points()-self.get_player1points())>=constante_two):
            result = "Win for " + get_Player2Name()
        return result
    
    def SetPlayer1Score(self, number):
        for i in range(number):
            self.Player1Score()
    
    def SetPlayer2Score(self, number):
        for i in range(number):
            self.Player2Score()
    
    def Player1Score(self):
        self.get_player1points() +=constante_one
    
    
    def Player2Score(self):
        self.get_player2points() +=constante_one
