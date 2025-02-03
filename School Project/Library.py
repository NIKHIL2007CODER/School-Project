print("-="*4,"⭐✨🌟░░░▒▒▓ＰＭ  ＳＨＲＩ  ＫＥＮＤＲＩＹＡ  ＶＩＤＹＡＬＡＹＡ  ＫＥＳＨＡＶＰＵＲＡＭ  ＬＩＢＲＡＲＹ▓▒▒░░░🌟✨⭐" , "=-"*4)
import pickle
from tabulate import tabulate

def Add_books():
    f = open("Books.dat" , "ab")
    while True:
        bName = input("| Enter the Name of Book |")
        bId = int(input("| Enter ISBN id of Book |"))
        bAuthor = input("| Enter Author of Book |")
        bPrice = int(input("| Enter Price of the Book |"))
        bGenre = input("| Enter Genre of the Book |")
        bRating = int(input("| Enter Rating out of 10 of Book |"))
        l = [bName,bId,bAuthor,bPrice,bGenre,bRating]
        pickle.dump(l,f)
        

        ch = input("To Add more records press yY :")

        if ch not in "yY":
            print("Your records have been successfully added!!!")
            break        
    f.close()

#========================================================================================
def search_book():
    f = open("Books.dat" , "rb")
    flag  = False
    x = True      
    searchBy = input("Seach by Name/ISBN Id/Price Range (n/id/pr):")

    if searchBy == "n":
        name = input("Enter Name of the Book:")
        l = []
        try:
            while x == True:
                r = pickle.load(f)

                if name in r[0]:
                    l.append(r)
                    
                    flag = True
        except EOFError:
            x = False
        header = "Name of Book" , "ISBN Id" ,"Author" , "Price" ,"Genre" , "Rating(Out of 10)"
        print("+-~-"*15)
        print("Records found with Name:",r[0])
        print(tabulate(l,header,tablefmt = "grid"))
        print("+-~-"*15)
            

    elif searchBy == "id":
        id = int(input("Enter Id of the Book:"))
        try:
            while x == True:
                r = pickle.load(f)

                if r[1] ==id:
                    header = "Name of Book" , "ISBN Id" ,"Author" , "Price" ,"Genre" , "Rating(Out of 10)"
                    a = [r]
                    print("+-~-"*15)
                    print("Records found with Id:",r[1])
                    print(tabulate(a,header,tablefmt = "grid"))
                    print("+-~-"*15)
                    flag = True
        except EOFError:
            x = False

    elif searchBy == "pr":
        p1 = int(input("Price Starting from:"))
        p2 = int(input("Price Ending at:"))
        l = []
        try:
            while x == True:
                r = pickle.load(f)

                if r[3]>=p1 and r[3]<=p2:
                    l.append(r)
                    flag = True
                    
        except EOFError:
            x = False
        header = "Name of Book" , "ISBN Id" ,"Author" , "Price" ,"Genre" , "Rating(Out of 10)"          
        print("+-~-"*15)
        print("Records found with Price Range:",p1,"to" ,p2)
        print(tabulate(l,header,tablefmt = "grid"))
        print("+-~-"*15)
        

    if flag == False:
        print("No Book found!")
    f.close()

#========================================================================================

def display_books():
    f = open("Books.dat" , "rb")
    x = True
    flag = False
    a = []
    header = ["ISBN ID" , "Name" , "Author" , "Price" , "Genre" , "Rating"]
    try:
        while x == True:
            r = pickle.load(f)
            l = [str(r[1]),r[0],r[2],str(r[3]),r[4],str(r[5])]
            a.append(l)
            flag = True
        
    except EOFError:
        x = False
    print(tabulate(a , header ,tablefmt = "grid"))
    if flag == False:
        print("NO BOOKS IN LIBRARY!")
    f.close()


#=========================================================================================

def update_books():
    f=open("Books.dat" , "rb")
    
    ch = input("What do you want to Update(ISBN Id=id \ Name = n \ Author = a \ Price = p \Genre = g \ Rating = r):")
    a =[]
    x = True
    if ch == "id":
        oid = int(input("Enter the old id:"))
        nid=int(input("Enter new id:" ))
        try:
            while x ==True:
                r = pickle.load(f)
                if r[1]==oid:
                    r[1]=nid
                    print(r[1])
                    a.append(r)
                else:
                    a.append(r)
        except EOFError:
            x = False

    elif ch == "n":
        oname = input("Enter the old Name:")
        nname=input("Enter new Name:" )
        try:
            while x ==True:
                r = pickle.load(f)
                if r[0]==oname:
                    r[0]=nname
                    print(r[0])
                    a.append(r)
                else:
                    a.append(r)
        except EOFError:
            x = False
    
    elif ch == "a":
        o = input("Enter the old Author:")
        n=input("Enter new Author:" )
        try:
            while x ==True:
                r = pickle.load(f)
                if r[2]==o:
                    r[2]=n
                    print(r[2])
                    a.append(r)
                else:
                    a.append(r)
        except EOFError:
            x = False
    
    elif ch == "p":
        o = int(input("Enter the old Price:"))
        n=int(input("Enter new Price:" ))
        try:
            while x ==True:
                r = pickle.load(f)
                if r[3]==o:
                    r[3]=n
                    print(r[3])
                    a.append(r)
                else:
                    a.append(r)
        except EOFError:
            x = False

    elif ch == "g":
        o = input("Enter the old Genre:")
        n=input("Enter new Genre:" )
        try:
            while x ==True:
                r = pickle.load(f)
                if r[4]==o:
                    r[4]=n
                    print(r[4])
                    a.append(r)
                else:
                    a.append(r)
        except EOFError:
            x = False

    elif ch == "r":
        o = int(input("Enter the old Rating:"))
        n=int(input("Enter new Rating:" ))
        try:
            while x ==True:
                r = pickle.load(f)
                if r[5]==o:
                    r[5]=n
                    print(r[5])
                    a.append(r)
                else:
                    a.append(r)
        except EOFError:
            x = False

    f.close()
        
    f2 = open("Books.dat" , "wb")
    for i in a:
        pickle.dump(i,f2)
    f2.close()
    
#============================================================================================
def issue_books():
    f = open("Issue.dat" , "ab")
    while True:
        
        iName = input("| Enter Name of Issuer | ")
        iMobile = int(input("| Enter Mobile no. of Issuer | "))
        iDate = input("| Enter Date of Issuing | ")
        ibook=input("| Enter Name of Book Issued | ")
        iId = int(input("| Enter Issued Book ISBN Id | "))
        rentedFor = int(input("| Days Rented for | "))
        l=[iName,iMobile,iDate,ibook,iId,rentedFor]
        pickle.dump(l,f)
        ch = input("To Add more records press yY :")

        if ch not in "yY":
            print("Your records have been successfully added!!!")
            break        
    f.close()


#==============================================================================================

def display_issued_books():
    f = open("Issue.dat" , "rb")
    x = True
    flag = False
    a = []
    header = ["Name" , "Mobile" , "Date" , "Book Issued" , "ISBN Id" , "Days Rented for"]
    try:
        while x == True:
            r = pickle.load(f)
            l = [r[0],str(r[1]) , r[2] , r[3] , str(r[4]) , str(r[5])]
            a.append(l)
            flag = True
        
    except EOFError:
        x = False
    print(tabulate(a , header ,tablefmt = "grid"))
    if flag == False:
        print("NO BOOKS ISSUED!!")
    f.close()

#==============================================================================================

def return_book():
    f = open("ReturnBook.dat" , "ab")
    while True:
        returner=input("| Name of the Returner | ")
        book=input("| Name of Book to be Returned | ")
        date=input("| Date of Returning | ")
        amount=int(input("| Amount to be Paid for Issued Book | "))
        l=[returner,book,date,amount]
        pickle.dump(l,f)

        ch=input("| Enter yY for more Entries | ")
        if ch not in "yY":
           break
    f.close()
    print("-=-=-=-=-= Record Added Successfully!! =-=-=-=-=-")

#=============================================================================================

def display_returns():
    f = open("ReturnBook.dat" , "rb")
    x = True
    flag = False
    a = []
    header = ["Name" ,"Book Returned", "Date" ,"Amount to be Paid"]
    try:
        while x == True:
            r = pickle.load(f)
            l = [r[0] , r[1] , r[2] , str(r[3])]
            a.append(l)
            flag = True
        
    except EOFError:
        x = False
    print(tabulate(a , header ,tablefmt = "grid"))
    if flag == False:
        print("NO RETURNED BOOKS!!")
    f.close()


while True:
    print("=-=-=-=-=-=-=-=-=-♾️♾️♾️♾️♾️♾️🔸🔸🔸🔸🔸⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜※※※※※※※※※※※※※※※※※※※※⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜🔸🔸🔸🔸🔸♾️♾️♾️♾️♾️♾️-=-=-=-=-=-=-=-=-=")
    ch = input("|1.Add Books \n|2.Search Books \n|3.Display Books \n|4.Update Books \n|5.Issue Book \n|6.Display Issued Book Records \n|7.Return Book \n|8.Display Returned Book Records \n|9.Exit \n =-=-=-=-=-=-=-=-=-♾️♾️♾️♾️♾️♾️🔸🔸🔸🔸🔸⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜※※※※※※※※※※※※※※※※※※※※⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜⁜🔸🔸🔸🔸🔸♾️♾️♾️♾️♾️♾️-=-=-=-=-=-=-=-=-=\n|Use:")
    if ch == "1":
        Add_books()
    elif ch=="2":
        search_book()
    elif ch == "3":
        display_books()
    elif ch == "4":
        update_books()
    elif ch == "5":
        issue_books()
    elif ch =="6":
        display_issued_books()
    elif ch =="7":
        return_book()
    elif ch =="8":
        display_returns()
    elif ch =="9":
        print("✨🌟💫~=~=~=~=~=~=~=~=~=~=~=~=~=~▓▒▒░░░ＥＮＤ ＯＦ ＰＲＯＧＲＡＭ░░░▒▒▓~=~=~=~=~=~=~=~=~=~=~=~=~💫🌟✨")
        print(" "*31 , "—"*40)
        print("🌟▪️▫️▪️▫️▪️▫️▪️▫️▪️▫️▪️▫️▪️▫️▪️▫️▪️▫️▪️🎉🎊ＴＨＡＮＫＳ ＦＯＲ ＵＳＩＮＧ ＴＨＩＳ ＰＲＯＧＲＡＭ🎊🎉▪️▫️▪️▫️▪️▫️▪️▫️▪️▫️▪️▫️▪️▫️▪️▫️▪️▫️▪️🌟")
        print(" ")
        break
