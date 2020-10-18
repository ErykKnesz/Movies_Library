import random

library = []

class Movie:
    def __init__ (self, title, year, genre, plays):
        self.title = title
        self.year = year
        self.genre = genre
        self.plays = plays
    
    def play(self):
        self.plays += 1

    def __str__(self):
        return f"{title} {year}"

class Series:
    def __init__(self, episode, season, *args, *kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season

    def __str__(self):
        return f"{title} S{season}E{episode}"