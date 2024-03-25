
from models.__init__ import CONN, CURSOR

class Player:
    
    all = []

    def __init__ (self, name, question_level, current_score):
        self.name = name
        self.question_level = question_level
        self.current_score = current_score
        self.id = None

    # __________Make the properties for each if neccessary



    @classmethod
    def create_table(cls):
        # creates a new table for players
        sql = """ 
            CREATE TABLE IF NOT EXISTS player (
                id INTEGER PRIMARY KEY,
                name TEXT,
                question_level INTEGER,
                current_score INTEGER) 
        """

        CURSOR.execute(sql)


    @classmethod
    def drop_table(cls):
        #drop the table that persists player data
        sql = """ 
            DROP TABLE IF EXISTS player;
        """

        CURSOR.execute(sql)


    def save(self):
        # insert a new row into the database
        sql = """ 
            INSERT INTO player (name, question_level, current_score)
            VALUES (?,?,?)
        """

        CURSOR.execute(sql, (self.name, self.question_level, self.current_score))
        CONN.commit()

        self.id = CURSOR.lastrowid

        Player.all.append(self)

    @classmethod
    def create(cls, name, question_level, current_score):
        #Initialize the new created player
        player1 = cls(name, question_level, current_score)
        player1.save()
        return player1


    @classmethod
    def instance_from_db(cls, row):
        #returns a play object from the database
        player1 = cls(row[1], row[2], row[3])
        player1.id = row[0]
        return player1

    
    @classmethod
    def get_all(cls):
        #return a list containing a player object per row
        sql = """ 
            SELECT * 
            FROM player
        """

        rows = CURSOR.execute(sql).fetchall()

        cls.all = [cls.instance_from_db(row) for row in rows]
        return cls.all


    @classmethod
    def find_by_id(cls, id):
        #return a player object that corresponds to the id given
        sql = """ 
            SELECT * 
            FROM player
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()

        if row:
            return cls.instance_from_db(row)
        else: 
            return None


    def update(self):
        #update the table row corresponding to the current Player
        sql = """ 
            UPDATE player
            SET name = ?, question_level = ?, current_score = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.name, self.question_level, self.current_score, self.id))
        CONN.commit()


    def delete(self):
        #Deletes a row from the table
        sql = """ 
            DELETE FROM player
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        Player.all = [player for player in Player.all if player.id != self.id]


    # def questions_at_level(self):

    #     from models.questions import Questions

    #     sql = """ 
    #         SELECT * 
    #         FROM questions
    #         WHERE level = ?
    #     """

    #     rows = CURSOR.execute(sql, (level,)).fetchall()

    #     return [Questions.instance_from_db(row) for row in rows]

