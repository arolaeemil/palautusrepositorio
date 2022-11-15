from playerreader import PlayerReader

class PlayerStats:
    def __init__(self, reader: PlayerReader):
        self.reader = reader
    
    def top_scorers_by_nationality(self, nationality):
        playerlist = self.reader.get_players()
        returnlist = []
        for player in playerlist:
            if player.nationality == nationality:
                returnlist.append(player)
        returnlist.sort(reverse=True)
        return returnlist