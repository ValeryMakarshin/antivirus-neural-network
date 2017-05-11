from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer

STEP = 5


def get_supervised_data_set(data):
    ds = SupervisedDataSet(len(data[0][0]), 1)
    for i in data:
        ds.addSample(i[0], i[1])
    return ds


def test_hidden0(data):
    net = buildNetwork(len(data[0][0]), 105, 1)
    trainer = BackpropTrainer(net, get_supervised_data_set(data))
    trainer.trainEpochs(500)
    # trainer.trainUntilConvergence()
    print net.activate((0, 0))
    return trainer


if __name__ == '__main__':
    # data = [[[1, 0], 1], [[0, 1], 1], [[1, 1], 0], [[0, 0], 0], [[0, 0], 1]]
    data = [((1, 0), 1), ((0, 1), 1), ((1, 1), 0), ((0, 0), 0)]
    trainer = test_hidden0(data)
