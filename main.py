from fastapi import FastAPI
from source.fetch import Fetch
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def root():
    return FileResponse("readme.md")


@app.get("/gameid/{game_id}")
def fetch_players(game_id: str):
    f = Fetch(game_id)
    player_data = f.players()
    return player_data
