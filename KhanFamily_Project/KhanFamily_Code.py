from pyswip import Prolog
prolog=Prolog()
prolog.consult("khanfamily.pl")


def display():
    print("<\tEnter 1 for Dada\t\t\t\t>")
    print("<\tEnter 2 for Dadi\t\t\t\t>")
    print("<\tEnter 3 for Bahu\t\t\t\t>")
    print("<\tEnter 4 for Sala\t\t\t\t>")
    print("<\tEnter 5 for Nana\t\t\t\t>")
    print("<\tEnter 6 for Nani\t\t\t\t>")
    print("<\tEnter 7 for Khala\t\t\t\t>") 
    print("<\tEnter 8 for BaapDada\t\t\t\t>")
    print("<\tEnter 9 for Nawasa\t\t\t\t>") 
    print("<\tEnter 10 for Pota\t\t\t\t>")
    print("<\tEnter 11 for Beta\t\t\t\t>") 
    print("<\tEnter 12 for Beti\t\t\t\t>")
    print("<\tEnter 13 for Pota\t\t\t\t>")
    print("<\tEnter 0 for Exit\t\t\t\t>")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

def KhanFamily():
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("<\t\t\t\t\t\t\t>\n<  Following are the Khan Family Memebers:\t\t>\n<\t\t\t\t\t\t\t>")
    print("<  chotekhan, chotirani, barrekhan, barrirani\t\t>")
    print("<  salim, kausar, nadir, asad, nahid, sumra\t\t>")
    print("<  rizwan, burhan, rashid, akram, salima, sanam, rabia\t>")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n")

def decision():
        while(True):
            decision = input("\n<<<<<<<<<<< Enter C to Continue and S to Stop >>>>>>>>>>>\n")
            if decision == "C" or decision == "c":
                return True
            elif decision == "S"  or decision == "s":
                return False
            else:
                print("<<<<<<<<<<<< Invalid Choice ! >>>>>>>>>>>>\n")  


def main():
    print("<<<<<<<<<<<<<<<<  WELL COME to Chat Bot  >>>>>>>>>>>>>>>>")

    choice = None
    exist = False

    while(choice!=0):
        display()    
        while True: 
            valid_choices = {"0","1","2","3","4","5","6","7","8","9","10","11","12","13"}
            choice=input("\n<< Enter your Choice for the Relationship that you are interested in >>\n")
            if choice in valid_choices:
                choice = int(choice)
                break
            else:
                print("\n<< Invalid Choice >>")
                continue

        if(choice==1):
            KhanFamily()  
            Z=input("Enter name of person whose Dada is required : ")
            Z=Z.lower()
            for val in prolog.query("dada(X,"+Z+")"):
                exist = True
                print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                print("Mr.{0} is the dada of {1}.".format(val["X"], Z))
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

        
        if(choice==2):
            KhanFamily()  
            Z=input("Enter name of person whose Dadi is required : ")
            Z=Z.lower()
            for val in prolog.query("dadi(X,"+Z+")"):
                exist = True
                print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                print("Ms.{0} is the dadi of {1}.".format(val["X"], Z))
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")    


        if(choice==3):
            KhanFamily()  
            Z=input("Enter name of person whose Bahu is required : ")
            Z=Z.lower()
            for val in prolog.query("bahu(X,"+Z+")"):
                exist = True
                print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                print("Ms.{0} is the bahu of {1}.".format(val["X"], Z))
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")      

        if(choice==4):
            KhanFamily()  
            Z=input("Enter name of person whose Sala is required : ")
            Z=Z.lower()
            for val in prolog.query("sala(X,"+Z+")"):
                exist = True
                print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                print("Mr.{0} is the sala of {1}.".format(val["X"], Z))
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")             
                
        if(choice==5):
            KhanFamily()  
            Z=input("Enter name of person whose Nana is required : ")
            Z=Z.lower()
            for val in prolog.query("nana(X,"+Z+")"):
                exist = True
                print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                print("Mr.{0} is the nana of {1}.".format(val["X"], Z))
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                
                
        if(choice==6):
            KhanFamily()  
            Z=input("Enter name of person whose Nani is required : ")
            Z=Z.lower()
            for val in prolog.query("nani(X,"+Z+")"):
                exist = True
                print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                print("Ms.{0} is the nani of {1}.".format(val["X"], Z))
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                     
       
        if(choice==7):
            KhanFamily()  
            Z=input("Enter name of person whose Khala is required : ")
            Z=Z.lower()
            for val in prolog.query("khala(X,"+Z+")"):
                exist = True
                print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                print("Ms.{0} is the khala of {1}.".format(val["X"], Z))
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

        if(choice==8):
            KhanFamily()  
            Z=input("Enter name of person whose BaapDada is required : ")
            Z=Z.lower()
            for val in prolog.query("baapDada(X,"+Z+")"):
                exist = True
                print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                print("Mr.{0} is the baapDada of {1}.".format(val["X"], Z))
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                        
        
        if(choice==9):
            KhanFamily()  
            Z=input("Enter name of person whose Nawasa is required : ")
            Z=Z.lower()
            for val in prolog.query("nawasa(X,"+Z+")"):
                exist = True
                print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                print("Mr.{0} is the nawasa of {1}.".format(val["X"], Z))
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")   

        if(choice==10):
            KhanFamily()  
            Z=input("Enter name of person whose Pota is required : ")
            Z=Z.lower()
            for val in prolog.query("pota(X,"+Z+")"):
                exist = True
                print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                print("Mr.{0} is the pota of {1}.".format(val["X"], Z))
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

        if(choice==11):
            KhanFamily()  
            Z=input("Enter name of person whose Beta is required : ")
            Z=Z.lower()
            for val in prolog.query("beta(X,"+Z+")"):
                exist = True
                print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                print("Mr.{0} is the beta of {1}.".format(val["X"], Z))
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

        if(choice==12):
            KhanFamily()
            Z=input("Enter name of person whose Beti is required : ")
            Z=Z.lower()
            for val in prolog.query("beti(X,"+Z+")"):
                exist = True
                print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                print("Ms.{0} is the beti of {1}.".format(val["X"], Z))
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

        if(choice==13):
            KhanFamily()  
            Z=input("Enter name of person whose ChachaTaya is required : ")
            Z=Z.lower()
            for val in prolog.query("chachataya(X,"+Z+")"):
                exist = True
                print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                print("Mr.{0} is the chachataya of {1}.".format(val["X"], Z))
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

        if exist == False:
            print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("Relationship does't Exist or Invalid Input.")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

        if decision() == True:
            continue
        else:
            break
    print("\n\n<<<<<<<<<<<<<<<<< Thank You for Coming >>>>>>>>>>>>>>>>>>\n")
        

if __name__=="__main__":
    main()