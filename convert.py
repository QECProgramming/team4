
import mapbox

geocoder = mapbox.Geocoder(access_token = 'pk.eyJ1IjoiYW5kcmV3Y3JhbXAiLCJhIjoiY2pvdmw4NzhoMThhczNrbzR4d2x0bGVhdyJ9.sc2tMk0EWnPkeCJWALbQ0g')

# param: address - street adress as string 
# return: coordinates [longitude, latitude]
def convert(address):
    #use mapbox api to geocde addres
    _response = geocoder.forward(address, country = ['ca'])
    #get coordinates from json output
    _coordinates = _response.geojson()['features'][0]['geometry']['coordinates']
    return(_coordinates)
print(convert("99 university Ave, Kingston ON"))
  

