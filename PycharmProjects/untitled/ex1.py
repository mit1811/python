import time

credit = 700
total = 1200


class Debitcard():
    def debitvalue(self, count):
        global total
        string = raw_input("you want to pay(p),withdraw(w) and exit(e)")
        if string == 'pay':
            value = int(input("enter value"))
            total += value
            print("Your total Balance is = {} (Time : {})".format(total, time.asctime()))
        elif string == 'wid':
            value = int(input("enter value"))
            total -= value
            print("Your total Balance is = {} (Time : {})".format(total, time.asctime()))
        elif string == 'exit':
            count = 3
            print ("Thank You")


class Creditcard(Debitcard):
    def creditvalue(self, count):
        global credit
        global total
        s = raw_input("You want to pay, Withdraw and exit:")

        if s == 'pay':
            value = int(input("enter value"))
            total = total - value
            print("Total Balance of debitcard is = {} (Time : {})".format(total, time.asctime()))
            credit = credit + value
            print("Total Balance of creditcard is = {} (Time : {})".format(credit, time.asctime()))
        elif s == 'wid':
            value = int(input("enter value"))
            credit = credit - value
            print("Total Balance is = {} (Time : {})".format(credit, time.asctime()))
        elif s == 'exit':
            count = 3
            print('Thank You')


class main:
    def main():
        count = 0
        debit = Debitcard()
        credit = Creditcard()
        while count < 3:
            count = count + 1
            account = raw_input("Enter Options :- credit or debit")
            if account == 'debit':
                debit.debitvalue(count)
            elif account == 'credit':
                credit.creditvalue(count)
            elif account == 'exit':
                print("Thank You")
                break

    if __name__ == "__main__": main()






