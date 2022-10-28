# GameKings Player Data Pull

## About
This web app uses Python3 and FastAPI to pull player data for a specific game from DraftKings. The response is returned in JSON format. User needs to know the specific game ID. The app is deployed on Deta.

**To Do:**
- Invalid Game ID error Handling
- A filter for player data.

## How to Use
Make a HTTP request to `https://gk361ms.deta.dev/gameid/{game_id}` replacing `{game_id}` with the integer game id of the game on DraftKings with which you would like to pull player data from. The reponse returned will be in application/json form.

## Demo Usage
Using Python & Flask framework, here is a snippet of how the microservice may possibly used.

```
from flask import render_template
from app import app
import requests

@app.route('/')
def index():
    game_id = 134948844
    players_raw = requests.get('https://gk344ms.deta.dev/gameid/' + str(game_id))
    players = players_raw.json()
    return render_template('index.html', players=players) 
```


The template code snippet below renders the pulled player data into a table with the player's picture, name, and stats.
```
<!doctype html>
<html>
    <head>
        <title>Microservice Demo</title>
    </head>
    <body>
    {% for player in players %}
        <table>
        <tr>
            <td><img src="{{ player.playerImage50 }}" alt={{ player.displayName }}></td>
            <td>
                <h3>{{ player.displayName }}</h3>
                <h4>Stats</h4>
                <p><b>Position:</b>{{ player.position }}</p>
                <p><b>Salary:</b>{{ player.salary }}</p>
            </td>
        </tr>
        </table>
    {% endfor %}
    </body>
</html>
```

An image of what is output:
![Demo using the microservice](source\assets\demo.jpg)

## Credits
**Tutorials Referenced:**
1. [Unofficial Documentation for DraftKings](https://seandrummy.medium.com/unofficial-documentation-for-the-draft-kings-api-8830f8e8c7fc)
2. [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
3. [Deploying FastAPI on Deta](https://fastapi.tiangolo.com/deployment/deta/)
4. For error handling requests and general reference: [Build a Stock Data API Using Web Scraping and FastAPI](https://python.plainenglish.io/build-a-stock-data-api-using-web-scraping-and-fastapi-dcbcdbd3d2ec)
5. [Requests Documentation for JSON Response Content](https://requests.readthedocs.io/en/latest/user/quickstart/#json-response-content)
6. Referenced for the creation of the demo: [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
7. [How to Write a Good Readme File](https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/)
