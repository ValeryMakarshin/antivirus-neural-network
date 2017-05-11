from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from train_data import get_supervised_data_set


def test_hidden0(data):
    net = buildNetwork(len(data[0][0]), 105, 1)
    trainer = BackpropTrainer(net, get_supervised_data_set(data))
    trainer.trainEpochs(500)
    # trainer.trainUntilConvergence()
    print net.activate((0, 0))
    return trainer
