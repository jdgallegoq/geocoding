import re
from math import (
    sin,
    cos,
    sqrt,
    atan2,
    radians
)

def get_distance(coord1:tuple, coord2:tuple) -> float:
    """
        Function to get the distance between two coordinates using Vincenty distance.
        Params:
             coord1: tuple. tuple of latitute and longitude coordinates
             coord2: tuple. tuple of latitude and longitude coordinates
    """
    # Aprox earth radius in km
    R = 6373.0

    lat1 = radians(coord1[0])
    lon1 = radians(coord1[1])
    lat2 = radians(coord2[0])
    lon2 = radians(coord2[1])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))

    distance = R * c

    return distance

def standardize_address(address:str) -> str:
    """
        Function to standardize colombian addresses (mainly):
        Params:
            address: str. raw address to standardize.
    """
    address = address.lower()
    address = address.replace('.', '')
    address = address.replace('no ', '#')
    address = address.replace('dg', 'diagonal')

    # define regex to substitude keywords for whitespace
    re_gral = re.compile(r'local.*|of.*|oficina.*|pi.*|piso.*|cs.*|consultorio.*|consultorios.*')
    # define regex to susbstitude whitespaces doubles or triples... for a single one
    re_ws = re.compile(r'\s{2,}')

    address = re_gral.sub('', address)
    address = re_ws.sub('', address).strip()
    
    return address