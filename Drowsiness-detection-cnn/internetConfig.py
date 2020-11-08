import urllib.request

def connect():
    try:
        urllib.request.urlopen('http://google.com') 
        return True
    except:
        return False
print( 'Connected to Internet' if connect() else 'No Internet Available, Switching to offline service' )
