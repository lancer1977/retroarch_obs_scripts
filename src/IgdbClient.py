
import requests
import json

from igdbGame import IgdbGame
from emulatordb import getIgdbIdFromSlug

class IgdbClient:
    def __init__(self, client_id, client_secret):
        self._client_id = client_id
        self._client_secret = client_secret
        self._token = None
        self._client = requests.Session()
        self._client.headers.update({
            "Client-ID": client_id,
            "Accept": "application/json"
        })

    @property
    def is_authenticated(self):
        return self._token is not None

    async def set_auth_token(self):
        if not self.is_authenticated:
            url = f"https://id.twitch.tv/oauth2/token?client_id={self._client_id}&client_secret={self._client_secret}&grant_type=client_credentials"
            result = self._client.post(url)
            response = result.json()
            self._token = response.get('access_token')
            print(self._token)
        return self._token
    
    async def post(self, url, query):
        #print(f"Query: {query}")
        # Form content for the request
        string_content = query

        headers = {
            "Content-Type": "application/json",  # Adjust content type as needed
            "Custom-Header": "Header-Value",  # Add custom headers here
            "Authorization": f"Bearer {self._token}",
            "Client-ID": self._client_id
        }
        
        # Send POST request
        response = requests.post(url, data=string_content, headers=headers)

        if response.status_code == 200:
            response_content = ""
            try:
                response_content = response.text
                #print(response_content)
                return json.loads(response_content)
            except Exception as ex:
                print(response_content)
                print(ex)

        else:
            print("Request failed: " + response.reason)

        return None

    async def getRawGame(self, name, platform):
        if not self.is_authenticated:
            await self.set_auth_token()
        platformId = getIgdbIdFromSlug(platform)
        platformSearch = f"where platforms = ({platformId});" 
        content = f'search "{name}";{platformSearch} fields  age_ratings,aggregated_rating,aggregated_rating_count,alternative_names.*,artworks.*,bundles,category,checksum,collection.*,cover.*,created_at,dlcs,expanded_games,expansions,external_games.*,first_release_date,follows,forks,franchise,franchises,game_engines,game_localizations,game_modes,genres,hypes,involved_companies.*,keywords,language_supports,multiplayer_modes,name,parent_game,platforms,player_perspectives,ports,rating,rating_count,release_dates,remakes,remasters,screenshots.*,similar_games,slug,standalone_expansions,status,storyline,summary,tags,themes.*,total_rating,total_rating_count,updated_at,url,version_parent,version_title,videos,websites;'
        print(content)
        url = f"https://api.igdb.com/v4/games"
        result = await self.post(url,content)        
        return result
    async def getGame(self, name, platform):
        igdbgames = await self.getRawGame(name, platform)
        if igdbgames:
            return [IgdbGame(x) for x in igdbgames]
    async def getPlatformData(self):
        if not self.is_authenticated:
            await self.set_auth_token()
        content = 'fields  id,abbreviation,alternative_name,category,checksum,created_at,generation,name,platform_family,platform_logo,slug,summary,updated_at,url,versions,websites;limit 500;sort name asc;'
        url = f"https://api.igdb.com/v4/platforms"
        result = await self.post(url,content)
        return result