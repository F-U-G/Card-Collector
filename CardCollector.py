import sqlite3

#Id index
COUNT_INDEX = 5

def searchCards(cursor):
    #get user input for name then search table for name
    cardList = []
    searchName = '%' + input("Enter card name: ") + '%'
    for row in cursor.execute("SELECT * FROM cards WHERE name LIKE ?", (searchName,)):
        cardList.append(row)
    print("ID | Name | Set | Number | Type | Count ")
    for card in cardList:
        print(card)


def main():
    #open database
    db = sqlite3.connect("collection.db")
    while True:
        #create cursor
        cursor = db.cursor()

        #get user input print options for user
        print("Options: [a] add card, [r] remove card, [d] display cards, [sq] save and quit, [q] quit without saving")
        option = input("Enter option: ")

        #add card
        if option == 'a':
            print("Add card, q to cancel")
            cName = "'" + input("Enter card name: ") + "'"
            if cName == "'q'":
                continue
            cSet = "'" + input("Enter set name: ") + "'"
            if cSet == "'q'":
                continue
            cNumber = "'" + input("Enter card number: ") + "'"
            if cNumber == "'q'":
                continue
            cType = "'" + input("Enter card typing/color: ") + "'"
            if cType == "'q'":
                continue
            try:
                cCount = int(input("How many of this card: "))
            except:
                continue
            try:
                cursor.execute("INSERT INTO cards (name, setName, cardNumber, type, count) VALUES (?, ?, ?, ?, ?);", (cName, cSet, cNumber, cType, cCount,))
                print("Card added\n")
            except sqlite3.Error as error:
                print("Error adding card: ", error + "\n")

        #remove card
        elif option == 'r':
            print("Remove card")
            searchCards(cursor)
            #get user input for card id to remove
            try:
                rCard = int(input("Enter the ID number of the card to remove(or any letter to cancel): "))
                rCount = int(input("Enter amount of cards to remove: "))
            except:
                continue
            #fetch id
            try:
                cursor = db.execute("SELECT * FROM cards WHERE id=?", (rCard,))
                idCount = cursor.fetchone()
                idCount = idCount[COUNT_INDEX]
                cursor = db.cursor()
            except:
                print("Error, card id not found.\n")
                continue
            #if count of card id is == to rCard then remove card
            if rCount >= idCount:
                #remove card
                cursor.execute("DELETE FROM cards WHERE id=?", (rCard,))
                print("Card removed.\n")
            #else subtract 
            else:
                #subtract card
                idCount -= rCount
                cursor.execute("UPDATE cards SET count=? WHERE id=?", (idCount, rCard))
                print("Card count updated.\n")

        #display cards
        elif option == 'd':
            print("Display cards")
            searchCards(cursor)
            print()

        #quit
        elif option == 'q':
            break

        #save and quit
        elif option == 'sq':
            db.commit()
            break

        else:
            print("Invalid option\n")



    db.close()


main()
