import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation


import networkx as nx
import threading

positions = [[10,10]]
nodes = 0

def moving():
    fig = plt.figure()
    fig.add_subplot(111)
    plt.ion()


    print(type(positions))
    def animate(*args):





        G = nx.Graph()
        #
        for e in range(len(positions)):

            G.add_node(e, pos=(positions[e][0],positions[e][1]) )


        plt.clf()
        plt.cla()

        nx.draw(G,pos= nx.get_node_attributes(G, 'pos'),with_labels=True, node_size=500, node_color="red", font_size=20, font_color="white")
        # print(nx.get_node_attributes(G,'pos'))

    an =animation.FuncAnimation(fig, animate,fargs=[len(positions),positions], interval=500)

    # plt.draw()
    plt.show()
    while True:
        plt.pause(0.5)


def printing():

    while True:
        print("im working")
        new=[int(input("x: ")),int(input("y: "))]
        positions.append(new)
        time.sleep(2)

def main():

    g = threading.Thread(target=moving)
    p = threading.Thread(target=printing)

    g.start()
    p.start()
    plt.close()





if __name__ == '__main__':
    threading.Thread(target=main).start()


