# GameKings Player Data Pull

## About
This web app uses Python3 and FastAPI to pull player data for a specific game from DraftKings. The response is returned in JSON format. User needs to know the specific game ID. The app is deployed on Deta.

**To Do:**
- Invalid Game ID error Handling
- A filter for player data.

## How to Use
Make a HTTP request to `https://gk344ms.deta.dev/gameid/{game_id}` replacing `{game_id}` with the integer game id of the game on DraftKings with which you would like to pull player data from. The reponse returned will be in application/json form.