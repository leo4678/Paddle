#  Copyright (c) 2018 PaddlePaddle Authors. All Rights Reserve.
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.
from paddle.trainer_config_helpers import *

settings(batch_size=1000, learning_rate=1e-5)

din = data_layer(name='data', size=100)

trans = trans_layer(input=din)

hidden = fc_layer(input=trans, size=100, bias_attr=False)

mask = data_layer(name='mask', size=100)

hidden_sel = selective_fc_layer(
    input=din, select=mask, size=100, act=SigmoidActivation())

outputs(hidden, hidden_sel)