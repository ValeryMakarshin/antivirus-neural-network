from pybrain.structure import FeedForwardNetwork
from pybrain.structure import FullConnection
from pybrain.structure import LinearLayer, SigmoidLayer


n = FeedForwardNetwork()
inLayer = LinearLayer(2)
hiddenLayer = SigmoidLayer(3)
outLayer = SigmoidLayer(1)

n.addInputModule(inLayer)
n.addModule(hiddenLayer)
n.addOutputModule(outLayer)

in_to_hidden = FullConnection(inLayer, hiddenLayer)
hidden_to_out = FullConnection(hiddenLayer, outLayer)
in_to_out = FullConnection(inLayer, outLayer)

n.addConnection(in_to_hidden)
n.addConnection(hidden_to_out)
n.addConnection(in_to_out)

n.sortModules()

print n