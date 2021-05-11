# !/usr/bin/python
# -*- coding: utf-8 -*-

from copy import deepcopy
import time


class AIPlayer:
    """
    AI 玩家
    """

    def __init__(self, color):
        """
        玩家初始化
        :param color: 下棋方，'X' - 黑棋，'O' - 白棋
        """

        self.color = color
        if self.color == 'O':
            self.op_color = 'X'
        else:
            self.op_color = 'O'
        self.second_weight = [[45, 2, 9, 9, 9, 9, 2, 45],
                              [2, 0, 3, 3, 3, 3, 0, 2],
                              [9, 3, 5, 5, 5, 5, 3, 9],
                              [9, 3, 5, 1, 1, 5, 3, 9],
                              [9, 3, 5, 1, 1, 5, 3, 9],
                              [9, 3, 5, 5, 5, 5, 3, 9],
                              [2, 0, 3, 3, 3, 3, 0, 2],
                              [45, 2, 9, 9, 9, 9, 2, 45]]
        self.start = 0
        self.base_stable_score = 10
        self.corner_score = 80
        self.s_corner_score = 40
        self.s_line_score = 20

    def get_move(self, board):
        """
        根据当前棋盘状态获取最佳落子位置
        :param board: 棋盘
        :return: action 最佳落子位置, e.g. 'A1'
        """
        if self.color == 'X':
            player_name = '黑棋'
        else:
            player_name = '白棋'
        print("请等一会，对方 {}-{} 正在思考中...".format(player_name, self.color))

        virtual_board = deepcopy(board)
        self.start = time.clock()
        action, value = self.max_value(virtual_board, -65, 65, 0)

        return action

    def heuristic(self, virtual_board, flexibility, op_flexibility):
        board = virtual_board._board
        value = 0
        s1, s2 = virtual_board.count(self.op_color), virtual_board.count(self.color)
        s_sum = s1 + s2
        s_diff = s1 - s2

        if board[0][0] == self.color:
            value += self.corner_score
            for i in range(1, 8):
                if board[0][i] == self.color:
                    value += self.base_stable_score 
                else:
                    break
            for i in range(1, 8):
                if board[i][0] == self.color:
                    value += self.base_stable_score 
                else:
                    break
        else:
            if board[1][1] == self.color:
                value -= self.s_corner_score
            if board[0][1] == self.color:
                value -= self.s_line_score
            if board[1][0] == self.color:
                value -= self.s_line_score

        if board[7][0] == self.color:
            value += self.corner_score
            for i in range(1, 8):
                if board[7][i] == self.color:
                    value += self.base_stable_score 
                else:
                    break
            for i in range(6, -1, -1):
                if board[i][0] == self.color:
                    value += self.base_stable_score 
                else:
                    break
        else:
            if board[6][1] == self.color:
                value -= self.s_corner_score
            if board[7][1] == self.color:
                value -= self.s_line_score
            if board[6][0] == self.color:
                value -= self.s_line_score

        if board[0][7] == self.color:
            value += self.corner_score
            for i in range(6, -1, -1):
                if board[0][i] == self.color:
                    value += self.base_stable_score 
                else:
                    break
            for i in range(1, 8):
                if board[i][7] == self.color:
                    value += self.base_stable_score 
                else:
                    break
        else:
            if board[1][6] == self.color:
                value -= self.s_corner_score
            if board[0][6] == self.color:
                value -= self.s_line_score
            if board[1][7] == self.color:
                value -= self.s_line_score

        if board[7][7] == self.color:
            value += self.corner_score
            for i in range(6, -1, -1):
                if board[7][i] == self.color:
                    value -= self.base_stable_score 
                else:
                    break
            for i in range(6, -1, -1):
                if board[i][7] == self.color:
                    value += self.base_stable_score 
                else:
                    break
        else:
            if board[6][6] == self.color:
                value -= self.s_corner_score
            if board[7][6] == self.color:
                value -= self.s_line_score
            if board[6][7] == self.color:
                value -= self.s_line_score

        if board[0][0] == self.op_color:
            value -= self.corner_score
            for i in range(1, 8):
                if board[0][i] == self.op_color:
                    value -= self.base_stable_score 
                else:
                    break
            for i in range(1, 8):
                if board[i][0] == self.op_color:
                    value -= self.base_stable_score 
                else:
                    break
        else:
            if board[1][1] == self.op_color:
                value += self.s_corner_score
            if board[0][1] == self.op_color:
                value += self.s_line_score
            if board[1][0] == self.op_color:
                value += self.s_line_score

        if board[7][0] == self.op_color:
            value -= self.corner_score
            for i in range(1, 8):
                if board[7][i] == self.op_color:
                    value -= self.base_stable_score 
                else:
                    break
            for i in range(6, -1, -1):
                if board[i][0] == self.op_color:
                    value -= self.base_stable_score 
                else:
                    break
        else:
            if board[6][1] == self.op_color:
                value += self.s_corner_score
            if board[7][1] == self.op_color:
                value += self.s_line_score
            if board[6][0] == self.op_color:
                value += self.s_line_score

        if board[0][7] == self.op_color:
            value -= self.corner_score
            for i in range(6, -1, -1):
                if board[0][i] == self.op_color:
                    value -= self.base_stable_score 
                else:
                    break
            for i in range(1, 8):
                if board[i][7] == self.op_color:
                    value -= self.base_stable_score 
                else:
                    break
        else:
            if board[1][6] == self.op_color:
                value += self.s_corner_score
            if board[0][6] == self.op_color:
                value += self.s_line_score
            if board[1][7] == self.op_color:
                value += self.s_line_score

        if board[7][7] == self.op_color:
            value -= self.corner_score
            for i in range(6, -1, -1):
                if board[7][i] == self.op_color:
                    value -= self.base_stable_score 
                else:
                    break
            for i in range(6, -1, -1):
                if board[i][7] == self.op_color:
                    value -= self.base_stable_score 
                else:
                    break
        else:
            if board[6][6] == self.op_color:
                value += self.s_corner_score
            if board[7][6] == self.op_color:
                value += self.s_line_score
            if board[6][7] == self.op_color:
                value += self.s_line_score

        if flexibility == 0:
            flexibility = -100

        if s_sum < 46:
            value += int(2.3 * flexibility) - op_flexibility
            if s_sum < 30:
                value += s_diff
        else:
            for i in range(8):
                for j in range(8):
                    if board[i][j] == self.color:
                        value += self.second_weight[i][j]
                    elif board[i][j] == self.op_color:
                        value -= self.second_weight[i][j]

        return value / 3000

    def max_value(self, virtual_board, alpha, beta, depth):
        list_x = list(virtual_board.get_legal_actions('X'))
        list_o = list(virtual_board.get_legal_actions('O'))

        if len(list_x) == 0 and len(list_o) == 0:
            return None, virtual_board.count(self.color) - virtual_board.count(self.op_color)

        v = -65
        final_action = None

        if self.color == 'X':
            current_color = 'X'
            legal_list = list_x
            op_legal_list = list_o
        else:
            current_color = 'O'
            legal_list = list_o
            op_legal_list = list_x

        if len(legal_list) == 0:
            return self.min_value(virtual_board, alpha, beta, depth + 1)

        s_sum = virtual_board.count('X') + virtual_board.count('O')
        if time.clock() - self.start >= 57.5 or (depth >= 6 and s_sum < 57):
            return None, self.heuristic(virtual_board, len(legal_list), len(op_legal_list))

        self.list_sort(virtual_board, legal_list)

        for action in legal_list:
            flipped = virtual_board._move(action, current_color)
            temp_min_value = self.min_value(virtual_board, alpha, beta, depth + 1)[1]
            virtual_board.backpropagation(action, flipped, current_color)

            if temp_min_value > v:
                final_action = action
                v = temp_min_value
            if v >= beta:
                return None, v
            if v > alpha:
                alpha = v
        return final_action, v

    def min_value(self, virtual_board, alpha, beta, depth):
        list_x = list(virtual_board.get_legal_actions('X'))
        list_o = list(virtual_board.get_legal_actions('O'))

        if len(list_x) == 0 and len(list_o) == 0:
            return None, virtual_board.count(self.color) - virtual_board.count(self.op_color)

        v = 65
        final_action = None

        if self.color == 'X':
            current_color = 'O'
            legal_list = list_o
        else:
            current_color = 'X'
            legal_list = list_x

        if len(legal_list) == 0:
            return self.max_value(virtual_board, alpha, beta, depth + 1)

        self.list_sort(virtual_board, legal_list)

        for action in legal_list:
            flipped = virtual_board._move(action, current_color)
            temp_max_value = self.max_value(virtual_board, alpha, beta, depth + 1)[1]
            virtual_board.backpropagation(action, flipped, current_color)

            if temp_max_value < v:
                final_action = action
                v = temp_max_value
            if v <= alpha:
                return None, v
            if v < beta:
                beta = v
        return final_action, v

    def list_sort(self, virtual_board, legal_list):
        for i in range(len(legal_list)):
            for j in range(len(legal_list) - i - 1):
                x1, y1 = virtual_board.board_num(legal_list[j])
                x2, y2 = virtual_board.board_num(legal_list[j + 1])
                if self.second_weight[x1][y1] < self.second_weight[x2][y2]:
                    tmp = legal_list[j]
                    legal_list[j] = legal_list[j + 1]
                    legal_list[j + 1] = tmp
