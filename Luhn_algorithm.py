import time

def execution_time(func):
    def wrapped_f(*args):
        time_mark = time.time()
        func(*args)
        time.sleep(1)
        exec_time = time.time() - time_mark
        print(f"Execution time is {exec_time} seconds")
        return func
    return wrapped_f

@execution_time
def luhn(number):
    digits = [int(x) for x in ''.join(number.split())]
    even = [x * 2 if x * 2 <= 9 else x * 2 - 9 for x in digits[-2::-2]]
    odd = [x for x in digits[-1::-2]]
    print(sum(even+odd))        #Сумма должна быть кратна 10

luhn(input("Введите номер карты:\n"))