
from models.__init__ import CONN, CURSOR

class High_Scores:
    
    all = []

    def __init__ (self, name, highest_level, final_score):
        self.name = name
        self.highest_level = highest_level
        self.final_score = final_score
        self.id = None

    # __________Make the properties for each if neccessary



    @classmethod
    def create_table(cls):
        # creates a new table for players
        sql = """ 
            CREATE TABLE IF NOT EXISTS high_scores (
                id INTEGER PRIMARY KEY,
                name TEXT,
                highest_level INTEGER,
                final_score INTEGER) 
        """

        CURSOR.execute(sql)


    @classmethod
    def drop_table(cls):
        #drop the table that persists player data
        sql = """ 
            DROP TABLE IF EXISTS high_scores;
        """

        CURSOR.execute(sql)


    def save(self):
        # insert a new row into the database
        sql = """ 
            INSERT INTO high_scores (name, highest_level, final_score)
            VALUES (?,?,?)
        """

        CURSOR.execute(sql, (self.name, self.highest_level, self.final_score))
        CONN.commit()

        self.id = CURSOR.lastrowid

        High_Scores.all.append(self)

    @classmethod
    def create(cls, name, highest_level, final_score):
        #Initialize the new created player high score
        player1 = cls(name, highest_level, final_score)
        player1.save()
        return player1



    @classmethod
    def instance_from_db(cls, row):
        #returns a play object from the database
        player_score = cls(row[1], row[2], row[3])
        player_score.id = row[0]
        return player_score

    
    @classmethod
    def get_all(cls):
        #return a list containing a players score object per row
        sql = """ 
            SELECT * 
            FROM high_scores
        """

        rows = CURSOR.execute(sql).fetchall()

        cls.all = [cls.instance_from_db(row) for row in rows]
        return cls.all


    @classmethod
    def get_top_five(cls):
        #return a list containing a players score object per row
        sql = """ 
            SELECT * 
            FROM high_scores
            ORDER BY final_score DESC
            LIMIT 5
        """

        rows = CURSOR.execute(sql).fetchall()

        cls.all = [cls.instance_from_db(row) for row in rows]
        return cls.all


    @classmethod
    def minimum_of_top_five(cls):
        list_of_high_scores = cls.get_top_five()
        lowest_score = list_of_high_scores[4]

        print(lowest_score)



    @classmethod
    def find_by_id(cls, id):
        #return a players score object that corresponds to the id given
        sql = """ 
            SELECT * 
            FROM high_scores
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()

        if row:
            return cls.instance_from_db(row)
        else: 
            return None


    def update(self):
        #update the table row corresponding to the current Players score
        sql = """ 
            UPDATE high_scores
            SET name = ?, highest_level = ?, final_score = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.name, self.highest_level, self.final_score, self.id))
        CONN.commit()


    def delete(self):
        #Deletes a row from the table
        sql = """ 
            DELETE FROM high_scores
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        High_Scores.all = [player for player in High_Scores.all if player.id != self.id]



    def __repr__ (self):
        return (f'id: {self.id}    Player: {self.name}    Level: {self.highest_level}   Final Score: {self.final_score}\n')
