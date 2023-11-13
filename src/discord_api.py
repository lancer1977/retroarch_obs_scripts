import requests
from dialog import showDialogShort
from settings import CurrentSettings

def update_discord(playing: str):
    if (not CurrentSettings.discord_enable):
        return
    token = CurrentSettings.discord_token
    # Set the status and activity details you want to update.
    status_data = {
        # You can use 'online', 'dnd' (Do Not Disturb), 'idle', or 'invisible'.
        # 0 for playing, 1 for streaming, 2 for listening, 3 for watching.
        "status" : "online",
        "custom_status": {
            "text": playing
        }       
    }

    # Define the API endpoint for updating the status.
    url = 'https://discord.com/api/v10/users/@me/settings'

    # Create headers with your token.
    headers = {
        'Authorization': f'{token}'
    }

    # Make a PATCH request to update the status.
    response = requests.patch(url, json=status_data, headers=headers)
    showDialogShort(status_data)
    # Check the response status code to see if the request was successful.
    if response.status_code == 200:        
        showDialogShort('Status updated successfully.')
    else:
        showDialogShort(f'Failed to update status. Status code: {response.status_code}')
        
