
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
    Questions.create(3,"Pounds to Kilograms", "2.2", "1.2", "1.6", "2.6")
    Questions.create(6,"What does the latin phrase 'bona fide' mean?", "in good faith", "to be bound", "will not stand for", "absolute disgust")
    Questions.create(5,"What country does not border Romania", "Croatia", "Slovakia", "Bulagria", "Ukraine")
    Questions.create(5,"How many people live in Germany", "83.2 million", "108.7 million", "114.4 million", "98.3 million")
    Questions.create(4,"Craigslist is named after its found. What is Craig's last name?", "Newmark", "Listerin", "Bolton", "Youshiem")
    Questions.create(3,"Who killed Julius Ceaser", "Brutus", "Duinis", "Tylor", "Blentin")
    Questions.create(3,"How many countries share the internation space station", "15", "8", "5", "11")
    Questions.create(2,"How many feet are in a mile", "5280", "5080", "4740", "3305")
    Questions.create(2,"How many yards are in a mile", "1740", "1620", "2010", "1487")
    Questions.create(6,"What year did Finland become a country", "1917", "1851", "1889", "1732")
    Questions.create(7,"The world capital cities of Vienna, Bratislava, and Budapest all lie along what river?", "Donube", "Jordan", "Tiger", "Yuli")
    Questions.create(7,"When ignoring the stem, how many points does the maple leaf on the Canadian flag have?", "11", "5", "7", "9")
    Questions.create(8,"1987 was the first time in 13 years that what American woman did not win a tennis grand slam?", "Chris Evert", "Cindy Scott", "Sarah Dennis", "Beverly Washington")
    Questions.create(9,"Known as 'The God of Cricket' what former indian cricketer is widely regarded as one of the greatest batsmen in the history of the sport and the highest run scorer of all time?", "Sachin Tendulkar", "Rahul David", "Virender Sehwag", "Virat Kohli")
    Questions.create(10,"What geological time period that began 358.9 million years ago, during which large coal deposits formed, has a name derived from the latin for 'coal-bearing'", "Carboniferous", "BuroCi", "Supericus-Flat", "Boron-vide")
    Questions.create(4,"Which metal has the chemical symbol 'Fe'", "Iron", "Copper", "Lead", "Zinc")
    Questions.create(4,"Where is Angel Falls, the world's largest waterfall located", "Venezuela", "Argentina", "Bolivia", "Peru")

    # Player.create("John Smith", 100, 777)

    # High_Scores.create("Clay", 2, 100)
    # High_Scores.create("Clay", 3, 200)
    # High_Scores.create("Kevin", 3, 200)
    # High_Scores.create("Trey", 9, 800)
    # High_Scores.create("Sarah", 3, 200)
    # High_Scores.create("Erica", 7, 600)
    # High_Scores.create("Carl", 1, 0)

