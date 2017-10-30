l = ['magical','unicorns']
# string = ""
# add = 0
# for i in l:
#     if type(i) == str:
#         string += i
#     if type(i) == int or type(i) == float:
#         add += i
# # print "String: " + string
# # print "Sum:",add


# int == True
# str == True
# for i in l:
#     if not type(i) == int or not type(i) == float:
#         int == False
#         else print "The list you entered is of integer type"
#     if not type(i) == str:
#         str == False
#         else print "The list you entered is of string type"
#     if str == False and int == False:
#         print "The list you entered is of mixed type"
new_string = ""
total = 0
for i in l:
    if isinstance(i, int) or isinstance(i, float):
        total += i
    elif isinstance(i, str):
        new_string += i
    
if new_string and total:
    print "The array you entered is of mixed type"
    print "String:", new_string
    print "Sum:", total

elif new_string:
    print "The array you entered is of string type"
    print "String:", new_string

else:
    print "The array you entered is of number(float or int) type"
    print "Sum:", total








