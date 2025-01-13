from pydantic import BaseModel
from logic.user_management import User, PlayList


class Songs(BaseModel):
    song_title: str = None
    song_performer: str = None
    song_genre: str = None
    song_year: int = None  # need to be int (in the swagger its str)
    song_rating: int = None
    rank: str = None
    op: str = None

    #Updates the Song object with data received from server response.
    def update_data(self, response_data: dict):
        data = response_data.get("data", {})

        # Map server response fields to object fields
        if "title" in data:
            self.song_title = data["title"]
        if "performer" in data:
            self.song_performer = data["performer"]
        if "genre" in data:
            self.song_genre = data["genre"]
        if "year" in data:
            self.song_year = data["year"]
        if "rating" in data:
            self.song_rating = data["rating"]

        return self




    #Prepares the data for adding a new song to the system.
    def prepare_add_song_request(self):
        return {
            "song_title": self.song_title,
            "song_performer": self.song_performer,
            "song_genre": self.song_genre,
            "song_year": self.song_year
        }

    # Prepares the data for upvote/downvote requests.
    def prepare_vote_request(self , user : User , playlist : PlayList ):
        return {
            "playlist_name": playlist.playlist_name,
            "song_title": self.song_title,
            "user_name": user.user_name,
            "user_password": user.user_password,
        }

    # Prepares parameters for getting song information.
    def prepare_get_song_params(self):
        return {
            "song_title": self.song_title
        }

    def prepare_ranked_songs_params(self):
        """Prepares parameters for getting ranked songs."""
        return {
            "rank": self.rank,
            "op": self.op
        }


    def to_json(self):
        j=(self.model_dump())
        return j


