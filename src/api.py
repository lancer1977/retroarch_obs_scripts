import subprocess  
import requests
from flask import Flask, jsonify,request
from retroArchGame import GameParams, RetroArchGame, importRetroArchGame
from settings import CurrentSettings 
from writedisk import writeDataFromGameParams
from igdbclient import IgdbClient

 
_igdbClient = IgdbClient(CurrentSettings.twitch_clientid, CurrentSettings.twitch_secret)
app = Flask(__name__)

@app.route('/getGame', methods=['GET'])
async def get_game():
    name = request.args.get('name')
    platform = request.args.get('platform')
    result = await _igdbClient.getRawGame(name,platform)
    return jsonify(result)

@app.route('/postGame', methods=['GET'])
async def post_game():
    name = request.args.get('name')
    platform = request.args.get('platform')
    game = GameParams()
    game.name = name 
    game.platform = platform
    await writeDataFromGameParams(game)
    
    return jsonify(game)



if __name__ == '__main__':
    app.run()