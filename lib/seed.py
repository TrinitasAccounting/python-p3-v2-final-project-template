
from models.player import Player
from models.questions import Questions
from models.high_scores import High_Scores


from models.__init__ import CONN, CURSOR


if __name__ == "__main__":
    Questions.create_table()
    Player.create_table()
    High_Scores.create_table()

    CURSOR.execute("DELETE FROM questions")
    CURSOR.execute("DELETE FROM player")
    # CURSOR.execute("DELETE FROM high_scores")
    CONN.commit()


    Questions.create(1,"What color is the sky", "Blue", "Red", "Green", "Yellow")
    Questions.create(1,"Grass is what color", "Green", "Red", "Blue", "Yellow")
    Questions.create(1,"What color is the Sun", "Yellow", "Red", "Blue", "Yellow")
    Questions.create(1,"How many seasons are there", "4", "2", "5", "There are no seasons thats absolutely nuts")
    Questions.create(2,"How much water is in my water bottle", "1 gallon", "2 gallon", "None", "I dont drink water")
    Questions.create(3,"Pounds to Kilograms", "2.2", "1.2", "1.6", "2.6")
    Questions.create(4,"First man on the moon", "Armstrong", "Carl", "Kevin", "Steve")
    Questions.create(5,"First man on the moon", "Armstrong", "Carl", "Kevin", "Steve")
    Questions.create(6,"First man on the moon", "Armstrong", "Carl", "Kevin", "Steve")
    Questions.create(7,"First man on the moon", "Armstrong", "Carl", "Kevin", "Steve")
    Questions.create(8,"First man on the moon", "Armstrong", "Carl", "Kevin", "Steve")
    Questions.create(9,"First man on the moon", "Armstrong", "Carl", "Kevin", "Steve")
    Questions.create(10,"First man on the moon", "Armstrong", "Carl", "Kevin", "Steve")
    

    Player.create("John Smith", 100, 777)

    # High_Scores.create("Clay", 1, 100)
    # High_Scores.create("Clay", 2, 200)
    # High_Scores.create("Kevin", 2, 200)
    # High_Scores.create("Trey", 8, 800)
    # High_Scores.create("Sarah", 3, 300)
    # High_Scores.create("Erica", 6, 600)
    # High_Scores.create("Carl", 1, 100)




    # Questions.instance_from_db(1)