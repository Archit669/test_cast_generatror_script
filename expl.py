import random
import bisect

# def binarySearch(arr, ele):
#     low = 0
#     high = len(arr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == ele:
#             return mid
#         elif arr[mid] > ele:
#             high = mid - 1
#         elif arr[mid] < ele:
#             low = mid + 1
#     return low

def binarySearch(nums, target):
    if not nums:
        return [-1, -1]
    
    left,right = bisect.bisect_left(nums, target), bisect.bisect_right(nums, target)
   
            
    return  [left, right - 1] if left < right else [-1, -1]

for case in range(51):
    arr=[]
    target = random.randint(1,10**7)
    size = random.randint(1, 10**7)
    for x in range(1, size):
        temp = random.randint(1,10**7)
        arr.append(temp)

    for i in range(1, 10**2):
        arr.append(target)

    inp = sorted(arr)
    #print("Input: ",inp)
    if case >9:
        filename= "input/input" + str(case) + ".txt"
    else:
        filename= "input/input0" + str(case) + ".txt"


    f = open(filename,"w+")
    f.write(str(len(inp))+"\n")

    # size 
    f.write(str(target) + "\n")
    for i in inp:
        #print(i)
        f.write(str(i) + " ")

    f.close()


    out = binarySearch(inp,target)
    print("Output: ",out)
    if case >9:

        filename= "output/output" + str(case) + ".txt"
    else:
        filename= "output/output0" + str(case) + ".txt"
    f = open(filename,"w+")
    f.write(str(out[0]) + "\n" )
    f.write(str(out[1]) )
    f.close()

# for case in range(101):

#     arr=[]
#     for x in range(1, 27*10**5): #"""random.randint(1,10**4)"""
#         arr.append(random.randint(1,10**7))
#     target = random.randint(1,10**7)
#     arr = list(set(arr))
#     #arr.append(target)
#     #arr = [i for x in range(random.randint(1,10)) i=10]
#     inp = sorted(arr)
#     #print("Input: ",inp)
#     if case >9:
#         filename= "input/input" + str(case) + ".txt"
#     else:
#          filename= "input/input0" + str(case) + ".txt"
#     f = open(filename,"w+")
#     f.write(str(len(inp))+"\n")
#     for i in inp:
#         #print(i)
#         f.write(str(i)+"\n")
#     f.write(str(target))
#     f.close()
#     out = binarySearch(inp,target)
#     print("Output: ",out)
#     if case >9:
#         filename= "output/output" + str(case) + ".txt"
#     else:
#          filename= "output/output0" + str(case) + ".txt"
#     f = open(filename,"w+")
#     f.write(str(out))
#     f.close()
