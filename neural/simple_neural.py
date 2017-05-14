from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from file_parse import get_all_data
from train_data import get_supervised_data_set

GOOD_FILE = 'base/dll_500.json'
BAD_FILE = 'base/dll_500.json'
STEP = 5


# def get_supervised_data_set(data):
#     ds = SupervisedDataSet(len(data[0][0]), 1)
#     for i in data:
#         ds.addSample(i[0], i[1])
#     return ds


def hidden0_test(good_data, bad_file):
    net = buildNetwork(len(good_data[0]), 5, 1)
    trainer = BackpropTrainer(net, get_supervised_data_set(good_data, bad_file))
    # trainer.trainUntilConvergence()
    return trainer


if __name__ == '__main__':
    trainer = hidden0_test(get_all_data())
    print trainer
