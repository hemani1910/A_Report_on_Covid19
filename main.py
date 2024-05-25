import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
d=pd.read_csv("COVID-19 REPORT 1.csv")
print(d)
df=pd.read_csv("COVID-19 REPORT 2.csv")

def a():
    choice=0
    while choice !=8:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~".center(120))
        print("COVID-19 ANALYSIS".center(120))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~".center(120))
        print(" 1. DISPLAY REPORT".center(110))
        print(" 2. DATA VISUALISATION".center(114))
        print(" 3. DELETE A COLUMN".center(112))
        print(" 4. ACCESSING A COLUMN".center(114))
        print(" 5. DISPLAY ALL THE COLUMNS".center(120))
        print(" 6. COUNT NUMBER OF ROWS AND COLUMNS".center(127))
        print(" 7. EXIT".center(100))
        choice=int(input("\n Choose an Option:"))        
#IF CHOICE1 IS ENTERED THEN FULL TABLE WILL BE DISPLAYED
        if choice==1:
            print("DISPLAY DATA")
            print(df)
        elif choice==2:
#FOR DATA VISUALISATION
            def a2():
                choice2=0
                while choice2 !=5:
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~".center(120))
                    print("DATA VISUALISATION".center(120))
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~".center(120))
                    print("1. LINE CHART".center(120))
                    print("2. BAR GRAPH".center(118))
                    print("3. BOX PLOT".center(118))
                    print("4. PIE CHART".center(118))
                    print("5. GO BACK TO MAINMENU a".center(130))
                    choice2=int(input("\n Choose an option for Data Visualisation:"))
 #IF CHOICE1 IS ENTERED THEN A LINE CHART WILL BE DISPLAYED
                    if choice2==1:
                        sno=[0,1,2,3,4,5,6,7,8,9,10]
                        age=[30,35,50,4,94,60,80,84,63,12,21]
                        plt.plot(sno,age,color='c',marker='p',markersize=8,linestyle='solid',markeredgecolor='m')
                        plt.xlabel("No. of people")
                        plt.ylabel("Age groups")
                        plt.title("LINE CHART B/W TOTAL NO. OF PEOPLE IN PARTICULAR AGE GROUPS")
                        plt.figure(figsize=(15,7))
                        plt.show()
 #IF CHOICE2 IS ENTERED THEN A BAR CHART WILL BE DISPLAYED 
                    elif choice2==2:
                        sno=[0,1,2,3,4,5,6,7,8,9,10]
                        age=[30,35,50,4,32,60,26,12,63,12,21]
                        wardno=np.arange(0,11,1)
                        x=np.arange(11)
                        plt.bar(x+0.00,sno,color='c',width=0.25,label='sno')
                        plt.bar(x+0.25,age,color='y',width=0.25,label='age')
                        plt.bar(x+0.50,wardno,color='r',width=0.25,label='warno')
                        plt.legend(loc='upper right')
                        plt.grid(True)
                        plt.title("MULTIRANGE BAR CHART")
                        plt.figure(figsize=(15,7))
                        plt.show()
#IF CHOICE3 IS ENTERED THEN A BOXPLOT WILL BE DISPLAYED 
                    elif choice2==3:
                        age=[30,35,50,4,32,60,26,12,63,12,21]
                        wardno=[0,1,2,3,4,5,6,7,8,9,10]
                        final=[wardno,age]
                        plt.boxplot(final,patch_artist=True,notch=True,labels=['AGE','wardno'])
                        plt.title("BOXPLOT OF COLUMN AGE")
                        plt.figure(figsize=(15,7))
                        plt.show()
#IF CHOICE4 IS ENTERED THEN A PIECHART WILL BE DISPLAYED
                    elif choice2==4:
                        district=['indore','dhar','jhabua','others']
                        wardno=[4,5,6,7]
                        exp=[0,0,0.2,0]
                        col=['cyan','yellow','violet','red']
                        plt.pie(wardno,labels=district,colors=col,explode=exp,autopct="%5.2f%%")
                        plt.title("PIE CHART ON MAXIMUM AFFECTED AREAS")
                        plt.figure(figsize=(15,7))
                        plt.show()
                    else:
                        print("WRONG INPUT")
            a2()     
        elif choice==3:
#FOR DELETING A COLUMN
            def a3():
                choice3=0
                choice3=int(input("\n Enter an integer to Delete a Column:"))
                if choice3==1:
                    df1=pd.DataFrame(df)
                    del df['phone'] 
                    print(df)
                else:
                    print("WRONG INPUT")
            a3()    
        elif choice==4:
#FOR ACCESSING A COLUMN
            def a4():
                choice4=0
                choice4=int(input("\n Enter an integer to access a Column:"))
                if choice4==1:
                    print(df.loc[:,'name':'gender'])
                else:
                    print("WRONG INPUT")
            a4()    
        elif choice==5:
#FOR DISPLAYING ALL THE COLUMNS
            def a5():
                choice5=0
                choice5=int(input("\n Enter an integer to display all the columns:"))
                if choice5==1:
                    print(df.columns)
                else:
                    print("WRONG INPUT")
            a5()
        elif choice==6:
#FOR COUNTING NUMBER OF ROWS AND COLUMNS
            def a6():
                choice6=0
                while choice !=3:
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~".center(120))
                    print("COUNTING NUMBER OF ROWS AND COLUMNS".center(120))
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~".center(120))
                    print("1. COUNT NUMBER OF ROWS".center(110))
                    print("2. COUNT NUMBER OF COLUMNS".center(112))
                    print("3. GO BACK TO MAINMENU a".center(110))
                    choice6=int(input("\n Enter your choice to count number of Rows & Columns:")) 
                    if choice6==1:
                        print(df.count())
                    elif choice6==2:
                        print(df.count(1))
                    else:
                        print("WRONG INPUT")
                        a()
            a6()
        elif choice==7:
#FOR COUNTING NUMBER OF ROWS AND COLUMNS
            exit()
            
a()

#END
