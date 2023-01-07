#!/usr/bin/python3
# -*- coding: utf-8 -*-


from Network import*
from Player import*
from State import*

from random import sample
import sys


try:
    nb_nodes = int(sys.argv[1])
    nb_infected = int(sys.argv[2])
    prob = float(sys.argv[3])
    deep_atk = int(sys.argv[4])
    deep_def = int(sys.argv[5])
    alphabeta = sys.argv[6]
    
    # verification of parameter
    if nb_nodes < 3 or nb_infected > nb_nodes / 2 or prob < 0 or deep_atk < 1 or deep_def < 1:
        print('Arguments error. Please read the readme')
        exit()
except IndexError:
    print('Arguments error. Please read the readme.')
    exit()



def useMinimax(state, deep_atk, deep_def, player_atk, player_def):
    """
        Use minimax algorithm on state to play the game
        
        :param state: initiate state
        :type state: State
        :param deep_atk: number of recursivity of algorithm for the attacker
        :type deep_atk: int
        :param deep_def: number of recursivity of algorithm for the defender
        :type deep_def: int
        :param player_atk: attacker player
        :type state: Player
        :param player_def: defender player
        :type state: Player
        :return: the state of end game
        :rtype: State
    """
    while not state.isFinished():
        _, next_move = player_def.minimax(state, deep_def)
        print(next_move)
        if next_move != None:
            state = state.playDefense(next_move)
        
        _, next_move = player_atk.minimax(state, deep_atk)
        print(next_move)
        if next_move != None:
            state = state.playAttack(next_move)
    print('Number of nodes explorate:', player_def.minimax.calls)
    return state



def useAlphabeta(state, deep_atk, deep_def, player_atk, player_def):
    """
        Use alphabeta algorithm on state to play the game
        
        :param state: initiate state
        :type state: State
        :param deep_atk: number of recursivity of algorithm for the attacker
        :type deep_atk: int
        :param deep_def: number of recursivity of algorithm for the defender
        :type deep_def: int
        :param player_atk: attacker player
        :type state: Player
        :param player_def: defender player
        :type state: Player
        :return: the state of end game
        :rtype: State
    """
    while not state.isFinished():
        _, next_move = player_def.alphabeta(state, deep_def)
        print(next_move)
        if next_move != None:
            state = state.playDefense(next_move)
        
        _, next_move = player_atk.alphabeta(state, deep_atk)
        print(next_move)
        if next_move != None:
            state = state.playAttack(next_move)
    print('Number of nodes explorate:', player_def.alphabeta.calls)
    return state



def main(nb_nodes, nb_infected, prob, deep_atk, deep_def, alphabeta):
    """
        The main function to play the game
        
        :param nb_nodes: number of machine in network. It must > 3
        :type nb_nodes: int
        :param nb_infected: number of infected machine in network. It must > 0 and < number of machine / 2
        :type nb_infected: int
        :param prob: probability to create link between two machines. It must > 0
        :type prob: float
        :param deep_atk: number of recursivity of algorithm for the attacker
        :type deep_atk: int
        :param deep_def: number of recursivity of algorithm for the defender
        :type deep_def: int
        :param alphabeta: use alphabeta or minimax algorithm
        :type alphabeta: boolean
    """
    player_def = Player('DEF')
    player_atk = Player('ATK')
    
    network = Network(nb_nodes, prob)
    list_infected = sample(network.getDico().keys(), nb_infected)
    
    state = State(network, list_infected, 'DEF')
    print(state, '-'*50, 'Processing...', sep='\n')
    
    if alphabeta.lower() != 'true':
        state = useMinimax(state, deep_atk, deep_def, player_atk, player_def)
    else:
        state = useAlphabeta(state, deep_atk, deep_def, player_atk, player_def)
    
    print('-'*50, 'End game', state, sep='\n')
    if state.whoWin() == 'DEF':
        print('The defender win')
    else:
        print('The attacker win')



main(nb_nodes, nb_infected, prob, deep_atk, deep_def, alphabeta)