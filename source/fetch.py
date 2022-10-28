import requests


class Fetch():

    def __init__(self, game_id):
        """ Initializes Fetch class """
        self._draftid = None    # draftGroupId
        self._g_res = {}        # JSON result of game ID
        self._p_res = {}        # JSON result of draftGroupId
        self._game_url = "https://api.draftkings.com/contests/v1/contests/" + str(game_id) + "?format=json"

    def get_game(self):
        """ Retrieves JSON file for requested group ID """
        g = requests.get(self._game_url)
        if (g.url != self._game_url):
            raise requests.TooManyRedirects()

        if g.status_code == 200:
            result = g.json()
        else:
            g.raise_for_status()

        self._g_res = result

    def get_draft(self):
        """ Retrieves draftGroupId from self._g_res """
        self.get_game()     # update self._g_res
        self._draftid = str(self._g_res["contestDetail"]["draftGroupId"])

    def players(self):
        """ Returns JSON of player data in draft group """
        self.get_draft()    # update self._draftid

        draft_url = "https://api.draftkings.com/draftgroups/v1/draftgroups/" + self._draftid + "/draftables"
        
        d = requests.get(draft_url)
        if (d.url != draft_url):
            raise requests.TooManyRedirects()

        if d.status_code == 200:
            result = d.json()
        else:
            d.raise_for_status()
        return result["draftables"]

