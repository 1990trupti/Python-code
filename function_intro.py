

s3 = "Today is thursday"
set1 = {10, 20, 30, 40, 50}
weakdays =("Monday", "Tuesday", "Wednesday","Thursday","Friday","Saturady","Sunday")
type_of_denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
indian_team = {
                "captain":"Rohit Sharma",
                "vc":"KL Rahul",
                "batsmen":["virat Kohli", "surya", "pujara"],
                "all_rounder":["axar patel", "ravindra jadeja"],
                "bowlers":{
                   "fast":["shami","siraj","bumrah"],
                   "spin":["kuldeep","cahal"]
                          },
                "coach":"rahul dravid"
             }

# print(len(s3))
# print(len(set1))
# print(len(weakdays))
# print(len(type_of_denominations))
# print(len(indian_team))


# n = int(input("Enter a number"))
#
# for i in range(2,n):
#     if n%i==0:
#         print("not prime")
#         break
# else:
#     print("prime")

#_______________________________________________________________________________________

# syntax:
#def <name_for _function>():
# lines


#using function()
# using def keyword means it is user define function


def is_prime():
    n = int(input("Enter a number"))
    for i in range(2,n):
        if n%i == 0:
            print("not prime")
            break
    else:
        print("prime")
is_prime()
is_prime()
is_prime()




# def function_name2(a, b, c, d):
#     print("parametrized")
#
#     for i in range(6):
#         if i%2==0:
#             print("*")
#         else:
#             print("#")
#
# function_name2(10,20,30,40)
#
# def is_prime(number):
#     """
#     Tells whether given number is prime or not
#     :param number: int
#     :return: returns true if prime else false
#     """
#     for i in range(2,n):
#         if number%i==0:
#             return False
#         else:
#             return True
#
# if is_prime(23):
#     print("Prime")

# if not is_prime(56):
#     print("Not Prime")











