#!/usr/bin/python3
# -*- coding: utf-8 -*-


from copy import deepcopy


class State(object):
    
    def __init__(self, network, list_infected, current_player):
        """
            Create a new state
            
            :param network: a network
            :type network: Network
            :param list_infected: a list of infected machine in network
            :type list_infected: list
            :param current_player: the player who must play
            :type current_player: String
        """
        self.__network = network
        self.__list_infected = list_infected
        self.__current_player = current_player
    
    
    def getCurrentPlayer(self):
        """
            Return the player of this state
            
            :return: the player of a state
            :rtype: String
        """
        return self.__current_player
    
    
    def getInfected(self):
        """
            Return the list of infected machine of a state
            
            :return: the list of state
            :rtype: list
        """
        return self.__list_infected
    
    
    def getNetwork(self):
        """
            Return the network of this state
            
            :return: the network of a state
            :rtype: Network
        """
        return self.__network
    
    
    def __repr__(self):
        """
            A representation of this state
            
            :return: a representation of a state
            :rtype: String
        """
        return 'Player: ' + self.getCurrentPlayer() + '\n' + str(self.getNetwork()) + 'Infected: ' + str(self.getInfected())
    
    
    def getHealthyEdge(self):
        """
            Return the edge between two healthy machines and between healthy and infected machines
            
            :return: the healthy edge
            :rtype: list
        """
        list_edge = []
        for node in self.getHealthyNode():
            for neighbour in self.getNetwork().getDico()[node]:
                if (neighbour,node) not in list_edge:
                    list_edge.append((node,neighbour))
        return list_edge
    
    
    def getHealthyNode(self):
        """
            Return machines who don't infected
            
            :return: the healthy node
            :rtype: list
        """
        return list(set(self.getNetwork().getDico().keys()) - set(self.getInfected()))
    
    
    def getPossibleAttack(self):
        """
            Return the infectable machines since infected machines
            
            :return: the infectable node
            :rtype: list
        """
        list_attack = []
        for node in self.getInfected():
            for neighbour in self.getNetwork().getDico()[node]:
                if neighbour not in self.getInfected() and neighbour not in list_attack:
                    list_attack.append(neighbour)
        return list_attack
    
    
    def getPossibleDefense(self):
        """
            Return the cutable link between machines
            
            :return: the cutable edge
            :rtype: list
        """
        # Inspired by https://rosettacode.org/wiki/Power_set#Python
        list_def = []
        for node in self.getHealthyNode():
            powerset = [[]]
            for neighbour in self.getNetwork().getDico()[node]:
                powerset.extend([subset + [(node,neighbour)] for subset in powerset])
            list_def += powerset
        # Remove the repetition of empty move ([])
        list_def = [move for move in list_def if len(move) != 0]
        return list_def
    
    
    def getValue(self):
        """
            Return the interest of this state
            
            :return: the value of state
            :rtype: int
        """
        # A state who is finished is more interesting
        # A formula for one player is a opposite of other player
        if self.isFinished():
            if self.whoWin() == 'DEF':
                return (len(self.getHealthyNode()) + len(self.getHealthyEdge())) * 1000
            else:
                return -(len(self.getHealthyNode()) + len(self.getHealthyEdge())) * 1000
        else:
            if self.getCurrentPlayer() == 'DEF':
                return (len(self.getHealthyNode()) + len(self.getHealthyEdge()))
            else:
                return -(len(self.getHealthyNode()) + len(self.getHealthyEdge()))
    
    
    def isFinished(self):
        """
            Return if a game is finished
            
            :return: if a game is finished
            :rtype: boolean
        """
        if len(self.getPossibleAttack()) == 0:
            return True
        return False
    
    
    def playAttack(self, move):
        """
            Play a move to generate a new state
            
            :param move: the move who must play
            :type move: int
            :return: a new updated state
            :rtype: State
        """
        # deepcopy is used to back more facility to original state
        next_network = deepcopy(self.getNetwork())
        next_infected = self.getInfected() + [move]
        return State(next_network, next_infected, 'DEF')
    
    
    def playDefense(self, move):
        """
            Play a move to generate a new state
            
            :param move: the move who must play
            :type move: list
            :return: a new updated state
            :rtype: State
        """
        # deepcopy and copy are used to back more facility to original state
        next_network = deepcopy(self.getNetwork())
        for edge in move:
            next_network.getDico()[edge[0]].remove(edge[1])
            next_network.getDico()[edge[1]].remove(edge[0])
        next_infected = self.getInfected().copy()
        return State(next_network, next_infected, 'ATK')
    
    
    def whoWin(self):
        """
            Return the winner of game where the game is finished
            
            :return: the winner of game
            :rtype: String
        """
        if len(self.getHealthyNode()) >= len(self.getInfected()):
            return 'DEF'
        else:
            return 'ATK'