import streamlit as st
import math
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="myApp")

# Initialization
if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

st.subheader("Find approximate distance between two locations")

def haversine (lat1, lon1, lat2, lon2):
    # distance between latitudes and longitudes
    dLat = (lat2 - lat1) * math.pi / 180.00
    dLon = (lon2 - lon1) * math.pi / 180.00

    # Convert to radians
    lat1 = (lat1) * math.pi / 180.00
    lat2 = (lat2) * math.pi / 180.00

    # apply formulae
    a = (pow(math.sin(dLat / 2), 2) +
         pow(math.sin(dLon / 2), 2) *
         math.cos(lat1) * math.cos(lat2));
    rad = 6371
    c = 2 * math.asin(math.sqrt(a))
    return rad * c


st.text_input(label="Enter address of first location", key='location1')
st.text_input(label="Enter address of second location", key='location2')

location1_geo = geolocator.geocode(st.session_state["location1"])
location2_geo = geolocator.geocode(st.session_state["location2"])


if (location1_geo is not None) & (location2_geo is not None):
    lat1 = location1_geo.latitude
    lon1 = location1_geo.longitude

    lat2 = location2_geo.latitude
    lon2 = location2_geo.longitude

    location_difference = round(haversine(lat1, lon1, lat2, lon2) / 1.609344, 2)

    location_difference = "The approximate distance is " + str(location_difference) + " Miles"

    st.text(location_difference)


#st.write(st.session_state)