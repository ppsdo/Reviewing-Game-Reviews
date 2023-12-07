import googleapiclient.discovery
from time import gmtime, strftime
import pandas as pd
import warnings
import sys
from pathlib import Path

# API functions

def get_sys_path():
    return sys.path

def get_api_key(filename="secret.txt"):
    '''
    Returns the YouTube API key as a string found in file.
    
    DO NOT publicly expose this file!
    '''
    key = ""    
    s = Path(__file__).absolute().parent.joinpath(filename)
    with open(s, "r") as f:
        key = f.read()
        
    return key

def get_youtube():
    '''
    Returns a YouTube Resource for interacting with the API
    For more information: https://googleapis.github.io/google-api-python-client/docs/epy/googleapiclient.discovery-module.html
    '''
    api_service_name = "youtube"
    api_version = "v3"
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=get_api_key())
    
    return youtube

