
def run_test(success):
    if success:
        print("✔️")
    else:
        print("❌")



# return the sum of the 2 dimensional array
# Iterate over indices rather than the items in the list
# Hint: use the 'range' function to get indices, and name loop variable using i,j,k to signify that they are indices not values
def sum_array(arr):
    ls = []
    sum_n = 0

    for i in range(len(arr)):
        ls = arr[i]
        for j in range(len(ls)):
            n = ls[j]
            sum_n += n  # arr[i][j]
    return sum_n




run_test(sum_array([[1, 2], [3, 4]]) == 10)
run_test(sum_array([[1, 1, 1], [1, 1], [1, 1, 1]]) == 8)





