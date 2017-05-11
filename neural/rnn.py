from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from train_data import get_supervised_data_set


def get_train(data):
    net = buildNetwork(len(data[0][0]), 105, 1, recurrent=True)
    trainer = BackpropTrainer(net, get_supervised_data_set(data))
    trainer.trainEpochs(500)
    # trainer.trainUntilConvergence()
    return trainer

