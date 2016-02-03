__author__ = 'Jessy'


import sqlite3

from tkinter import*

database_filename = "Hockey_sql.db"


class hyGUI(Frame):

    def __init__(self):


        Frame.__init__(self)
        self.master.title("Hockey team Data")

        self.master.maxsize(600, 530)
        self.pack()


        self.gameLocationLabel = Label(self, text = "Enter game location")
        self.gameLocationLabel.pack()

        self.gameLocationVar = StringVar()
        self.gameLocationEntry = Entry(self, textvariable = self.gameLocationVar, width=30)
        self.gameLocationEntry.pack()



        self.gameDateLabel = Label(self, text = "Enter game date")
        self.gameDateLabel.pack()

        self.gameDateVar = StringVar()
        self.gameDateEntry = Entry(self, textvariable = self.gameDateVar, width = 30)
        self.gameDateEntry.pack()



        self.hatSoldLabel = Label(self, text = "Enter how many hats were sold")
        self.hatSoldLabel.pack()

        self.hatSoldVar = StringVar()
        self.hatSoldEntry = Entry(self, textvariable = self.hatSoldVar, width = 30)
        self.hatSoldEntry.pack()



        self.posterSoldLabel = Label(self, text = "Enter how many poster were sold")
        self.posterSoldLabel.pack()

        self.posterSoldVar = StringVar()
        self.posterSoldEntry = Entry(self, textvariable = self.posterSoldVar, width = 30)
        self.posterSoldEntry.pack()


        self.jerseySoldLabel = Label(self, text = "Enter how many jersey were sold")
        self.jerseySoldLabel.pack()

        self.jerseySoldVar = StringVar()
        self.jerseySoldEntry = Entry(self, textvariable = self.jerseySoldVar, width = 30)
        self.jerseySoldEntry.pack()


        self.hockeyStickSoldLabel = Label(self, text = "Enter how many hockey stick were sold")
        self.hockeyStickSoldLabel.pack()

        self.hockeyStickSoldVar = StringVar()
        self.hockeyStickSoldEntry = Entry(self, textvariable = self.hockeyStickSoldVar, width = 30)
        self.hockeyStickSoldEntry.pack()


        self._resultVar = StringVar()
        self._resultLabel = Label(self, text=" \n ", textvariable=self._resultVar)
        self._resultLabel.pack()



        self._addButton = Button(self, text="Add", command=self._add)
        self._addButton.pack()


        self._resultVar = StringVar()
        self._resultLabel = Label(self, text=" \n ", textvariable=self._resultVar)
        self._resultLabel.pack()


        self._addButton = Button(self, text="Delete", command=self._delete)
        self._addButton.pack()

        self._resultVar = StringVar()
        self._resultLabel = Label(self, text=" \n ", textvariable=self._resultVar)
        self._resultLabel.pack()



        self._exitButton = Button(self, text="Exit", command=self._exit)
        self._exitButton.pack()

        self._resultVar = StringVar()
        self._resultLabel = Label(self, text=" \n ", textvariable=self._resultVar)
        self._resultLabel.pack()



        self._salesButton = Button(self, text="Sales Table", command=self._sales)
        self._salesButton.pack()

        self._resultVar = StringVar()
        self._resultLabel = Label(self, text=" \n ", textvariable=self._resultVar)
        self._resultLabel.pack()



        self._gameButton = Button(self, text="Game Table", command=self._game)
        self._gameButton.pack()

        self._resultVar = StringVar()
        self._resultLabel = Label(self, text=" \n ", textvariable=self._resultVar)
        self._resultLabel.pack()


        self._itemButton = Button(self, text="Merchandise Table", command=self._item)
        self._itemButton.pack()



    def _add(self):
        pass


    def _delete(self):
        pass

    def _exit(self):
        sys.exit()

    def _sales(self):
        pass

    def _game(self):
        pass

    def _item(self):
        pass







    def _quit(self):

        exit(0)



    def setupDataInput(self):
        gameLocation = self.gameLocationVar.get()
        gameDate = self.gameDateVar.get()
        hatSold = self.hatSoldVar.get()
        posterSold = self.posterSoldVar.get()
        jerseySold = self.jesrseySoldVar.get()
        hockyStick = self.hockyStickSoldVar()



        if gameLocation == "":
            print("Please enter a game location ")

        if gameDate == "":
            print("Please enter a game date ")

        if hatSold == "":
            print("Please enter a hat sold amount")

        if posterSold == "":
            print("Please enter a poster sold amount")

        if jerseySold == "":
            print("Please enter a jersey sold amount")

        if hockyStick == "":
            print("Please enter a hockey stick sold amount")








def setup_database():

    db = sqlite3.connect(database_filename)
    cursor = db.cursor()

    # Delete any existing data
    cursor.execute('DROP TABLE IF EXISTS gameTable')
    cursor.execute('DROP TABLE IF EXISTS salesTable')
    cursor.execute('DROP TABLE IF EXISTS itemTable')

    db.commit()

    # Create a database table with columns for user's name (name), user id (user),  and password (password)
    cursor.execute('CREATE TABLE gameTable (GameID integer primary key , location text, date text) ')
    cursor.execute('CREATE TABLE salesTable (SalesID integer primary key, TotalSales Real, GameIDs Integer, FOREIGN KEY(GameIDs) REFERENCES gameTable(GameID) ) ')
    cursor.execute('CREATE TABLE itemTable (ItemID integer primary key, Description text, Price Real) ')

    # Add some sample data. Note that the admin is the first entry in the table, as is often the case
    cursor.execute('''INSERT INTO gameTable VALUES ( '1', 'Denver', '2016-2-7') ''')
    cursor.execute('''INSERT INTO gameTable VALUES ( '2', 'Miami', '2016-1-19') ''')


    cursor.execute('''INSERT INTO salesTable VALUES ( '1', '$1178.09', '22') ''')
    cursor.execute('''INSERT INTO salesTable VALUES ( '2', '$4567.85','12' ) ''')

    # commit saves changes
    db.commit()

    # and then close the connection to the database.
    db.close()


def start_gui():

    hyGUI().mainloop()


def quit():

    sys.exit()


def main():
    setup_database()
    start_gui()


if __name__ == '__main__':
    main()






























