import matplotlib.pyplot as plt
import networkx as nx
import threading
import time
import matplotlib.animation as animation
from players import colors

positions = [[10, 10]]
nodes = 0
clr_dict = {v: k for k, v in colors.items()}



def moving(board, *args):

    plt.rcParams["figure.figsize"] = [12,8]
    fig = plt.figure()
    fig.add_subplot(111)
    plt.ion()
    positions =[]
    s = len(board.board)
    l = 10 * s
    def animate(*args):

        G = nx.Graph()
        G.add_node('x',pos = (0,0), color = 'white')
        G.add_node('y',pos = (l,l),color = 'white')
        frame = nx.Graph()

        for i in range(len(board.board)):
            for j in range(len(board.board[i])):
                if board.board[i][j] != 0:
                    G.add_node(int(str(i)+str(j)), pos=(j*10, (s-i)*10), color=clr_dict.get(board.board[i][j]))


        plt.clf()
        plt.cla()
        ndcolor = [nx.get_node_attributes(G, 'color').get(node) for node in G.nodes()]
        nx.draw(G, pos=nx.get_node_attributes(G, 'pos'), with_labels=False, node_size=500, node_color=ndcolor,
                font_size=20, font_color="white")


    an = animation.FuncAnimation(fig, animate, fargs=[len(positions), positions], interval=500)

    plt.show()
    while True:
        plt.pause(0.5)

