import MySQLdb
from Tkinter import *
from PIL import Image
import mysql.connector
try:
	db=mysql.connector.connect(host='localhost',user='root',password='root',database='dbms')
	cur=db.cursor()
	print ("Database was connected successfully")
except:
	print ("Error")
	
cursor=db.cursor()
root = Tk()
image1=PhotoImage(file="/home/ritub/Downloads/bg.png")
panel=Label(root,image=image1,bg="black").place(x=0,y=0,relwidth=1,relheight=1)
root.title("BLOOD BANK")
root.geometry("1920x1080")
root.configure(background='white')

while(1):
        ch1 = input("Do you want to continue<y/n> : ")
        if(ch1 == 'n' or ch1 == 'N'):
                break
        ch = int(input("\n1.Create database\n2.Add new donor\n3.View all donors\n4.Update donor details\n5.Search donor details\n6.Remove donor\nEnter your choice : "))
        if(ch == 1):
                sql = "CREATE TABLE DONOR(FIRST_NAME VARCHAR(20) NOT NULL, LAST_NAME VARCHAR(20),AGE INT, SEX VARCHAR(1),DONOR_ID INT,BLOOD_TYPE VARCHAR(5),PRIMARY KEY(DONOR_ID))"
                try:        
                        cur.execute(sql)
                        print("table created successfully") 
                        db.commit()
                        
                except:
                        db.rollback()
                
        elif(ch == 2):
                b = int(input("Enter the ID : "))
                f = input("Enter the first name : ")
                l = input("Enter the last name : ")
                a = int(input("Enter the age : "))
                s = input("Enter the gender[F/M] : ")
                i = input("Enter the type : ")
                sql = "INSERT INTO DONOR VALUES ('%s', '%s', '%d', '%c','%d', '%s' )" %(f,l,a,s,b,i)
                print("Donor was successfully added")
                try:
                        cur.execute(sql)
                        db.commit()
                except:
                        db.rollback()
        elif(ch == 3):
                view="SELECT* FROM DONOR"
                cur.execute(view)
                results = cur.fetchall()
                for row in results:
                      fname = row[0]
                      lname = row[1]
                      age = row[2]
                      sex = row[3]
                      did = row[4]
                      typ = row[5]
                      print("\nID={0}\nFirst name= {1}\nLast name = {2}\nAge ={3}\nSex = {4}\nType = {5}".format(did,fname,lname,age,sex,typ))
        elif(ch == 4):
                e = int(input("Enter the donor ID for modification : "))
                ch = int(input("\n1.Update age\n2.Update type\nEnter your choice : "))
                if(ch == 1):
                        age = int(input("Enter the age to be updated : "))
                        upd = "UPDATE DONOR SET AGE='%d' WHERE DONOR_ID='%d'"%(age,e)
                        try:
                                cur.execute(upd)
                                db.commit()
                                print("Age Updated Successfully")
                        except:
                                db.rollback()
                elif(ch == 2):
                        typ =input("Enter the type to be updated : ")
                        upd = "UPDATE DONOR SET BLOOD_TYPE='%s' WHERE DONOR_ID='%d'"%(typ,e)
                        try:
                                cur.execute(upd)
                                db.commit()
                                print("blood type Updated Successfully")
                        except:
                                db.rollback()
        elif(ch == 5):
                e = int(input("Enter the donor ID : "))
                view="SELECT * FROM DONOR WHERE DONOR_ID = '%d'"%(e)
                cur.execute(view)
                results = cur.fetchall()
                for row in results:
                      fname = row[0]
                      lname = row[1]
                      age = row[2]
                      sex = row[3]
                      did = row[4]
                      typ = row[5]
                      print("\nID={0}\nFirst name= {1}\nLast name = {2}\nAge ={3}\nSex = {4}\nTYPE = {5}\n".format(did,fname,lname,age,sex,typ))

        elif(ch == 6):
                e = int(input("Enter the DONOR ID to be deleted : "))
                dele = "DELETE FROM DONOR WHERE DONOR_ID='%d'"%(e)
                try:
                        cur.execute(dele)
                        print("Successfully deleted")
                        db.commit()
                except:
                        db.rollback()
