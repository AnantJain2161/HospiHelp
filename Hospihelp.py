# CS PROJECT
import random
from datetime import *
from time import sleep
import mysql.connector as c
con=c.connect(host="localhost",
                         user="root",
                         passwd="admin",
                         database="hospihelp",
                         auth_plugin='mysql_native_password')
cur=con.cursor()
cur.execute("create database if not exists xiiaquila")
cur.execute("create table if not exists Bookings"
            "("
            "   SerialNO int primary key not null auto_increment,"
            "Name varchar(25),"
            "Age char(2),"
            "Gender char(1),"
            "Hospital varchar(25),"
            "specialist varchar(25),"
            "dayofappointment varchar(10),"
            "dateofappointment varchar(20),"
            "timeallotedinPM varchar(20),"
            "DoctorName varchar(25))")
l3=["shashankh sharma","tanishq saini","rahul jain","vishwas kumar","krish jaiswal","aditi sharma","jeevika sharma","vyomini jain","aditya narayan","kanha sharma","govind sachdev","rajgrover","rajiv verma","shrivastava jain"]



ds=int(input("Are you [1. Doctor/2.Patient]?:"))
if ds==1:
        print("""
                    ==================================
                                        !!!!!!!!  {{SIGN IN }}  !!!!!!!!!!
                    ==================================
                                                        """)
        print(" ")
        while True:
                w='hospital'
                check="correct"
                vbc=input("Enter your name:")
                if vbc in l3:
                        while True:
                                print('''If you have been feeling sick
And then you feel even worse
You might go to this building
To see a doctor or a nurse

Where is this building?''')
                                pswd=input('ENTER THE ANSWER AS PASSWORD TO LOGIN:')
                                pswd.lower()
                                while True:
                                        print('')
                                        if pswd==w:
                                                check=="incorrect"
                                                print("|||   Hi",vbc,"  |||")
                                                print(" ")
                                                print(""" YOU HAVE APPOINTMENT WITH FOLLOWING PATIENTS:-""")
                                                fgh="select * from bookings where DoctorName='%s'"%(vbc)
                                                cur.execute(fgh)
                                                records=cur.fetchall()
                                                vn=len(records)
                                                print(vn)
                                                if len(records)==0:
                                                        print("record not found")
                                                else:
                                                    for y in records:
                                                                print(y)




                                                while True:
                                                        cz=int(input('''Would you like to [1.allot time to patient,
                                                                     2.delete a record of patient,
                                                                     3.Search a record of patient,
                                                                     4 nurse details,
                                                                     5.quit]?:'''))
                                                        vb=random.randrange(12,22)
                                                        if cz ==1:
                                                            for i in range(1,vn+1):
                                                                sql="Select * from bookings where SerialNo=%s and DoctorName='%s'"%(i,vbc)
                                                                cur.execute(sql)
                                                                records=cur.fetchall()
                                                                if len(records)==0:
                                                                        print("record not found")
                                                                else:
                                                                    for y in records:
                                                                            print(y)
                                                                nb=input("Doctor would you like to change the time allotted to the patient?:")
                                                                if nb in "Yesyes":
                                                                    ds="update bookings set timeallotedinpm='%s' where SerialNo=%s"%(vb,i)
                                                                    cur.execute(ds)
                                                                    con.commit()
                                                                    print(cur.rowcount,"record(s) affected")
                                                                    print("")
                                                                elif nb in "Nono":
                                                                        continue
                                                                        
                                                        elif cz==2:
                                                                for i in range(1,vn+1):
                                                                        sql="Select * from bookings where SerialNo=%s"%(i)
                                                                        cur.execute(sql)
                                                                        records=cur.fetchall()
                                                                        if len(records)==0:
                                                                                print("record not found")
                                                                        else:
                                                                            for y in records:
                                                                                    print(y)
                                                                        nb=input("Doctor would you like to delete this record?:")
                                                                        if nb in "Yesyes":
                                                                                vv="delete from Bookings where SerialNo=%s"%(i)
                                                                                cur.execute(vv)
                                                                                con.commit()
                                                                                print(cur.rowcount,"record(s) affected")
                                                                                print("")
                                                                        elif nb in "Nono":
                                                                                continue
                                                        if cz==3:
                                                                lk=str(input("Enter the name of patient whose record you would like to search:"))
                                                                nm="select * from Bookings where Name='%s'"%(lk)
                                                                cur.execute(nm)
                                                                con.commit
                                                                record=cur.fetchall()
                                                                if len(record)==0:
                                                                        print("Record not found")
                                                                else:
                                                                        for x in record:
                                                                                print(x)
                                                        if cz==4:
                                                                cur.execute("select * from HIREnurse")
                                                                row=cur.fetchall()
                                                                con.commit()
                                                                print("Here are the records:")
                                                                sleep(0.2)
                                                                for i in row:
                                                                        v=list(i)
                                                                        k=["SNO","NAME","SPECIALISATION","COSTPERDAY","HOSPITALNAME"]
                                                                        d=dict(zip(k,v))
                                                                        print(d)
                                                        else:
                                                                quit()
                                                                
                                        elif pswd!=w:
                                                print('~!~!~!~~PASSWORD OR ID IS WRONG RE-ENTER~~!~!~!~')
                                                break
                                
                elif vbc not in l3:
                        print("You entered the name wrong:(( RE-ENTER IT")
                        continue
                
                

                        
                        
elif ds==2:
        
        print("*"*100)
        sleep(0.2)
        print(" "*40,end=' ')
        sleep(0.2)
        print("HOSPIHELP")
        sleep(0.2)
        print("*"*100)
        sleep(0.2)
        print('''Welcome To Hospihelp
1.Emergency,
2.First Aid,
3.Book an Appointment
4.Order from MediStore
5.Want to book nurse?
6.Quit''')
        sleep(0.2)
        choice = int(input("Select one of the above options to proceed with: "))
        sleep(0.2)
        if choice==1:
            print("You chose Emergency")    
            d={1:"Call an ambulance",2:"Tell me the nearest hospital",3:"Saftey procedure manual"}
            print(d)
            choice2 = int(input("Select one of the above options to proceed with: "))
            
            if choice2==1:
                print("You chose - Call an Ambulace")
                x=input("Please Enter your location: ")
                y=input("Enter your mobile number:")
                import random
                z=str(random.randrange(2345,2467))
                print("The no.of amulance is",'DL09'+z)
                print("The phone number of ambulance","1100 2345"+z)
                print("An ambulance is on the way to ",x)
            elif choice2==2:
                print("You chose - Tell me the nearest hospital")
                x=input("Please Enter your location: ")
                print('''The nearest hospitals from''',x,'''are 1.Golden Hospital - 2.3Km \n 2.MDA Hospital - 2.7Km
                      \n 3.AJK Hospital - 3.1Km''')
            elif choice2==3:
                print("You chose - Safety procedure manual")
                print('''1.Kindly maintain enough distance for patient to breathe properly\n)
                2.If the injury is on the head, make sure the patient is in an upright position\n)
                3.If there is any bleeding,try to prevent loss of blood by covering it with a clean tissue/towel\n)
                4.Make sure the patient remains concious and rush to a nearby hospital\n)
                5. CPR in case of patient drowning, short breathed, unconcious\n)
                6.For further queries, kindly contact this number - 011 2711-2233''')
        elif choice==2:
            print("You chose First Aid")
            print(''' 1.Procedure manual for small burns.''')
            choice3 = int(input("Select one of the above options to proceed with: "))
            if choice3==1:
                    print('''DO's
                        Stop the burning process: cool the burn with running cool (not cold) water for at least 5minutes.\n
                        But do not use ice, as this may cause further skin damage. Do not over cool! If the victim starts to shiver, stop the cooling process.\n
                        Remove all jewelry, watches, rings and clothing around the burned area as soon as possible.\n
                        Administer an over-the-counter pain reliever such as ibuprofen or acetaminophen for pain control.\n
                        Follow the directions on the label. Consult a physician or health care provider if pain is not relieved.\n
                        Cover the burn with a sterile gauge bandage or clean cloth. Wrap the burned area loosely to avoid putting too much pressure on the burn tissue.\n
                        Minor burns will usually heal without further treatment.\n
                        Lotions can be helpful torelive pain\n
                        DON’TS\n
                        Do not apply ice – this may cause further damage to the skin.n\
                        Do not use any butter, ointments or other home remedies on the burn. Such substances may trap the heat in the tissue and makes the burn worse.\n
                        Do not break any blisters…leave intact.\n
                        Do not delay seeing medical attention if the burn is larger than the size of the victim’s palm.''')
        elif choice==3:
                output="wrong"
                while (output=="wrong"):
                    nbbbb=str(input("Enter your name:"))
                    Age=int(input("Enter you age:"))
                    L3=['M','F','OTHER']
                    print(L3)
                    Gender=str(input("Enter your Gender:"))
                    if Gender in L3:
                            output="correct"
                            ans ="incorrect"
                            while (ans=="incorrect"):
                                L1=[]
                                print("You chose Book an appointment")
                                cur.execute("select * from doctor")
                                records=cur.fetchall()
                                if len(records)==0:
                                    print("record not found")
                                else:
                                    for y in records:
                                        print(y)
                                N=int(input("Choose a number from above to fix an appointment with a specialist of a particular hospital:"))
                                print("You chose")
                                Z="select * from doctor where SerialNO=%s"%(N)
                                cur.execute(Z)
                                records=cur.fetchall()
                                print(records)
                                sleep(0.2)
                                print("Hospital and specialist chosen are")
                                sleep(0.2)
                                f="select Specialist from doctor where SerialNO=%s"%(N)
                                cur.execute(f)
                                records=cur.fetchall()
                                h=records
                                print(records)
                                g=h[0][0]
                                m="select Hospital from doctor where SerialNO=%s"%(N)
                                cur.execute(m)
                                records=cur.fetchall()
                                b=records
                                print(records)
                                c=b[0][0]
                                kkk="select doctorname from doctor where SerialNO=%s"%(N)
                                cur.execute(kkk)
                                records=cur.fetchall()
                                sss=records
                                print(records)
                                nbn=sss[0][0]

                                d2={1:['2pm to 4pm','6pm to 8pm',150],2:['1pm to 3pm','5pm to 7pm',100],3:['9am to 11am','6pm to 8pm',80],4:['7am to 9am','3pm to 5pm',85],5:['2pm to 4pm','6am to 8am',100]}
                                m=random.randrange(1,6)
                                n=random.randrange(1,6)
                                for i in d2:
                                    print(i,'.',d2[i][0],d2[i][2])
                                print("available time slots" 'are\n','1.',d2[m][1],"price:-",d2[m][2],'and','2.',d2[n][1],"price:-",d2[n][2])
                                sleep(0.2)
                                choice6=int(input("Choose time slot:"))
                                pc=d2[choice6][0]
                                x=input("Enter the day of the appointment:")
                                y=input("Enter date of the appointment:")
                                z=input("Is this the appointment you wanted to book:")
                                if z in 'YESyes':
                                    print('Your appointment has been booked:')
                                    p="insert into Bookings(Name,Age,Gender,Hospital,Specialist,dayofappointment,dateofappointment,timeallotedinPM,DoctorName) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                    val=(nbbbb,Age,Gender,c,g,x,y,pc,nbn)
                                    cur.execute(p,val)
                                    con.commit()
                                    print(cur.rowcount,"record inserted.")
                                    print("""
                                        ====================================
                                                     !!!!!!!REGISTERED SUCCESSFULLY!!!!!!
                                        ====================================
                                                        """)
                                    print('Thank you')
                                    ans="correct"
                                elif z in 'NOno':
                                    print("Enter details again:")
                    elif Gender not in L3:
                                    print('''You didnt chose the gender from the given options
                                          Enter details again:''')
        elif choice==4:
                d=input("Are you chemist:").lower()
                F={}
                def hospi():
                     cur.execute("Select* from medistore")
                     myresult=cur.fetchall()
                     print('Medicinename\tcost\tquantity available\tmedicine number')
                     for x in myresult:
                         print(x)
                while True:
                    if d in "yes":
                        u=input("create your username:")
                        z=input("create your password:")
                        f=input("enter your password:")
                        if z==f:
                            F[u]=z
                            break
                        else:
                            print("Your password do not match")
                            continue
                    elif d in "no":
                        break
                import mysql.connector
                con=c.connect(host="localhost",user="root",passwd="admin",database="hospihelp",auth_plugin='mysql_native_password')
                cur=con.cursor()
                while True:
                    print("1.Login as a chemist\n2.Login as a user")
                    a=int(input("You want to login as:"))
                    if a==1:
                        x=input("user id:")
                        y=input("password")
                        if y==F[x]:
                            while True:
                                print("1.want to see the records:\n 2.Make changes in the records \n3.To go back to the prevoiu menu")
                                g=int(input("Enter the number of the option you chose:"))
                                if g==1:
                                    hospi()
                                elif g==2:
                                    print("1.Enter new medicine \n2.Enter the quantity of new stock received \n3.Change the price of a medicine \n4.To delect existing medicine\n5.To go to the previou menu")
                                    k=int(input("What do you wish to do:"))
                                    while True:
                                        if k==1:
                                            n=int(input("How many records you want to enter:"))
                                            for i in range(n):
                                                d=0
                                                x=input("Enter name of the medicine:")
                                                y=int(input("Enter the price of the medicine:"))
                                                z=int(input("Enter the quantity available for the medicine:"))
                                                cur.execute("Select* from medistore")
                                                myresult=cur.fetchall()
                                                d=len(myresult)+1
                                                sql="insert into medistore values(%s,%s,%s,%s)"
                                                val=(x,y,z,d)
                                                cur.execute(sql,val)
                                                con.commit()
                                                print(cur.rowcount ,"Record(s) inserted")
                                        elif k==2:
                                            hospi()
                                            v=int(input("Enter the number of the medicine whose quantity you want to change:"))
                                            g=int(input("Enter the quantity received:"))
                                            dfg="update medistore set quantity=quantity+%s where medino=%s"%(g,v)
                                            cur.execute(dfg)
                                            con.commit()
                                            print(cur.rowcount ,"Record(s) updated")
                                        elif k==3:
                                            hospi()
                                            v=int(input("Enter the number of the medicine whose price you want to change:"))
                                            g=int(input("Enter the new price of the medicine:"))
                                            sql="update medistore set price=%s where medino=%s"%(g,v)
                                            cur.execute(sql)
                                            con.commit()
                                            print(cur.rowcount ,"Record(s) updated")
                                        elif k==4:
                                            hospi()
                                            o=int(input("Enter the Serial number of the record you want to delete:"))
                                            sql="Delete from medistore where medino=%s"%(o)
                                            cur.execute(sql)
                                            con.commit()
                                            print(cur.rowcount ,"Record(s) deleted")
                                        elif k==5:
                                            break
                                        else:
                                            print("Enter 1,2,or3")
                                        break
                                elif g==3:
                                    break
                                else:
                                    print("Enter 1,2 or 3")
                    elif a==2:
                        hospi()
                        while True:
                            x=int(input("Write the number of the medicine which you want:"))
                            y=int(input("Enter the quantity of the medicine:"))
                            sql="Select * from medistore where medino=%s"%(x)
                            cur.execute(sql)
                            myresult=cur.fetchall()
                            for z in myresult:
                                if z[2]<y:
                                    print("Order can not be placed not enough stock")
                                    print("Only",z[2],"packets of",z[0],"are left")
                                    break
                                else:
                                    t=0
                                    t=t+z[1]*y
                                    dfg="update medistore set quantity=quantity-%s where medino=%s"%(y,x)
                                    cur.execute(dfg)
                                    con.commit()
                            y=input("Do you want to continue")
                            if y in "NOno":
                                break
                            else:
                                continue
                        print("Your bill amount is:",t)
                    else:
                        print("Enter 1or2")
                        continue
        elif choice==5:
                cur.execute("SELECT * FROM hirenurse")
                myresult=cur.fetchall()
                print('No \tName\t   speciality\tcost\tHospitalName') 
                for x in myresult:
                        print(x)
                choice=int(input("choose from above nurses:-"))
                if choice in myresult[0]:
                        cur.execute("Select * from nurse")
                        myresult=cur.fetchall()
                        f=len(myresult)
                        k=input("enter name of booker:-")
                        y=input("enter date of booking:-")
                        z=input("enter state:-")
                        j=input("enter address:-")
                        print("a nurse was appointed at", j ,"on", y, " for name", k)
                        sql="INSERT INTO nurse(name,dateofbooking,state,address) values('%s','%s','%s','%s')" %(k,y,z,j)
                        cur.execute(sql)
                        con.commit()
        elif choice==6:
                quit()

                        
                        
                
            

                    
            
            
            
                   
    
    
        






    
