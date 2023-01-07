#!/usr/bin/python3
# -*- coding: utf-8 -*-


from random import random


class Network(object):
    
    def __init__(self, nb_nodes, prob):
        """
            Create a new network
            
            :param nb_nodes: number of machines in a network. It must > 2
            :type nb_nodes: int
            :param prob: probability to create a link between two machine. It must > 0
            :type prob: float
        """
        self.__dico = {}
        # Fill the dict with a binomial random law
        for num in range(nb_nodes):
            list_neighbour = []
            for next_num in range(num+1, nb_nodes):
                luck = random()
                if luck < prob:
                    list_neighbour.append(next_num)
            self.getDico()[num] = list_neighbour
        
        # For the nodes to see each other
        for node in self.getDico():
            for neighbour in self.getDico()[node]:
                if node not in self.getDico()[neighbour]:
                    self.getDico()[neighbour].append(node)
    
    
    def getDico(self):
        """
            Return the dict of network
            
            :return: the dict of network
            :rtype: dict
        """
        return self.__dico
    
    
    def __repr__(self):
        """
            A representation of this network
            
            :return: a representation of a network
            :rtype: String
        """
        rep = ''
        for node in self.getDico():
            rep += str(node) + ' -> ' + str(self.getDico()[node]) + '\n'
        return rep