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
        self.__p1points = constante_zero
        self.__p2points = constante_zero
        
    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.P1Score()
        else:
            self.P2Score()
            
    def get_Player1Name(self):
        return self.__player1Name
    
    def get_Player2Name(self):
        return self.__player2Name
    
    def get_p1points(self):
        return self.__p1points
    
    def get_p2points(self):
        return self.__p2points
    
    
    def score(self):
        result = ""
        if (get_p1points() == get_p2points() and get_p1points() < constante_three):
            if (get_p1points()==constante_zero):
                result = "Love"
            if (get_p1points()==constante_one):
                result = "Fifteen"
            if (get_p1points()==constante_two):
                result = "Thirty"
            result += "-All"
        if (get_p1points()==get_p2points() and get_p1points()>constante_two):
            result = "Deuce"
        
        P1res = ""
        P2res = ""
        if (get_p1points()> constante_zero and get_p2points()==constante_zero):
            if (get_p1points()==constante_one):
                P1res = "Fifteen"
            if (get_p1points()==constante_two):
                P1res = "Thirty"
            if (get_p1points()==constante_three):
                P1res = "Forty"
            
            P2res = "Love"
            result = P1res + "-" + P2res
        if (get_p2points() > constante_zero and get_p1points()==constante_zero):
            if (get_p2points()==constante_one):
                P2res = "Fifteen"
            if (get_p2points()==constante_two):
                P2res = "Thirty"
            if (get_p2points()==constante_three):
                P2res = "Forty"
            
            P1res = "Love"
            result = P1res + "-" + P2res
        
        
        if (get_p1points()>get_p2points() and get_p1points() < constante_for):
            if (get_p1points()==constante_two):
                P1res="Thirty"
            if (get_p1points()==constante_three):
                P1res="Forty"
            if (get_p2points()==constante_one):
                P2res="Fifteen"
            if (get_p2points()==constante_two):
                P2res="Thirty"
            result = P1res + "-" + P2res
        if (get_p2points()>get_p1points() and get_p2points() < constante_for):
            if (get_p2points()==constante_two):
                P2res="Thirty"
            if (get_p2points()==constante_three):
                P2res="Forty"
            if (get_p1points()==constante_one):
                P1res="Fifteen"
            if (get_p1points()==constante_two):
                P1res="Thirty"
            result = P1res + "-" + P2res
        
        if (get_p1points() > get_p2points() and get_p2points() >= constante_three):
            result = "Advantage " + get_Player1Name()
        
        if (get_p2points() > get_p1points() and get_p1points() >= constante_three):
            result = "Advantage " + get_Player2Name()
        
        if (get_p1points()>=constante_for and get_p2points()>=constante_zero and (get_p1points()-get_p2points())>=constante_two):
            result = "Win for " + get_Player1Name()
        if (get_p2points()>=constante_for and get_p1points()>=constante_zero and (get_p2points()-get_p1points())>=constante_two):
            result = "Win for " + get_Player2Name()
        return result
    
    def SetP1Score(self, number):
        for i in range(number):
            self.P1Score()
    
    def SetP2Score(self, number):
        for i in range(number):
            self.P2Score()
    
    def P1Score(self):
        get_p1points() +=constante_one
    
    
    def P2Score(self):
        get_p2points() +=constante_one
