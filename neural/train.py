from json_parse import get_all_data
from multilayer_perceptron import *
from recurrent_nn import *

good, bad = get_all_data()


def mlp1():
    for i in range(5, 226, 10):
        result = 0
        for j in range(10):
            result += first_hidden_lvl(value=i, good_data=good, bad_data=bad)
        print i, result / 10


def mlp2(first):
    for i in range(5, 156, 10):
        result = 0
        for j in range(10):
            result += second_hidden_lvl(first_hidd=first, value=i,
                                        good_data=good, bad_data=bad)
        print i, result / 10


def mlp3(first, second):
    for i in range(5, 61, 5):
        result = 0
        for j in range(10):
            result += third_hidden_lvl(first_hidd=first, second_hidd=second,
                                       value=i, good_data=good, bad_data=bad)
        print i, result / 10


def rnn():
    for i in range(5, 226, 10):
        result = 0
        for j in range(10):
            result += first_hid_rec(value=i, good_data=good, bad_data=bad)
        print i, result / 10
