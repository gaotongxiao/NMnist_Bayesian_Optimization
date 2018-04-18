from layer_graph import LAYERS, Layer_graph
import matplotlib.pyplot as plt

class Pool(object):
    def __init__(self):
        self.pool = []
        G = Layer_graph(57784)
        G.add_node(LAYERS.ip)
        G.append(LAYERS.conv3, 64)
        G.append(LAYERS.conv3, 64)
        G.append(LAYERS.maxpool)
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.maxpool)
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.maxpool)
        G.append(LAYERS.conv3, 256)
        G.append(LAYERS.conv3, 256)
        G.append(LAYERS.maxpool)
        G.append(LAYERS.conv3, 512)
        G.append(LAYERS.conv3, 512)
        G.append(LAYERS.maxpool)
        G.append(LAYERS.fc, 128)
        G.append(LAYERS.fc, 256)
        G.append(LAYERS.fc, 512)
        G.append(LAYERS.softmax)
        G.append(LAYERS.op)
        G.update_lm()
        self.pool.append(G)
        G = Layer_graph(92111)
        G.add_node(LAYERS.ip)
        G.append(LAYERS.conv3, 64)
        G.append(LAYERS.conv3, 64)
        G.append(LAYERS.maxpool)
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.maxpool)
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.maxpool)
        G.append(LAYERS.conv3, 256)
        G.append(LAYERS.conv3, 256)
        G.append(LAYERS.conv3, 256)
        G.append(LAYERS.maxpool)
        G.append(LAYERS.conv3, 512)
        G.append(LAYERS.conv3, 512)
        G.append(LAYERS.conv3, 512)
        G.append(LAYERS.maxpool)
        G.append(LAYERS.fc, 128)
        G.append(LAYERS.fc, 256)
        G.append(LAYERS.fc, 512)
        G.append(LAYERS.softmax)
        G.append(LAYERS.op)
        G.update_lm()
        self.pool.append(G)
        G = Layer_graph(126517)
        G.add_node(LAYERS.ip)
        G.append(LAYERS.conv3, 64)
        G.append(LAYERS.conv3, 64)
        G.append(LAYERS.maxpool)
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.maxpool)
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.maxpool)
        G.append(LAYERS.conv3, 256)
        G.append(LAYERS.conv3, 256)
        G.append(LAYERS.conv3, 256)
        G.append(LAYERS.conv3, 256)
        G.append(LAYERS.maxpool)
        G.append(LAYERS.conv3, 512)
        G.append(LAYERS.conv3, 512)
        G.append(LAYERS.conv3, 512)
        G.append(LAYERS.conv3, 512)
        G.append(LAYERS.maxpool)
        G.append(LAYERS.fc, 128)
        G.append(LAYERS.fc, 256)
        G.append(LAYERS.fc, 512)
        G.append(LAYERS.softmax)
        G.append(LAYERS.op)
        G.update_lm()
        self.pool.append(G)
        G = Layer_graph(57735)
        G.add_node(LAYERS.ip)
        G.append(LAYERS.conv7, 64)
        G.append(LAYERS.maxpool)
        G.append(LAYERS.conv3, 64) #conv 3 / 2
        G.append(LAYERS.conv3, 64)
        G.append(LAYERS.conv3, 128) #conv 3 / 2
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.conv3, 256) #conv 3 / 2
        G.append(LAYERS.conv3, 256)
        G.append(LAYERS.conv3, 512) #conv 3 / 2
        G.append(LAYERS.conv3, 512)
        G.append(LAYERS.avgpool)
        G.append(LAYERS.fc, 1024)
        G.append(LAYERS.softmax)
        G.append(LAYERS.op)
        G.update_lm()
        self.pool.append(G)
        G = Layer_graph(92551)
        G.add_node(LAYERS.ip)
        G.append(LAYERS.conv7, 64)
        G.append(LAYERS.maxpool)
        G.append(LAYERS.conv3, 64) #conv 3 / 2
        G.append(LAYERS.conv3, 64)
        G.append(LAYERS.conv3, 64)
        G.append(LAYERS.conv3, 128) #conv 3 / 2
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.conv3, 256) #conv 3 / 2
        G.append(LAYERS.conv3, 256)
        G.append(LAYERS.conv3, 256)
        G.append(LAYERS.conv3, 512) #conv 3 / 2
        G.append(LAYERS.conv3, 512)
        G.append(LAYERS.conv3, 512)
        G.append(LAYERS.avgpool)
        G.append(LAYERS.fc, 1024)
        G.append(LAYERS.softmax)
        G.append(LAYERS.op)
        G.update_lm()
        self.pool.append(G)
        G = Layer_graph(31659)
        G.add_node(LAYERS.ip)
        G.append(LAYERS.conv7, 64)
        G.append(LAYERS.maxpool)
        G.append(LAYERS.conv3, 64) #conv 3 / 2
        G.append(LAYERS.conv3, 64)
        G.append(LAYERS.conv3, 64)
        G.append(LAYERS.conv3, 64)
        G.append(LAYERS.conv3, 128) #conv 3 / 2
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.conv3, 256) #conv 3 / 2
        G.append(LAYERS.conv3, 256)
        G.append(LAYERS.conv3, 256)
        G.append(LAYERS.conv3, 256)
        G.append(LAYERS.avgpool)
        G.append(LAYERS.fc, 512)
        G.append(LAYERS.softmax)
        G.append(LAYERS.op)
        G.update_lm()
        self.pool.append(G)
        G = Layer_graph(127367)
        G.add_node(LAYERS.ip)
        G.append(LAYERS.conv7, 64)
        G.append(LAYERS.maxpool)
        G.append(LAYERS.conv3, 64) #conv 3 / 2
        G.append(LAYERS.conv3, 64)
        G.append(LAYERS.conv3, 64)
        G.append(LAYERS.conv3, 64)
        G.append(LAYERS.conv3, 128) #conv 3 / 2
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.conv3, 128)
        G.append(LAYERS.conv3, 256) #conv 3 / 2
        G.append(LAYERS.conv3, 256)
        G.append(LAYERS.conv3, 256)
        G.append(LAYERS.conv3, 256)
        G.append(LAYERS.conv3, 512) #conv 3 / 2
        G.append(LAYERS.conv3, 512)
        G.append(LAYERS.conv3, 512)
        G.append(LAYERS.conv3, 512)
        G.append(LAYERS.avgpool)
        G.append(LAYERS.fc, 1024)
        G.append(LAYERS.softmax)
        G.append(LAYERS.op)
        G.update_lm()
        self.pool.append(G)
        print(len(self.pool))

if __name__ == '__main__':
    P = Pool()
    mut_pool = P.pool[0]
    mut_pool.show_graph()
    mut_pool.mut_dec_en_masse()
    # node = mut_pool.get_graph().nodes[3]
    # print(type(node), node['num_of_filters'])
    # node['num_of_filters']= 1111
    mut_pool.show_graph()
    plt.show()
