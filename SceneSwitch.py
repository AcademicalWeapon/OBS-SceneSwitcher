import os
from dotenv import load_dotenv
from obswebsocket import obsws, requests

load_dotenv()

# Set up connection parameters
host: str = "localhost"
port: int = 4444
password: str = os.getenv('api_key_obs')

# OBS Cred
ws = obsws(host, port, password)


def ConnectOBS() -> None:
    """Connects to OBS"""
    try:
        ws.connect()
    except Exception as e:
        print(f"Error Occured while trying to Connect: {e}")


def SwitchScene(scene) -> None:
    """Switches to given Scene"""
    try:
        NewScene: str = scene
        ws.call(requests.SetCurrentScene(
            **{'scene-name': NewScene}))
    except Exception as e:
        print(f"Error Occured while trying to Switch Scenes: {e}")


def DisconnectOBS() -> None:
    """Disconnects from OBS"""
    try:
        ws.disconnect()
    except Exception as e:
        print(f"Error Occured while trying to Disconnect: {e}")


ConnectOBS()
