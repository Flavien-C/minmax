#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Player(object):
    
    def __init__(self, role):
        """
            Create a new player
            
            :param role: the role of player
            :type role: String
        """
        self.__role = role
    
    
    def getRole(self):
        """
            Return the role of this player
            :return: the role of player
            :rtype: String
        """
        return self.__role
    
    
    # Copy: https://www.python-course.eu/python3_count_function_calls.php
    def call_counter(func):
        """ Decorator for counting the number of function or method calls to the function or method func """
        def helper(*args, **kwargs):
            helper.calls += 1
            return func(*args, **kwargs)
        helper.calls = 0
        helper.__name__ = func.__name__
        return helper
    
    
    @call_counter
    def minimax(self, state, deep):
        """
            Execute a minimax algorithm to return the best move
            
            :param state: a state
            :type state: State
            :param deep: number of recursivity. It must > 0. A hight value (>6) will ask many time of calcul
            :type deep: int
            :return: return the best move
            :rtype: (int, Move)
        """
        if deep == 0 or state.isFinished():
            return state.getValue(), None
        else:
            if state.getCurrentPlayer() == 'DEF':
                best_value = float('-inf')
                best_move = None
                for move in state.getPossibleDefense():
                    next_state = state.playDefense(move)
                    value, _ = self.minimax(next_state, deep-1)
                    if value > best_value:
                        best_value = value
                        best_move = move
                return best_value, best_move
            else:
                best_value = float('+inf')
                best_move = None
                for move in state.getPossibleAttack():
                    next_state = state.playAttack(move)
                    value, _ = self.minimax(next_state, deep-1)
                    if value < best_value:
                        best_value = value
                        best_move = move
                return best_value, best_move
    
    
    @call_counter
    def alphabeta(self, state, deep, alpha=float('-inf'), beta=float('+inf')):
        """
            Execute a alphabeta algorithm to return the best move
            
            :param state: a state
            :type state: State
            :param deep: influence a recursivity. It must > 0. A hight value (>6) will ask many time of calcul
            :type deep: int
            :return: return the best move
            :rtype: (int, Move)
        """
        if deep == 0 or state.isFinished():
            return state.getValue(), None
        else:
            if state.getCurrentPlayer() == 'DEF':
                best_move = None
                for move in state.getPossibleDefense():
                    next_state = state.playDefense(move)
                    value, _ = self.alphabeta(next_state, deep-1, alpha, beta)
                    if value > alpha:
                        alpha = value
                        best_move = move
                    if alpha >= beta:
                        # Coupure beta
                        return alpha, best_move
                return alpha, best_move
            else:
                best_move = None
                for move in state.getPossibleAttack():
                    next_state = state.playAttack(move)
                    value, _ = self.alphabeta(next_state, deep-1, alpha, beta)
                    if value < beta:
                        beta = value
                        best_move = move
                    if alpha >= beta:
                        # Coupure alpha
                        return beta, best_move
                return beta, best_move