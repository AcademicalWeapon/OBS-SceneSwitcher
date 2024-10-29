import os
from dotenv import load_dotenv
from obswebsocket import obsws, requests

load_dotenv()

# Set up connection parameters
host: str = "localhost"
port: int = 4444
password: str = os.getenv('api_key')


# OBS Cred
ws = obsws(host, port, password)

def ConnectOBS() -> None:
    """Connects to OBS"""
    try:
        ws.connect()
        print("Connected")
    except Exception as e:
        print(f"Error Occured while trying to Connect: {e}")


def SwitchScene(scene) -> None:
    """Switches to given Scene"""
    try:
        StandbyScene: int = scene
        ws.call(requests.SetCurrentScene(**{'scene-name': StandbyScene})) # WHY???
        print("Scene Switched")
    except Exception as e:
        print(f"Error Occured while trying to Switch Scenes: {e}")


def DisconnectOBS() -> None:
    """Disconnects from OBS"""
    try:
        ws.disconnect()
        print("Disconnected")
    except Exception as e:
        print(f"Error Occured while trying to Disconnect: {e}")
