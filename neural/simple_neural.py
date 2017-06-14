from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from file_parse import get_all_data
from train_data import get_supervised_data_set

STEP = 10


# def get_supervised_data_set(data):
#     ds = SupervisedDataSet(len(data[0][0]), 1)
#     for i in data:
#         ds.addSample(i[0], i[1])
#     return ds


def hidden0_tst(good_data, n, bad_file):
    net = buildNetwork(len(good_data[0]), n, 2)
    trainer = BackpropTrainer(net, get_supervised_data_set(good_data, bad_file))
    # trainer.trainUntilConvergence()
    return trainer


def train_for_step(good_data, bad_data):
    for i in range(5, 226, STEP):
        trainer = hidden0_tst(good_data, i, bad_data)
        for j in range(20):
            trainer.train()
        print "{:03d}".format(i), trainer.train()


if __name__ == '__main__':
    good_data, bad_data = get_all_data()
    train_for_step(good_data, bad_data)
    # print trainer
