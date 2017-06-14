from time import clock

from json_parse import parse_file, get_all_data
from simple_neural import hidden0_tst, train_for_step
from train_data import get_supervised_data_set


GOOD_FILE = 'base/dll_500.json'
BAD_FILE = 'base/dll_500.json'

if __name__ == '__main__':
    print clock()
    good_data, bad_data = get_all_data()
    # trainer = hidden0_test(good_data, bad_data)
    train_for_step(good_data, bad_data)
    # for i in range(20):
        # print trainer.train()
        # print 'time = ', clock()
    #
    # print 'fin time = ', clock()



