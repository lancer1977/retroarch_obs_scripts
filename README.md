# retroarch_obs_scripts
Scripts to assist in updating OBS with data regarding the current game playing in retroarch. 

## How it works
When you run a game in retroarch content_history.lpl is updated with json describing some data about the state including the games run, the items has the last game inserted into record 0. The code grabs that and attempts to parse the information.
The core is extracted to try to convert it into a folder structure that we then look for a boxart folder if existing, if not it attempts to grab the first matching file, then it tries to remove any (USA) identifiers and make a match against that, otherwise it attempts to set the default value.

This image is then copied to a image directory that the user would need to point OBS to, and display as an IMAGE. I recommend trying to set the image as a fixed value to avoid spam.

## OBS Setting
Edit the Transform for the image with the following properties:
### Positional Alignment
Top Left

### Bounding Box Type
Scale to inner bounds

Then set the size and so forth however you like and it should remain static.


## Usage
Currently things are fairly opinionated as trying to get things working locally. 
Most of the directories are located at the top of *whatson.py* and the subfolder decoration is currently in *playing.py*

# Future Goals
## More Metadata 
I want to feed the actual core data and so fort to the output folder as well, this shouldn't be hard to perhaps provide additional metadata such as titles, game names, cores, etc to the able to be consumed by external apps.
## Web Queries
Query DB for additional data on the title to inject into the output
### Web based images

## Webhooks
Make a call to a discord webhook for example to announce whats playing with the image data.


Inspired by the work done by marcomalachias: https://obsproject.com/forum/threads/obs-retroarch-watchdog.127058/
