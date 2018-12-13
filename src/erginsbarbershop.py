'''
Shop:
Open for 8 hours, 9-5
2 shifts of barbers, 4 hours each
barbers1 = ['Lee', 'Dan', 'Brad', 'Darren']
barbers2 = ['Isaac', 'Chris', 'Cary', 'Ivan']
Cut takes 20-40 minutes

Customers:
Customer1-n
Show up an average of every 10 minutes
Can only have 15 at a time
A customer waits 30 minutes then leaves
'''
import numpy.random as npr
import scipy.stats as ss


class Barbershop(object):
    def __init__(self):
        ## closing time is at 480, shift change is at 240
        self.time = 0
        self.queue = Queue()
        self.customer_interval = 10
        self.shifts = [[0,240],[240,480]]
        self.braber_names = [['Lee', 'Dan', 'Brad', 'Darren'],['Isaac', 'Chris', 'Cary', 'Ivan']]
        self.finished_customers = []
        self.expired_customers = []



    def run_shift(self,barber_list,shift_time):
        self.start_barbers(barber_list)
        for self.time in range(shift_time[0],shift_time[1]):
            self.check_new_customer()
            if self.is_barber_available() and self.is_customer_waiting():
                self.assign_new_customer()

    def run(self):
        for shift_time, barber_list in zip(self.shifts,self.braber_names):
            self.run_shift(barber_list,shift_time)
        self.list_finished_customers()

    def start_barbers(self,barber_list):
        self.barbers = [Barber(name) for name in barber_list]


    def list_finished_customers(self):
        for c in self.finished_customers:
            print c.arrival_time,c.start_time,c.cut_time, c.barber_name

    def assign_new_customer(self):
        available_barbers = self.get_available_barbers()
        next_customer = self.queue.get_next_customer()
        barber_ind = npr.randint(0,len(available_barbers))
        available_barbers[barber_ind].assign(next_customer,self.time)
        self.finished_customers.append(next_customer)

    def check_new_customer(self):
        if npr.rand()<ss.expon.cdf(1.0/self.customer_interval):
            self.queue.add(Customer(self.time))

    def get_available_barbers(self):
        return [barber for barber in self.barbers if barber.finishtime <= self.time]

    def is_barber_available(self):
        return len(self.get_available_barbers())>0

    def is_customer_waiting(self):
        return len(self.queue.customer_list)>0

    def check_expired_customers(self):
        pass

class Queue(object):
    def __init__(self):
        self.customer_list = []

    def add(self,customer):
        self.customer_list.append(customer)

    def get_next_customer(self):
        return self.customer_list.pop(0)



class Barber(object):
    def __init__(self, name):
        self.name = name
        self.shift = None
        self.customer = None
        self.starttime = None
        self.finishtime = 0

    def assign(self,customer,time):
        self.customer = customer
        self.finishtime = time + customer.cut_time
        customer.start_time = time
        customer.barber_name = self.name


class Customer(object):
    def __init__(self, arrival_time):
        self.cut_time = npr.randint(20,41)
        self.arrival_time = arrival_time
        self.start_time = None
        self.barber_name = ""
