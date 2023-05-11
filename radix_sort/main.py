import random as rn   
import time as t                     

while True:
    do_output = False
    sort_type = "lsd"

    if input("Ausgabe von Input und Output (y/n) > ") == "y": do_output = True
    else: do_output = False

    if input("Radixsort Typ (lsd/msd) > ") == "msd": sort_type = "msd"
    else: sort_type = "lsd"
    
    maximum_number = int(input("Höchste Zahl > "))
    amount_of_data = int(input("Länge der Liste > "))

    def lsd_radix_sort(data):
        for digit in range(0, len(str(max(data)))): 
            buckets = [[] for x in range(10)]          
            for number in data: buckets[(number // 10 ** digit) % 10].append(number)
            data = [buckets[i][k] for i in range(10) for k in range(len(buckets[i]))]                  
        return data
    
    def msd_radix_sort(data, digit):
        if len(data) <= 1 or digit == -1: return data
        result = []
        buckets = [[] for x in range(10)]
        try: 
            for number in data: buckets[(number // 10 ** digit) % 10].append(number)
            for sublist in buckets: result += msd_radix_sort(sublist, digit - 1)
        except TypeError: return
        return result

    data = [rn.randint(0, maximum_number) for x in range(amount_of_data)]

    if do_output is True: print(f"\n{data}\n") 

    start_time = t.time() 
    if sort_type == "lsd": data = lsd_radix_sort(data)
    else: data = msd_radix_sort(data, len(str(max(data))) - 1)
    end_time = t.time() 

    if do_output is True: print(f"{data}\n") 

    print(f"Benötigte Zeit: {end_time - start_time}s \n")







