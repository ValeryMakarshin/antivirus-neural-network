from pybrain.structure import FeedForwardNetwork
from pybrain.structure import FullConnection
from pybrain.structure import LinearLayer, SigmoidLayer
from pybrain.supervised import BackpropTrainer

from train_data import get_supervised_data_set

THRESHOLD = 0.5


def get_third_nn(value, good_data, bad_data):
    build_network = FeedForwardNetwork()
    inLayer = LinearLayer(len(good_data[0]))
    hiddenLayer = SigmoidLayer(value)
    outLayer = SigmoidLayer(1)

    build_network.addInputModule(inLayer)
    build_network.addModule(hiddenLayer)
    build_network.addOutputModule(outLayer)

    in_to_hidden = FullConnection(inLayer, hiddenLayer)
    hidden_to_out = FullConnection(hiddenLayer, outLayer)
    in_to_out = FullConnection(inLayer, outLayer)

    build_network.addConnection(in_to_hidden)
    build_network.addConnection(hidden_to_out)
    build_network.addConnection(in_to_out)

    build_network.sortModules()
    trainer = BackpropTrainer(build_network,
                              get_supervised_data_set(good_data, bad_data))

    result = trainer.trainUntilConvergence()
    return result[0][-1]


def make_choice(data):
    return True if data[0] > THRESHOLD else False


def find_virus(first_nn, second_nn, third_nn, good_base, bad_base):
    good_index = 0
    bad_index = 0
    for i in good_base:
        if make_choice(first_nn.activate(i)) \
                or make_choice(second_nn.activate(i)) \
                or make_choice(third_nn.activate(i)):
            good_index += 1

    for i in bad_base:
        if (not make_choice(first_nn.activate(i))) \
                and (not make_choice(second_nn.activate(i))) \
                and (not make_choice(third_nn.activate(i))):
            bad_index += 1
    return (1 - good_index / len(good_base)), (1 - bad_index / len(bad_base))
