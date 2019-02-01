from customer import Account  # importing the account module

ed = Account("Ed Harris", 67000)  # creating the account Account object named ed
ed.print_info()  # print balance
ed.withdraw(7000)
ed.print_info()  # print balance
ed.deposit(7000)
ed.print_info()