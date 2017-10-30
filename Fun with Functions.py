def oddEven():
    for i in range(1,2001):
        if i % 2 == 0:
            print "Number is" + " " + str(i) + "." + "This is an even number"
        else:
            print "Number is" + " " + str(i) + "." + "This is an odd number"

print oddEven()

def multiply(arr,mul):
    for i in range(0,len(arr)):
        arr[i] *= mul
    return arr

    
a = [2,4,10,16]
print multiply(a,5)

def layered_multiples(arr):
    print arr
    new_array = []
    for x in arr:
        val_arr = []
        for i in range(0,x):
            val_arr.append(1)
        new_array.append(val_arr)
    return new_array
x = layered_multiples(multiply([2,4,5],3))
print x

        