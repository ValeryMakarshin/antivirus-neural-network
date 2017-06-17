# coding=utf-8
from pybrain import SoftmaxLayer, SigmoidLayer
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from train_data import get_supervised_data_set


# rnn с одним скрытым уровнем
def first_hid_rec(value, good_data, bad_data):
    build_network = buildNetwork(len(good_data[0]), value, 2,
                                 bias=True,
                                 hiddenclass=SigmoidLayer,
                                 outclass=SoftmaxLayer,
                                 recurrent=True)

    trainer = BackpropTrainer(build_network,
                              get_supervised_data_set(good_data, bad_data))
    result = trainer.trainUntilConvergence()
    return result[0][-1]


# rnn с двумя скрытыми уровнями
def second_hid_rec(first_hidd, value, good_data, bad_data):
    build_network = buildNetwork(len(good_data[0]), first_hidd, value, 2,
                                 bias=True,
                                 hiddenclass=SigmoidLayer,
                                 outclass=SoftmaxLayer,
                                 recurrent=True)

    trainer = BackpropTrainer(build_network,
                              get_supervised_data_set(good_data, bad_data))
    result = trainer.trainUntilConvergence()
    return result[0][-1]


# rnn с тремя скрытыми уровнями
def third_hid_rec(first_hidd, second_hidd, value, good_data, bad_data):
    build_network = buildNetwork(len(good_data[0]), first_hidd, second_hidd, value, 2,
                                 bias=True,
                                 hiddenclass=SigmoidLayer,
                                 outclass=SoftmaxLayer,
                                 recurrent=True)

    trainer = BackpropTrainer(build_network,
                              get_supervised_data_set(good_data, bad_data))
    result = trainer.trainUntilConvergence()
    return result[0][-1]


# example
if __name__ == '__main__':
    print first_hid_rec(2, [[1, 0], [1, 0], [3, 0]], [[0, 6], [0, 1], [0, 3]])
    print second_hid_rec(5, 2, [[1, 0], [1, 1], [1, 2]], [[0, 1], [0, 4], [2, 0]])
    print third_hid_rec(5, 2, 2, [[1, 0], [1, 1], [1, 2]], [[0, 1], [0, 4], [2, 0]])
