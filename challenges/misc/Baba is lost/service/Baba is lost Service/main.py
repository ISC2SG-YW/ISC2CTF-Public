import random, math 
import os
def generate_grid(n):
    target_location = (random.randint(0,n-1),random.randint(0,n-1))
    baba_location = target_location 
    while baba_location == target_location:
        baba_location = (random.randint(0,n-1),random.randint(0,n-1))
    return target_location, baba_location

def determine_direction(target_location,baba_location):
    directions = {
        (0,1):"S",
        (0,-1):"N",
        (1,0):"E",
        (-1,0):"W",
        (1,1):"SE",
        (-1,-1):"NW",
        (1,-1):"NE",
        (-1,1):"SW"
    }
    direction_vector = (target_location[0]-baba_location[0],target_location[1]-baba_location[1])
    direction = (direction_vector[0]//abs(direction_vector[0]) if direction_vector[0] != 0 else 0,\
                direction_vector[1]//abs(direction_vector[1]) if direction_vector[1] != 0 else 0)
    return directions[direction]

def giveTestCase(testNo):
    print("Test Case ",testNo)
    n = 10**testNo 
    target_location, baba_location = generate_grid(n)
    print(n)
    print(" ".join(map(str,baba_location)))
    print(determine_direction(target_location,baba_location))
    for i in range(math.ceil(math.log2(n))):
        newlocation = input().split(" ")
        if len(newlocation) != 2:
            print("Invalid Input")
            return False 
        try:
            newlocation = (int(newlocation[0]),int(newlocation[1]))
        except:
            print("Invalid Input")
            return False
        if newlocation == target_location:
            print("You have arrived at Singapore!")
            return True
        else:
            print(determine_direction(target_location,newlocation))
    print("You have run out of moves!")
    return False
    
def main():
    for i in range(1,11):
        success = giveTestCase(i)
        if not success:
            return 
    print(f"All test cases passed! Heres the flag: {os.getenv('FLAG')}") 
    
if __name__ == "__main__":
    main()