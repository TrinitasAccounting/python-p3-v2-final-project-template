
from models.__init__ import CONN, CURSOR

class Questions:
    
    all = []

    def __init__(self, level, text, correct_answer, w_answer1, w_answer2, w_answer3):
        self.level = level
        self.text = text
        self.correct_answer = correct_answer
        self.w_answer1 = w_answer1
        self.w_answer2 = w_answer2
        self.w_answer3 = w_answer3
        self.id = None

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level_param):
        if(isinstance(level_param, int)) and (0 < level_param < 11):
            self._level = level_param
        else: 
            raise ValueError("Level has to be between 1 and 10")

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text_param):
        if(isinstance(text_param, str)):
            self._text = text_param
        else: 
            raise ValueError("Question text needs to be a string longer than 5 characters")
    

    # @property
    # def correct_answer(self):
    #     return self._correct_answer

    # @correct_answer.setter
    # def correct_answer(self, correct_answer_param):
    #     if(isinstance(correct_answer_param, str)):
    #         self._correct_answer = correct_answer_param
    #     else: 
    #         raise ValueError("The correct answer needs to be a string")


    # @property
    # def w_answer1(self):
    #     return self._correct_answer

    # @correct_answer.setter
    # def correct_answer(self, correct_answer_param):
    #     if(isinstance(correct_answer_param, str)):
    #         self._correct_answer = correct_answer_param
    #     else: 
    #         raise ValueError("The correct answer needs to be a string")




    # class ORM methods for SQL link

    @classmethod
    def create_table(cls):
        #new table that stores the instances of questions created
        sql = """
            CREATE TABLE IF NOT EXISTS questions (
                id INTEGER PRIMARY KEY,
                level INTEGER,
                text TEXT,
                correct_answer TEXT,
                w_answer1 TEXT,
                w_answer2 TEXT,
                w_answer3 TEXT)
            """

        CURSOR.execute(sql)


    @classmethod
    def drop_table(cls):
        #dropping the questions table
        sql = """
            DROP TABLE IF EXIST questions;
        """

        CURSOR.execute(sql)


    def save(self):
        # inserting a new row into our questions database
        sql = """ 
            INSERT INTO questions (level, text, correct_answer, w_answer1, w_answer2, w_answer3)
            VALUES (?,?,?,?,?,?)
        """

        CURSOR.execute(sql, (self.level, self.text, self.correct_answer, self.w_answer1, self.w_answer2, self.w_answer3))
        CONN.commit()

        self.id = CURSOR.lastrowid

        Questions.all.append(self)


    @classmethod
    def create(cls, level, text, correct_answer, w_answer1, w_answer2, w_answer3):
        # Creates a new instance of the questions class and saves the object
        question = cls(level, text, correct_answer, w_answer1, w_answer2, w_answer3)
        question.save()
        return question

    
# _________________I think this one isn't correct either
    @classmethod
    def instance_from_db(cls, row):
        # returns a object from the questions table matching the values
        question = cls(row[1], row[2], row[3], row[4], row[5], row[6])
        question.id = row[0]
        return question


    @classmethod
    def get_all(cls):
        # returns list containing a question object per row in the table
        sql = """ 
            SELECT *
            FROM questions
        """

        rows = CURSOR.execute(sql).fetchall()

        cls.all = [cls.instance_from_db(row) for row in rows]
        return cls.all

    
    @classmethod
    def find_by_id(cls, id):
        # return a question that corresponds to the table row that was input
        sql = """ 
            SELECT * 
            FROM questions 
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()

        if row:
            return cls.instance_from_db(row)
        else: 
            return None


#___________________________Wrong, need to watch the lectures to solve this_______________________________________
    def update (self):
        # Update the table row for a question instance
        sql = """ 
            UPDATE questions
            SET level = ?, text = ?, correct_answer = ?, w_answer1 = ?, w_answer2 = ?, w_answer3 = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.level, self.text, self.correct_answer, self.w_answer1, self.w_answer2, self.w_answer3, self.id))
        CONN.commit()


    def delete(self):
        #Delete the row corresponding to the current questions instance
        sql = """ 
            DELETE FROM questions
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        Questions.all = [question for question in Questions.all if question.id != self.id]



# This should be on the players class and selecting all questions corresponding to the current level the player is on. Then random integer filter the questions to output on
    # def player_level(self):
    #     from model.player import Player

    #     sql = """ 
    #         SELECT * 
    #         FROM 
    #     """

    @classmethod
    def find_by_level(cls, level):
        # return a question that corresponds to the table row that was input
        sql = """ 
            SELECT * 
            FROM questions 
            WHERE level = ?
        """

        rows = CURSOR.execute(sql, (level,)).fetchall()

        # cls.all = [cls.instance_from_db(row) for row in rows]
        # return cls.all

        return [Questions.instance_from_db(row) for row in rows]


    def __repr__ (self):
        return (f'____Level: {self.level}, Question => {self.text}____')











