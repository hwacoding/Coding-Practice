arr=[1,2,3,4]

def gen_combinations(arr, n):
    result=[]

    if n==0:
        print(result)
        return

    rest_arr=arr
    for i in range(len(arr)):
        result.append(arr[i])
        rest_arr.remove(arr[i])
        gen_combinations(rest_arr,n-1)


gen_combinations(arr,3)
print(arr)