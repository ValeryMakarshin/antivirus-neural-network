from pybrain.datasets import SupervisedDataSet


def get_supervised_data_set(good_data, bad_data):
    ds = SupervisedDataSet(len(good_data[0]), 2)

    for i in good_data:
        # ds.addSample(i, 0)
        ds.addSample(i, [0, 1])

    for i in bad_data:
        # ds.addSample(i, 1)
        ds.addSample(i, [1, 0])

    return ds


if __name__ == '__main__':
    print get_supervised_data_set([[1, 0], [1, 1], [1, 2]], [[0, 1], [0, 4], [2, 0]])
