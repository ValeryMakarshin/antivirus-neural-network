from pybrain.datasets import SupervisedDataSet


def get_supervised_data_set(data):
    ds = SupervisedDataSet(len(data[0][0]), 1)
    for i in data:
        ds.addSample(i[0], i[1])
    return ds