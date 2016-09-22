#credentials
client_id = "228256"
client_secret = "11462f9d222a1783940251b0c5e8af3b"
access_token = ""
refresh_token = ""


from flask import Flask
import base64
import requests #down
import json #down
app = Flask(__name__)

oauth_uri = "https://www.fitbit.com/oauth2/authorize?response_type=code&client_id=228256&redirect_uri=http%3A%2F%2Fchawlamit.myddns.me%3A5000&scope=activity%20heartrate%20location%20nutrition%20profile%20settings%20sleep%20social%20weight&expires_in=604800"
redirect_uri = http://chawlamit.myddns.me:5000
token_uri = "https://api.fitbit.com/oauth2/token"

@app.route('/')
def firstTime():

@app.route('/<string:access_code>')
def getAccessToken():
    if access_code:
        headers = {"Authorization":"Basic " +  base64.b64encode(client_id + ":" + client_secret), "content-type":"application/x-www-form-urlencoded"}
        body = {"client_id":client_id, "grant_type":"authorization_code", "code":access_code, "redirect_uri":redirect_uri}
        r = request.post(token_uri, headers=headers, data=body)
        content = json.loads(r.content)
        access_token = content['access_token']
        refresh_token = content['refresh_token']
        print access_token
        }

    else:
        #user comes for the first time
        return redirect(oauth_uri, code=302)
