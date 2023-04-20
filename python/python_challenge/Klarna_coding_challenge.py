#%%
class MovingAverage:
    def __init__(self, N):
        if not isinstance(N, int):
            raise Exception("Invalid data type! Initial with a positive integer value.")
        elif N <= 0:
            raise Exception("Incorrect input! Initial with a positive integer value.")
        else:
            self.window = N  # moving average window

        self.sum = 0
        self.num_list = []  # list to store the number input by user

    def add(self, X):
        if isinstance(X, int) or isinstance(X, float):
            self.num_list.append(X)
        else:
            raise Exception("Invalid data type! Enter a number.")

        if len(self.num_list) <= self.window:
            self.sum = self.sum + X
            self.av = self.sum / len(self.num_list)
        else:
            self.sum = 0
            start_index = len(self.num_list) - self.window
            for num in self.num_list[start_index:]:
                self.sum = self.sum + num

            self.av = self.sum / self.window

        return self.av


#%%
class Underwriter:
    def transaction_check(transaction1, transaction2):
        invalid_transactions = False
        if (
            abs(transaction1[1] - transaction2[1]) <= 60
            and transaction1[2] == transaction2[2]
        ):
            print("first if")
            print(transaction1)
            print(transaction2)
            invalid_transactions = True

        elif (
            abs(transaction1[1] - transaction2[1]) <= 60
            and transaction1[3] != transaction2[3]
        ):
            print("first elif")
            invalid_transactions = True

        elif abs(transaction1[1] == transaction2[1]):
            print("second elif")
            invalid_transactions = True

        return invalid_transactions

    def identify_invalid_transactions(transactions):
        invalid_transactions = []
        blank = False

        if not transactions:
            print("not transactions")
            return invalid_transactions
        if len(transactions) < 2:
            return invalid_transactions

        name_list = []
        time_list = []
        amt_list = []
        city_list = []

        for transaction in transactions:
            if transaction == "":
                blank = True
                print("blank")
                continue
            try:
                print("try")
                name, time, amt, city = transaction.split(",")

                if name != "" and int(time) >= 0 and int(amt) > 0 and city != "":
                    print("inside if")
                    name_list.append(name)
                    time_list.append(int(time))
                    amt_list.append(int(amt))
                    city_list.append(city)
                    if int(amt) > 2000:
                        invalid_transactions.append(transaction)
                        continue
                else:
                    invalid_transactions.append(transaction)
                    continue
            except:
                print("except")
                invalid_transactions.append(transaction)
                continue

        if blank:
            transactions = [data for data in transactions if data != ""]

        for i in range(len(name_list) - 1):
            name = name_list[i]
            for j in range(i + 1, len(name_list)):
                if name == name_list[j]:
                    transaction_check_response = Underwriter.transaction_check(
                        [name_list[i], time_list[i], amt_list[i], city_list[i]],
                        [name_list[j], time_list[j], amt_list[j], city_list[j]],
                    )
                    if transaction_check_response:
                        invalid_transactions.append(transactions[i])
                        invalid_transactions.append(transactions[j])

        invalid_transactions = list(set(invalid_transactions))
        return invalid_transactions


#%%
test_input = [
    "john2,15,1819,Sydney",
    "john2,105,944,Tokyo",
    "john0,67,1991,Sydney",
    "john1,30,143,Stockholm",
    "john2,87,229,Stockholm",
    "john1,63,1181,New York",
]
Underwriter.identify_invalid_transactions(test_input)


#%%
def who_is_going_home_early(n, k):
    num_of_employee_leave = n // 2
    num_of_employee_leave_list = []
    game_list = []  # list of all player
    counter = 0
    counter_diff = 0

    if n == 1:
        return []

    if n == 0 or k == 0:
        raise Exception("invalid input!")

    for i in range(1, n + 1):
        game_list.append(i)

    while len(num_of_employee_leave_list) < num_of_employee_leave:
        if k < n:
            counter = counter + k
            if counter >= len(game_list):
                counter = counter - len(game_list)
                num_of_employee_leave_list.append(game_list[counter])
                game_list.pop(counter)

            else:
                num_of_employee_leave_list.append(game_list[counter])
                game_list.pop(counter)

        else:
            # got this logic through trial and error.
            # similar to modulo in group theory
            counter = k % len(game_list) - counter_diff
            num_of_employee_leave_list.append(game_list[counter])
            game_list.pop(counter)
            counter_diff = len(game_list) - counter
    return num_of_employee_leave_list
