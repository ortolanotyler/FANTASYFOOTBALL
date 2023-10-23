from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

# Define the API URL and your API key
API_URL = "https://api.sportsdata.io/v3/nfl/projections/json/PlayerSeasonProjectionStatsByPlayerID"
API_KEY = "d8858b65be5e4f86af2f894c06ea0293"  

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        player_id = request.form.get("player_id")
        if player_id:
            # Make a request to the NFL API with the player ID
            url = f"{API_URL}/2023/{player_id}?key={API_KEY}"
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                return render_template("result.html", data=data)
            else:
                error_message = "Error: Unable to retrieve data from the API."
                return render_template("index.html", error_message=error_message)
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001)


