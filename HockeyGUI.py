__author__ = 'Jessy'



### For this project I got some help by a looking at other material URL source like
###     https://github.com/minneapolis-edu/sql_injection/blob/master/login.py

###     I also got some help from Mason from learning center and Boyd from my classmate to do this project

###  Importing tkinter to use GUI interface with Python code

###   Importing sqlite3 for database function




import sqlite3

from tkinter import*

##  importing Treeview from tkinter to display a database table on GUI Frame
from tkinter.ttk import Treeview


##    Database name

database_filename = "Hockey_sql.db"



##  Creating a GUI frame with
class hyGUI(Frame):


    def __init__(self):


        Frame.__init__(self)
        self.master.title("Hockey team Data")

        self.master.maxsize(1400, 1000)      ##  Maximum Frame size
        self.pack()
        self._treeview = Treeview(self)      ## initialize the treeview


##  Writing label on gui and creating a data insert box to get user input when clicking a button

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



##  Creating space between the button on the GUI interface
        self._resultVar = StringVar()
        self._resultLabel = Label(self, text=" \n ", textvariable=self._resultVar)
        self._resultLabel.pack()


##  Add button
        self._addButton = Button(self, text="Add", command=self._add)
        self._addButton.pack()


        self._resultVar = StringVar()
        self._resultLabel = Label(self, text=" \n ", textvariable=self._resultVar)
        self._resultLabel.pack()


## Delete button
        self._addButton = Button(self, text="Delete", command=self._delete)
        self._addButton.pack()

        self._resultVar = StringVar()
        self._resultLabel = Label(self, text=" \n ", textvariable=self._resultVar)
        self._resultLabel.pack()


## Exit button
        self._exitButton = Button(self, text="Exit", command=self._exit)
        self._exitButton.pack()

        self._resultVar = StringVar()
        self._resultLabel = Label(self, text=" \n ", textvariable=self._resultVar)
        self._resultLabel.pack()


## Best item sold button
        self._bestItemButton = Button(self, text="Best Item Sold", command=self._bestItem)
        self._bestItemButton.pack()

        self._resultVar = StringVar()
        self._resultLabel = Label(self, text=" \n ", textvariable=self._resultVar)
        self._resultLabel.pack()


##  Worst item sold button
        self._worstItemButton = Button(self, text="Worst Item Sold", command=self._worstItem)
        self._worstItemButton.pack()

        self._resultVar = StringVar()
        self._resultLabel = Label(self, text=" \n ", textvariable=self._resultVar)
        self._resultLabel.pack()


##  Best sales per game button
        self._itemButton = Button(self, text="Game for best Sales", command=self._item)
        self._itemButton.pack()


## this button is not packed but, it is needed to populate the table
        self._tableButton = Button(self, text = "Show the Complete table", command =self._maketable())



        self._resultVar = StringVar()
        self._resultLabel = Label(self, text=" \n ", textvariable=self._resultVar)
        self._resultLabel.pack()


##  Using empty sting label to display the different text on GUI Frame when clicking button
        self.resultBestLabel = Label(self, text = "")
        self.resultBestLabel.pack()


        self._treeview['columns']=('location', 'date', 'no_hats', 'val_hats', 'no_jerseys', 'val_jerseys',
                                   'no_hockstick', 'val_hockstick', 'no_posters', 'val_posters','total_sales')


##  Creating a columns name heading for the table
        self._treeview.heading('location', text = "Location")
        self._treeview.column('#0', width = 0)
        self._treeview.heading('date', text = "Date")
        self._treeview.heading('no_hats', text = "# hats")
        self._treeview.heading('val_hats', text = "$ hats")
        self._treeview.heading('no_jerseys', text = "# jerseys")
        self._treeview.heading('val_jerseys', text = "$ jerseys")
        self._treeview.heading('no_hockstick', text = "# hockey stick")
        self._treeview.heading('val_hockstick', text = "$ hockey stick")
        self._treeview.heading('no_posters', text = "# posters")
        self._treeview.heading('val_posters', text = "$ posters")
        self._treeview.heading('total_sales', text = "Total Sales")

##  The column size is 100
        for item in self._treeview['columns']:
            self._treeview.column(item, width = 100)


        self._treeview.pack()



##
    def _maketable(self):
        makeTableDatabase(self)







## when clicking add button with the user input, it will get the user input and add the data to the database

    def _add(self):
        location = self.gameLocationVar.get()
        date = self.gameDateVar.get()
        hat = self.hatSoldVar.get()
        jersey = self.jerseySoldVar.get()
        stick = self.hockeyStickSoldVar.get()
        poster = self.posterSoldVar.get()

        hatTotal = int(hat) * 20         ## Calculate hat quantity sold with hat retail price of $20
        jerseyTotal = int(jersey) * 40   ## Calculate jersey quantity sold with jersey retail price of $20
        stickTotal = int(stick) * 30     ## Calculate hockey stick quantity sold with hockey stick retail price of $20
        posterTotal = int(poster) * 10   ## Calculate poster quantity sold with poster retail price of $20

        TotalSales = posterTotal + stickTotal + jerseyTotal + hatTotal   # calculation of total sales of the game


##  Calling add_data method with the user input and calculated value to a add a data to a database
        add_data(location, date, hat, hatTotal, jersey, jerseyTotal, stick, stickTotal, poster, posterTotal, TotalSales)

##  update the data on the table
        update_table(self)



##  when delete button is pressed, it will call deleteData method
    def _delete(self):
        deleteData(self)


#  when exit button is clicked, the GUI frame close
    def _exit(self):
        sys.exit()


# when best item button is clicked, it will calculate the best item sold amount per game
    def _bestItem(self):
        bestItem(self)




# when worst item button is clicked, it will calculate the worst item sold amount per game

    def _worstItem(self):
        worstItem(self)


#  when game for best sales button were clicked, it will display the game location
#  for the best total sales per game
    def _item(self):
        bestSalesGame(self)




#  method to get total sales  for each game and display the result on the GUI
def bestSalesGame(self):

    db = sqlite3.connect(database_filename)

    cursor = db.cursor()

##   Selecting game location and total sales amount from the hockey table, where the maximum totals sales from all the game
##   And display the game location and total sales for the game location on the label format on the GUI Frame

    cursor.execute('SELECT location, totalSales FROM hockeyTable WHERE totalSales IN (SELECT MAX(totalSales) FROM hockeyTable)')

    db.commit()

    rows = cursor.fetchall()
    db.close()

    item = rows[0]

    self.resultBestLabel['text']= "The maximum sales were at the {} location which had ${} total sales".format(item[0], item[1])



##   making the database table display on Treeview
def makeTableDatabase(self):
    db = sqlite3.connect(database_filename)
    cursor = db.cursor()
    cursor.execute("Select * from hockeyTable")
    rows = cursor.fetchall()
    db.close()

##  inserting the data into a Treeview to be displayed
    for row in rows:
        self._treeview.insert('', 'end', values = row)




##  updating the data on the table
def update_table(self):

    ##  delete every data from the table and inserting updated data to the table

    for item in self._treeview.get_children():
        self._treeview.delete(item)

    db = sqlite3.connect(database_filename)
    cursor = db.cursor()
    cursor.execute("Select * FROM hockeyTable")
    rows = cursor.fetchall()
    db.close()

##  inserting new updated data to the treeview table
    for row in rows:
        self._treeview.insert('', 'end', values = row)





##  method to Delete last row from hockey table in the database

def deleteData(self):

    db = sqlite3.connect(database_filename)
    cursor = db.cursor()


##  Delete a row that has a maximum ROW ID number for the table
    cursor.execute('DELETE FROM hockeyTable WHERE ROWID = (SELECT MAX(ROWID) FROM hockeyTable)')

    db.commit()  # make change to the database

    cursor.execute('SELECT * FROM hockeyTable')

    rows = cursor.fetchall()
    print(rows)

    db.close()

    update_table(self)





###  Creating a table called "hockeyTable" and inserting a data into hockeyTable table
def setup_database():

    global db, cursor, rows
    db = sqlite3.connect(database_filename)
    cursor = db.cursor()

    # Delete any existing data
    cursor.execute('DROP TABLE IF EXISTS hockeyTable')

    db.commit()

    # Create a database table called "hockeyTable" with a column name - location, date, hatSold, hatSales, jerseySold,
    #  jerseySales, stickSold, stickSales, posterSold, posterSales and totalSales

    cursor.execute('CREATE TABLE hockeyTable (location text, date text, hatSold Integer,'
                   ' hatSales Integer, jerseySold Integer, jerseySales Integer, stickSold Integer, stickSales Integer,'
                   ' posterSold Integer, posterSales Integer, totalSales Integer)')



##  Inserting data to a table

    cursor.execute('''INSERT INTO hockeyTable VALUES ( 'Denver', '1/7/2016', 2, 40, 4, 160, 3, 90, 5, 50, 340) ''')
    cursor.execute('''INSERT INTO hockeyTable VALUES ( 'Minneapolis', '2/2/2016', 1, 20, 5, 200, 2, 60, 7, 70, 350) ''')
    cursor.execute('''INSERT INTO hockeyTable VALUES ( 'Atlanta', '12/20/2015', 3, 60, 3, 120, 6, 180 , 4, 40, 400 )''')

    cursor.execute('''INSERT INTO hockeyTable VALUES ( 'Portland', '1/5/2016', 5, 100, 7, 280, 1, 30, 3, 30, 440) ''')
    cursor.execute('''INSERT INTO hockeyTable VALUES ( 'Vancouver', '2/2/2016', 0, 0, 1, 40, 7, 210, 8, 80, 330) ''')
    cursor.execute('''INSERT INTO hockeyTable VALUES ( 'Toronto', '12/20/2015', 7, 140, 8, 320, 4, 120 , 2, 20, 600)''')



    # commit saves changes
    db.commit()

###   printing the instruction on how to look at th e values on the database

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



##    Adding the user data input to the database "hockeyTable"
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




## Calculate the best item quantity amount sold from the entire game
def bestItem(self):


    max =0

    string = ""


    db = sqlite3.connect(database_filename)
    cursor = db.cursor()

    # Calculate the total number of item quantity sold for each item from the hockeyTable
    # And display the best item of quantity sold on the GUI Frame
    cursor.execute('SELECT SUM(hatSold) AS hatTotalSold, SUM(jerseySold) AS jerseyTotalSold, SUM(stickSold) AS stickTotalSold, SUM(posterSold) AS posterTotalSold FROM hockeyTable');

    db.commit()

    rows = cursor.fetchall()
    print(rows)

##  Comparing the each SUM value of item quantity sold

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


##  display the best item sold on GUI
    self.resultBestLabel['text']= string

    db.close()



##  find worst item quantity sold from "hockeyTable"
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






























