class creditcard:
    """A consumer credit card"""
    
    def __init__(self,customer,bank,acnt,limit):
        """Create a new credit card instance
        The initial balance is zero
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
    
    def get_customer(self):
        """Return name of the customer"""
        return self._customer
    
    def get_bank(self):
        """Return the bank's name"""
        return self._bank
    
    def get_account(self):
        """Return account details"""
        return self._account
    
    def get_limit(self):
        """Return currect credit limit"""
        return self._limit
    
    def get_balance(self):
        """Return current balance"""
        return self._balance
    
    def charge(self, price):
        """Charge given price to the card, assuming sufficient limit"""
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True
    
    def make_payment(self, amount):
        """Process customer payment that reduces balance"""
        self._balance -= amount

#########################################################################################################################

# our class for the in-build class range
class Range:
    """a class that minic's the built-in range class"""
    
    def __init__(self,start,stop=None,step=1):
        """Initialize a Range instance.
        Sementics is similar to built-in range class
        """
        if step == 0:
            raise ValueError('step cannot be 0')
        if stop is None:
            start,stop = 0,start
        
        # calculate the effective length once
        self._length = max(0, (stop - start + step - 1)//step)
        self._start = start
        self._step = step
    
    def __len__(self):
        """Return number of entries in the range
        """
        return self._length
    
    def __getitem__(self,k):
        """Return entry at index k (using standard interpretation if negative).
        """
        if k < 0:
            k += len(self)
        
        if not 0 <= k < self._length:
            raise IndexError('index out of range')
        
        return self._start + k*self._step

#############################################################################################################################

class predetorycredit(creditcard):
    """An extension to creditcard that compounds interest and fees"""
    
    def __init__(self,customer,
                bank,acnt,
                limit,apr):
        """Create a new predatory credit card instance"""
        super().__init__(customer,bank,acnt,limit)
        self._apr = apr
        
    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit"""
        success =  super().charge(price)
        if not success:
            self._balance += 5
        return success
    
    def process_month(self):
        """Assess monthly interest on outstanding balance"""
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr,1/12)
            self._balance *= monthly_factor

################################################################################################################################

class progression:
    """iterator producing a generic progression"""
    
    def __init__(self,start=0):
        self._currect = start
        
    def _advance(self):
        self._current += 1
    
    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer
    
    def __iter__(self):
        return self
    
    def print_progression(self, n):
        print(' '.join(str(next(self)) for j in range(n)))
        

class arithmeticprogression(progression):
    
    def __init__(self,increment=1,start=0):
        super().__init__(start)
        self._increment = increment
    
    def _advance(self):
        self._current += self._increment
        

class geometricprogression(progression):
    
    def __init__(self,base=2,start=1):
        super().__init__(start)
        self._base = base
    
    def _advance(self):
        self._current *= self._base
        

class fibonacciprogression(progression):
    
    def __init__(self,first=0,second=1):
        super().__init__(first)
        self._prev = second - first
    
    def _advance(self):
        self._prev, self._current = self._current, self._prev + self._current

#####################################################################################################################

# warmtones = ['red','blue','green']
# print("warmtones: ",warmtones)
# palette = warmtones
# print("palette: ", palette)
# palette[0] = 'magenta'
# print("warmtones: ",warmtones)
# print("palette: ", palette)
# we made changes in the palette but change was reflected in warmtones as well.

# warmtones = ['red','blue','green']
# print("warmtones: ",warmtones)
# palette = list(warmtones) # shallow copy
# print("palette: ", palette)
# palette[0] = 'magenta'
# print("warmtones: ",warmtones)
# print("palette: ", palette)
# change in palette was not reflected in warmtones

import copy
warmtones = ['red','blue','green']
print("warmtones: ",warmtones)
palette = copy.deepcopy(warmtones) # deep copy
print("palette: ", palette)
palette[0] = 'magenta'
print("warmtones: ",warmtones)
print("palette: ", palette)

#####################################################################################################################

# Recursive Factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    
factorial(5)

######################################################################################################################

# A recursive approach to Ruler Drawing

def draw_line(tick_length, tick_label =''):
    """Draw one line with gigen tick length (followed by opitonal label)."""
    line = '-' * tick_length
    if tick_label:
        line += '|' + tick_label
    print(line)
# draw_line(2)

def draw_interval(center_length):
    """Draw tick interval based upon a central tick length"""
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)

def draw_ruler(num_inches,major_length):
    """Draw English ruler with given number of inches, major tick length"""
    draw_line(major_length, '0')
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))
draw_ruler(4,3)

#######################################################################################################################

# Binary search

def binary_search(data, target, low, high):
    """Return True if target is found in indicated portion of a Python list
    The search only considers the portion from data[low] to data[high] inclusive"""
    if low > high:
        return False
    else:
        mid = (low + high)/2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low,mid - 1)
        else:
            return binary_search(data, target,mid + 1,high)

#######################################################################################################################

# Recursive function for reporting disk usage of a file system

import os

def disk_usage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)
    print('{0:<7}'.format(total),path)
    return total

# disk_usage('C:\maths\Data Science\python')

#######################################################################################################################