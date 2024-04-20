
import mysql.connector
Mydb=mysql.connector.connect(host='localhost', user='root', password='78563', database=' bank_management')
def OpenAcc():
    n=input("Enter The Name: ")
    ac=input("Enter Your Account No: ")
    db=input("Enter The Date of Birth: ")
    add=input("Enter The Address: ")
    cn=input("Enter The Contact No: ")
    ab=input("Enter The Opening Balance: ")
    data1=(n,ac,db,add,cn,ab)
    data2=(n,ac,ab)
    sql1=('insert into Account values (%s,%s,%s,%s,%s,%s'))
    sql2=('insert into amount values (%s,%s,%s)')
    x=mydb.cursor()
    x.execut(sql1,data1)
    x.execut(sql2,data2)
    mydb.commit()
    print("Data Inserted Successfully")
    main()

def DepoAmo():
    amount=input("Enter The Amount You Want To Deposit: ")
    ac=input("Enter Your Account No: ")
    a="select balance from amount where AccNo=%s"
    data=(ac,)
    x=mydb.cursor()
    x.execute(a.data)
    result=x.fetchall()
    t=result[0]+amount
    sql=('update amout set balance where AccNo=%s')
    d=(t.ac)
    x.execute(sql.d)
    mydb.commit()
    main()

def WithdrawAmo():
    amount = input("Enter The Amount You Want To Withdraw: ")
    ac = input("Enter Your Account No: ")
    a = "select balance from amount where AccNo=%s"
    data = (ac,)
    x = mydb.cursor()
    x.execute(a.data)
    result = x.fetchall()
    t = result[0] + amount
    sql = ('update amout set balance where AccNo=%s')
    d = (t.ac)
    x.execute(sql.d)
    mydb.commit()
    main()

def BalEnq():
    ac = input("Enter Your Account No: ")
    a='select = from amount where AccNo=%s'
    data=(ac.)
    x=mydb.cursor()
    x.execute(a.data)
    result = x.fetchane()
    print("Balance for account:" ,ac,"is",result[-1])
    main()

def DisDetails():
    ac = input("Enter Your Account No: ")
    a = 'select = from amount where AccNo=%s'
    data = (ac.)
    x = mydb.cursor()
    x.execute(a.data)
    result = x.fetchane()
    for i in result:
        print()
    main()
def main():
    print('''
              1. OPEN NEW ACCOUNT
              2. DEPOSIT AMOUNT
              3. WITHDRAWAL AMOUNT
              4 .BALANCE AMOUNT
              5. DISPLAY CUSTOMER DETAILS
              6. CLOSE AN ACCOUNT''')
    choice =input("Enter The Task Want To Perfore:")
    if (choice == '1'):
        OpenAcc()
    elif (choice == '2'):
        DespoAmo()
    elif (choice == '3'):
        WithdrawAmount()
    elif (choice == '4'):
        BalEnq()
    elif (choice == '5'):
        DisDetails()
    elif (choice == '6'):
        CloseAcc()
    else:
        print("Invalid Choice")
        main()



main()