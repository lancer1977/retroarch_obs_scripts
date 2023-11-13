import subprocess  
import requests
from flask import Flask, jsonify,request

from settings import CurrentSettings 
from IgdbClient import IgdbClient 

 
_igdbClient = IgdbClient(CurrentSettings.twitch_clientid, CurrentSettings.twitch_secret)
app = Flask(__name__)

@app.route('/getGame', methods=['GET'])
async def get_date():
    name = request.args.get('name')
    platform = request.args.get('platform')
    result = await _igdbClient.getRawGame(name,platform)
    return jsonify(result)



if __name__ == '__main__':
    app.run()