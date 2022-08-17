
# Copyright 2020 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import logging
import random
from flask import Flask, request

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger(__name__)

app = Flask(__name__)
moves = ['F', 'T', 'L', 'R']

@app.route("/", methods=['GET'])
def index():
    return "Let the battle begin!"

@app.route("/", methods=['POST'])
def move():
    request.get_data()
    logger.info(request.json)
    data = request.json
    state = data['arena']['state']
    x = state['https://cloud-run-hackathon-python-2lrdjc6pya-uc.a.run.app']['x']
    y = state['https://cloud-run-hackathon-python-2lrdjc6pya-uc.a.run.app']['y']
    dir = state['https://cloud-run-hackathon-python-2lrdjc6pya-uc.a.run.app']['direction']
    bots=[]
    for player in state:
        bot=[]
        bot['x'] = int(player['x'])
        bot['y'] = int(player['y'])
        bot['dir'] = player['direction']
        bots.append(bot)
    for bot in bots:
        if bot['x'] - x <3:
            if bot['x'] - x <3 & bot['dir'] == dir:
                return 'F'
            elif bot['x'] - x <3:
                return bot['dir']
            else:
                return moves[random.randrange(len(moves))]
        else:
            return moves[random.randrange(len(moves))]

if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
  
