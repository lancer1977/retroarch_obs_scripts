import subprocess  
import requests
from flask import Flask, jsonify,request
from BatoceraGameParams import BatoceraGameParams
from retroArchGame import  RetroArchGame, importRetroArchGame
from settings import CurrentSettings 
from writedisk import writeDataFromGameParams
from igdbclient import IgdbClient
from BatoceraGameParams import BatoceraGameParams 
import json
 
_igdbClient = IgdbClient(CurrentSettings.twitch_clientid, CurrentSettings.twitch_secret)
app = Flask(__name__)

@app.route('/getIgdbGame', methods=['GET'])
async def get_IgdbGame():
    name = request.args.get('name')
    platform = request.args.get('platform')
    result = await _igdbClient.getRawGame(name,platform)
    return jsonify(result)

@app.route('/getGame', methods=['GET'])
async def get_game():
    name = request.args.get('name')
    platform = request.args.get('platform')
    game = BatoceraGameParams()
    game.name = name 
    game.platform = platform
    result = await writeDataFromGameParams(game)    
    return result.title


@app.route('/postGame', methods=['POST'])
async def post_game():
    decrypt = json.loads(request.data) 
    batocera = BatoceraGameParams()
    batocera.load(decrypt)
 
    result = await writeDataFromGameParams(batocera)    
    return result.title

if __name__ == '__main__':
    CurrentSettings.importSettings()
    app.run(debug=True,host=CurrentSettings.local_api_ip,port=CurrentSettings.local_api_port)