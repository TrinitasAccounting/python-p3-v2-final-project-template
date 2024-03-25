
from models.player import Player
from models.questions import Questions
from models.scores import Scores

from models.__init__ import CONN, CURSOR


if __name__ == "__main__":
    Questions.create_table()
    Player.create_table()

    CURSOR.execute("DELETE FROM questions")
    CURSOR.execute("DELETE FROM player")
    CONN.commit()


    Questions.create(1,"What color is the sky", "Blue", "Red", "Green", "Yellow")
    Questions.create(1,"Grass is what color", "Green", "Red", "Blue", "Yellow")
    Questions.create(2,"How much water is in my water bottle", "1 gallon", "2 gallon", "None", "I dont drink water")
    Questions.create(3,"Pounds to Kilograms", "2.2", "1.2", "1.6", "2.6")
    Questions.create(4,"First man on the moon", "Armstrong", "Carl", "Kevin", "Steve")

    Player.create("John Smith", 100, 777)




    # Questions.instance_from_db(1)