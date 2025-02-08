foods = ["rice", "beans", "yam", "potatoes", "noodles", "cassava"]
print(foods[3])
foods.append("fufu")
print(foods)
foods.pop()
print(foods)
foods.sort()
print(foods)
# foods.clear()
print (foods)
foods.reverse()
foods.remove("yam")
print(foods)


#dictionary
student1 = {
    "name":"Vivian",
    "age" : 14,
    "hobby" : "Reading Stories and Coding"
}
print(student1 ["hobby"])
student1["name"] = "Nwasinachi"
print(student1)
student1.clear()
print(student1)

#project
import random
    
num = random.randint(1, 10)
guess = None
    
while guess != num:
    guess = input("guess a number between 1 and 10: ")
    guess = int(guess)
    
    if guess == num:
        print("congratulations! you won!")
        break
    else:
        print("nope, sorry. try again!")