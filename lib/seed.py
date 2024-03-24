
from models.player import Player
from models.questions import Questions
from models.scores import Scores

from models.__init__ import CONN, CURSOR


if __name__ == "__main__":
    Questions.create_table()

    CURSOR.execute("DELETE FROM questions")
    CONN.commit()



    Questions.create(1,"What color is the sky", "Blue", "Red", "Green", "Yellow")



    # Questions.instance_from_db(1)