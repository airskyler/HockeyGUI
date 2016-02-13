__author__ = 'Jessy'


import sqlite3

from tkinter import*

database_filename = "Hockey_sql.db"


class hyGUI(Frame):

    def __init__(self):


        Frame.__init__(self)
        self.master.title("Hockey team Data")

        self.master.maxsize(800, 800)
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



        self._bestItemButton = Button(self, text="Best Item Sold", command=self._bestItem)
        self._bestItemButton.pack()

        self._resultVar = StringVar()
        self._resultLabel = Label(self, text=" \n ", textvariable=self._resultVar)
        self._resultLabel.pack()



        self._worstItemButton = Button(self, text="Worst Item Sold", command=self._worstItem)
        self._worstItemButton.pack()

        self._resultVar = StringVar()
        self._resultLabel = Label(self, text=" \n ", textvariable=self._resultVar)
        self._resultLabel.pack()


        self._itemButton = Button(self, text="Game for best Sales", command=self._item)
        self._itemButton.pack()


        self._resultVar = StringVar()
        self._resultLabel = Label(self, text=" \n ", textvariable=self._resultVar)
        self._resultLabel.pack()



        self.resultBestLabel = Label(self, text = "")
        self.resultBestLabel.pack()








    def _add(self):
        location = self.gameLocationVar.get()
        date = self.gameDateVar.get()
        hat = self.hatSoldVar.get()
        jersey = self.jerseySoldVar.get()
        stick = self.hockeyStickSoldVar.get()
        poster = self.posterSoldVar.get()
        hatTotal = int(hat) * 20
        jerseyTotal = int(jersey) * 40
        stickTotal = int(stick) * 30
        posterTotal = int(poster) * 10
        TotalSales = posterTotal + stickTotal + jerseyTotal + hatTotal


        add_data(location, date, hat, hatTotal, jersey, jerseyTotal, stick, stickTotal, poster, posterTotal, TotalSales)



    def _delete(self):
        deleteData(self)


    def _exit(self):
        sys.exit()

    def _bestItem(self):
        bestItem(self)


    def _worstItem(self):
        worstItem(self)


    def _item(self):


        bestSalesGame(self)



def bestSalesGame(self):


    max =0

    string = ""


    db = sqlite3.connect(database_filename)

    cursor = db.cursor()


    cursor.execute('SELECT totalSales FROM hockeyTable')

    db.commit()

    rows = cursor.fetchall()
    print(rows)

    if rows[0][0]> max:
        max = rows[0][0]

        string = "The best game sale is "+str(max)+""



    if rows[0][1]> max:
        max = rows[0][1]

        string = "The best game sale is "+str(max)+""



    if rows[0][2]> max:
        max = rows[0][2]

        string = "The best game sale is "+str(max)+""


    if rows[0][3] > max:
        max = rows[0][3]

        string = "The best game sale is  "+str(max)+""


    if rows[0][4] > max:
        max = rows[0][4]

        string = "The best game sale is "+str(max)+""


    if rows[0][5] > max:
        max = rows[0][5]

        string = "The best game sale is  "+str(max)+""


    if rows[0][6] > max:
        max = rows[0][6]

        string = "The best game sale is "+str(max)+""


    if rows[0][7] > max:
        max = rows[0][7]

        string = "The best game sale is  "+str(max)+""



    if rows[0][8] > max:
        max = rows[0][8]

        string = "The best game sale is  "+str(max)+""


    if rows[0][9] > max:
        max = rows[0][9]

        string = "The best game sale is  "+str(max)+""



    if rows[0][10] > max:
        max = rows[0][10]

        string = "The best game sale is  "+str(max)+""



    self.resultBestLabel['text']= string


    db.close()








def deleteData(self):

    db = sqlite3.connect(database_filename)
    cursor = db.cursor()



    cursor.execute('DELETE FROM hockeyTable WHERE ROWID = (SELECT MAX(ROWID) FROM hockeyTable)')

    db.commit()

    cursor.execute('SELECT * FROM hockeyTable')

    rows = cursor.fetchall()
    print(rows)

    db.close()






def setup_database():

    global db, cursor, rows
    db = sqlite3.connect(database_filename)
    cursor = db.cursor()

    # Delete any existing data
    cursor.execute('DROP TABLE IF EXISTS hockeyTable')

    db.commit()

    # Create a database table with columns for user's name (name), user id (user),  and password (password)
    cursor.execute('CREATE TABLE hockeyTable (location text, date text, hatSold Integer,'
                   ' hatSales Integer, jerseySold Integer, jerseySales Integer, stickSold Integer, stickSales Integer,'
                   ' posterSold Integer, posterSales Integer, totalSales Integer)')




    cursor.execute('''INSERT INTO hockeyTable VALUES ( 'Denver', '1/7/2016', 2, 40, 4, 160, 3, 90, 5, 50, 340) ''')
    cursor.execute('''INSERT INTO hockeyTable VALUES ( 'Minneapolis', '2/2/2016', 1, 20, 5, 200, 2, 60, 7, 70, 350) ''')
    cursor.execute('''INSERT INTO hockeyTable VALUES ( 'Atlanta', '12/20/2015', 3, 60, 3, 120, 6, 180 , 4, 40, 400 )''')

    cursor.execute('''INSERT INTO hockeyTable VALUES ( 'Portland', '1/5/2016', 5, 100, 7, 280, 1, 30, 3, 30, 440) ''')
    cursor.execute('''INSERT INTO hockeyTable VALUES ( 'Vancouver', '2/2/2016', 0, 0, 1, 40, 7, 210, 8, 80, 330) ''')
    cursor.execute('''INSERT INTO hockeyTable VALUES ( 'Toronto', '12/20/2015', 7, 140, 8, 320, 4, 120 , 2, 20, 600)''')



    # commit saves changes
    db.commit()
    print("Instruction for understanding the value on the data table below \n\n First value is shown the location of the game \n"
          " Second value is a date of Game \n Third value is quantity of hat sold \n Forth value is a calculated value of hat sales from the game \n"
          " Fifth value is quantity of jersey sold \n Sixth value is a calculated value of a jersey sales  \n"
          " Seventh value is hockey stick quantity sold \n Eight value is a calculated value of a hockey stick sales \n "
          "Ninth value is a poster quantity sold \n Tenth value is a calculated value of poster sales \n"
          " Eleventh is a calculated total sales of the game"
    )

    cursor.execute('SELECT * FROM hockeyTable')
    rows = cursor.fetchall()
    print(rows)

    # and then close the connection to the database.
    db.close()

    start_gui()




def add_data( gameLocation, gameDate, hat, hatTotal, jersey, jerseyTotal, stick, stickTotal, poster, posterTotal, totalSales ):
    db = sqlite3.connect(database_filename)

    cursor = db.cursor()

    cursor.execute('INSERT OR IGNORE INTO hockeyTable VALUES (?,?,?,?,?,?,?,?,?,?,?)',
                   (gameLocation,gameDate, hat, hatTotal, jersey, jerseyTotal, stick, stickTotal, poster, posterTotal, totalSales))
    db.commit()
    cursor.execute('SELECT * FROM hockeyTable')

    rows = cursor.fetchall()
    print(rows)
    db.close()



def bestItem(self):


    max =0

    string = ""


    db = sqlite3.connect(database_filename)
    cursor = db.cursor()

    # Delete any existing data
    cursor.execute('SELECT SUM(hatSold) AS hatTotalSold, SUM(jerseySold) AS jerseyTotalSold, SUM(stickSold) AS stickTotalSold, SUM(posterSold) AS posterTotalSold FROM hockeyTable');

    db.commit()

    rows = cursor.fetchall()
    print(rows)



    if rows[0][0]> max:
        max = rows[0][0]

        string = "The hat sold the most with the quantity of "+str(max)+""



    if rows[0][1]> max:
        max = rows[0][1]

        string = "The jersey sold the most with the quantity of "+str(max)+""



    if rows[0][2]> max:
        max = rows[0][2]

        string = "The hockey stick sold the most with the quantity of "+str(max)+""


    if rows[0][3] > max:
        max = rows[0][3]

        string = "The poster sold the most with the quantity of "+str(max)+""



    self.resultBestLabel['text']= string



    db.close()



def worstItem(self):


    minn = 1000

    string = ""


    db = sqlite3.connect(database_filename)
    cursor = db.cursor()

    # Delete any existing data
    cursor.execute('SELECT SUM(hatSold) AS hatTotalSold, SUM(jerseySold) AS jerseyTotalSold, SUM(stickSold) AS stickTotalSold, SUM(posterSold) AS posterTotalSold FROM hockeyTable');

    db.commit()

    rows = cursor.fetchall()
    print(rows)



    if rows[0][0]< minn:
        minn = rows[0][0]

        string = "The hat sold the least with a quantity of "+str(minn)+""



    if rows[0][1]< minn:
        minn = rows[0][1]

        string = "The jersey sold the least with a quantity of "+str(minn)+""



    if rows[0][2]< minn:
        minn = rows[0][2]

        string = "The hockey stick sold the least with a quantity of "+str(minn)+""


    if rows[0][3] < minn:
        minn = rows[0][3]

        string = "The poster sold the least with a quantity of "+str(minn)+""



    self.resultBestLabel['text']= string



    db.close()







def start_gui():

    hyGUI().mainloop()



def main():
    setup_database()
    start_gui()


if __name__ == '__main__':
    main()






























