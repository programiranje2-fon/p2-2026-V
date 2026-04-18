"""
Vezbe, dvocas 4
"""
from functools import reduce

def compute_product(*numbers, squared=False):
    # p = 1
    # for number in numbers:
    #     p *= number if not squared else number**2
    # return p

    # Option 2
    return reduce(lambda a,b: a*b, [n**2 if squared else n for n in numbers])


def select_strings(*strings, threshold=3):
    # selection = []
    # for s in strings:
    #     if s[0].lower() == s[-1].lower() and len(set(s)) > threshold:
    #         selection.append(s)
    # return selection

    # Option 2
    # return [s for s in strings if s[0].lower() == s[-1].lower() and len(set(s)) > threshold]

    # Option 3
    return list(filter(lambda s: s[0].lower() == s[-1].lower() and len(set(s)) > threshold, strings))


def process_product_orders(orders, discount=None, shipping=10):

    def compute_tot_price(quantity, unit_price):
        tot_price = quantity * unit_price
        tot_price *= (1 - discount / 100) if discount else 1
        tot_price += shipping if tot_price < 100 else 0
        return tot_price

    # Option 1
    # orders_dict = dict()
    # for order in orders:
    #     order_id, _, quantity, unit_price = order
    #     # price = quantity * unit_price
    #     # price = price * (1-discount/100) if discount else price
    #     # price += shipping if price < 100 else 0
    #     orders_dict[order_id] = compute_tot_price(quantity, unit_price)
    # return orders_dict

    # Option 2
    # return {order_id: compute_tot_price(quantity, unit_price)
    #         for order_id, _, quantity, unit_price in orders}

    # Option 3
    return dict(map(lambda o: (o[0], compute_tot_price(o[2], o[3])), orders))


import functools
from time import perf_counter

def timer(func):
      @functools.wraps(func)
      def wrapper_timer(*args, **kwargs):

        start_time = perf_counter()

        vrednost = func(*args, **kwargs)

        tot_time = perf_counter() - start_time
        print(f"Funkcija {func.__name__} se izvrsila za {tot_time:.4f}s")

        return vrednost
      return wrapper_timer


@timer
def compute_sum_loop(n):
    s = 0
    for x in range(1, n+1):
        for i in range(1, x+1):
            s += i
    return s

@timer
def compute_sum_lc(n):
    # 1, 2, ... n
    # S(1), S(2), S(3), ... S(n)
    # sum([S(1), S(2), S(3), ... S(n)])
    # S(x) = 1 + 2 + ... + x
    # S(x) = sum([1, 2, ... x])
    return sum([sum(range(1, x+1)) for x in range(1, n+1)])

@timer
def compute_sum_mr(n):
    # 1, 2, ... n -> S(1), S(2), S(3), ... S(n) map
    # S(1), S(2), S(3), ... S(n) -> S(1) + S(2) + S(3) + ... + S(n) reduce
    mapped_vals = map(lambda x: sum(range(1, x+1)), range(1, n+1))
    return reduce(lambda a,b: a+b, mapped_vals)


def standardizer(func):
    @functools.wraps(func)
    def wrapper_standardizer(*args, **kwargs):

        if all(isinstance(a, (int, float)) for a in args):
            from statistics import mean, stdev
            m = mean(args)
            sd = stdev(args)
            args = list(map(lambda a: (a-m)/sd, args))
        else:
            print("Standardizacija ulaznih argumenata nije uradjena jer nisu svi brojevi")

        print(f"Poziva se funkcija {func.__name__} sa sledecim ulaznim argumentima:")
        print("\t- pozicioni argumenti:" + ", ".join([f"{arg:.4f}" for arg in args]))
        print("\t- imenovani argumenti: " + ", ".join([f"{name}={val}" for name, val in kwargs.items()]))

        vrednost = func(*args, **kwargs)

        vrednost = round(vrednost, 4)

        return vrednost

    return wrapper_standardizer


@standardizer
def sum_of_sums(*numbers, n=10):
    # S(x) = 1 + x + x**2 + x**3 + ... + x**n
    return sum([sum([number**i for i in range(0,n+1)]) for number in numbers])


if __name__ == "__main__":

    # ZADATAK 1
    # print(compute_product(1,-4,13,2))
    # print(compute_product(1, -4, 13, 2, squared=True))
    # print()

    # # Calling the compute_product function with a list
    # num_list = [2, 7, -11, 9, 24, -3]
    # # This is NOT a way to make the call:
    # print("Calling the function by passing a list as the argument")
    # print(compute_product(num_list))
    # print()
    #
    # # instead, this is how it should be done (the * operator is 'unpacking' the list):
    # print("Calling the function by passing an UNPACKED list as the argument")
    # print(compute_product(*num_list))


    # ZADATAK 2
    # str_list = ['yellowy', 'Bob', 'lovely', 'Yesterday', 'too']
    # print(select_strings(*str_list))


    # ZADATAK 3
    # orders = [("34587", "Learning Python, Mark Lutz", 4, 40.95),
    #           ("98762", "Programming Python, Mark Lutz", 5, 56.80),
    #           ("77226", "Head First Python, Paul Barry", 3, 32.95),
    #           ("88112", "Einführung in Python3, Bernd Klein", 3, 24.99)]
    #
    # print(process_product_orders(orders))
    # print()
    # print("The same orders with discount of 10%")
    # print(process_product_orders(orders, discount=10))


    # ZADATAK 4
    # print(compute_sum_loop(10000))
    # print()
    # print(compute_sum_lc(10000))
    # print()
    # print(compute_sum_mr(10000))


    # ZADATAK 5
    print(sum_of_sums(1,3,5,7,9,11,13, n=7))