
class ATM:
    def main(self):
        balance = 0  
        while True:
            import mysql.connector as mysql
            con = mysql.connect(host="localhost", user= "root", password="1513", database="atm_2024")
            cur=con.cursor()
            print("Automated Teller Machine")
            print("Choose 1 for Withdraw")
            print("Choose 2 for Deposit")
            print("Choose 3 for Check Balance")
            print("choose 4 for pin creation")
            print("Choose 5 for EXIT")
            choice = int(input("Choose the operation you want to perform: "))
            if choice == 1:
                pin=int(input("enter a 4 digit pin number"))
                cur.execute(f"select * from atm where pin='{pin}'")
                rows= cur.fetchall()
                if not rows:
                    print("please enter correct pin")
                elif rows:
                    withdraw = int(input("Enter money to be withdrawn: "))
                    if withdraw%100==0:
                        for i in rows:
                            balance=i[2]
                        if balance >= withdraw:
                            balance -= withdraw
                            cur.execute(f"update atm set balance= '{balance}'where pin='{pin}'")
                            print("Please collect your money")
                            con.commit()
                        else:
                            print("Insufficient Balance")
                            print("")
                    else:
                        print("please enter the amount in hundered multiples only")
                    print()
                
            elif choice == 2:
                pin=int(input("enter a 4 digit pin number"))
                cur.execute(f"select * from atm where pin='{pin}'")
                rows= cur.fetchall()
                if not rows:
                    print("please enter correct pin")
                elif rows:
                    deposit = int(input("Enter money to be deposited: "))
                    if deposit%100==0:
                        for i in rows:
                            balance=i[2] 
                        balance=balance+deposit
                        cur.execute(f"update atm set balance= '{balance}'where pin='{pin}'")
                        con.commit()
                        print("Your Money has been successfully deposited")
                        print("")
                    else:
                        print("enter the deposit amount only in 100 multiples")
                    print()
                
            elif choice == 3:
                pin=int(input("enter a 4 digit pin number"))
                cur.execute(f"select * from atm where pin='{pin}'")
                rows= cur.fetchall()
                if not rows:
                    print("please enter correct pin")
                elif rows:
                    for i in rows:
                        balance=i[2]
                    print("Balance : " + str(balance))
                    print("")
                    con.close()
            elif choice==4:
                pin=int(input("enter the 4 digit pin"))
                pin1=int(input("conform the 4 dgit pin"))
                name=input()
                if pin==pin1:
                    cur.execute(f"insert into atm values({pin},'{name}',{0})")
                    con.commit()
                    con.close()
                print()
            elif choice == 5:
                break

a1=ATM()
a1.main()
