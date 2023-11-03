
def details(name, age, weight, height, nationality = "Indian"):
                                            #default argu

    print("name is",name)
    print("age is",age)
    print("weight is", weight)
    print("height is", height)
    print("nationality is", nationality)

# details("Ashok",45, height=5.7,weight=67)
        #position       keyword argu

details("Prem", 45, 67, 6.1, "Maharashtrian") #position argument

#keyword Argument

details(weight=56, age=31, name="Trupti", nationality="Indi",height=65)

#_______________________________________________
def is_prime(number):
    """
    Tells whether given number is prime or not
    :param number: int
    :return: returns true if prime else false
    """
    print(1)
    if number==1:
        return True, "prime"
    print(2)
    for i in range(2,number):
        print("*")
        if number%i==0:
            print(4)
            return False, "not prime"
        else:
            print(5)
            return True, "prime"
        print(6)

print(is_prime(23))
print(is_prime(1))
print(is_prime(4))

print(divmod(45,6))











