# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?
num = 13195

def get_prime(num):
    for i in range(num, -1, -1):
        
        if i != 0:
            result = num/i
          
            if result%2==1:
                return(i)

                
print(get_prime(num))
