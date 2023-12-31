import torch
from random import choice
from model import NumberCodeModel
from numbercode import NumberCode 
from dataset import createInputAsFloatList
import torch.nn as nn
import sys
from configparser import ConfigParser

config = ConfigParser()
config.read('train.conf')
enviroment = sys.argv[1]

print("Testing training result from env "+enviroment)

NumberCode.codeWith = config.getint(enviroment, 'width')
model = NumberCodeModel(hiddenLayerOrder=config.getint(enviroment, 'hidden_layer_size'))

model.load_state_dict(torch.load(config.get(enviroment,'model_file')))

counter = 0
counterSuccess = 0
counterValid = 0

for i in range(1000):
    wrongValue = choice((True, False))
    if wrongValue:
        counterValid = counterValid +1
    code = NumberCode.createRandomCode(wrong=wrongValue)
    counter = counter+1
    input = torch.FloatTensor(createInputAsFloatList(code.code))
    output = model.forward(input)
    softmax = nn.Softmax(dim = 0)
    expectedResult = not(wrongValue)
    tensorResult = softmax(output)
    calculatedResult = tensorResult.data[1] > tensorResult.data[0]
    if (calculatedResult == expectedResult):
        counterSuccess = counterSuccess+1

print(str(counterSuccess)+" successes from "+str(counter)+" trials with "+str(counterValid)+" valid codes")
    
    
