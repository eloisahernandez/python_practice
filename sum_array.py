
def run_test(success):
    if success:
        print("✔️")
    else:
        print("❌")




# return the sum of the 2 dimensional array
def sum_array(arr):
    sum_n = 0

    for ls in arr:
        #print(ls)
        for n in ls:
            #print (n)
            sum_n = sum_n + n  
            #print (sum_n)
    return sum_n


run_test(sum_array([[1, 2], [3, 4]]) == 10)
run_test(sum_array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 9)





