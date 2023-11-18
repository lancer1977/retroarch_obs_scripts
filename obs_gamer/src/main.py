from retroarch_monitor import start
from settings import CurrentSettings
import asyncio

asyncio.run( start(CurrentSettings.retroarch_path, CurrentSettings.sleep_seconds, CurrentSettings.verbose))