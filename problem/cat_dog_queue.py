# implement a dog and cat queue structure. the requirements are as below:
# user can put class cat and class dog into a queue. user can use pollAll method
# to retrieve from queue based on the sequence of queue input. user can call
# pollCat to retrieve the cat based on the queue order.
# call pollDog to retrieve the dog based on the same way
# user can call isDogEmpty and isCatEmpty to check whether there is dog or cat
from collections import deque
class Pet():
    type = ""
    
    def __init__(self, type):
        self.type = type

    def getPetType(self):
        return self.type

class Dog(Pet):
    def __init__(self):
        Pet.__init__(self, "dog")

class Cat(Pet):
    def __init__(self):
        Pet.__init__(self, "cat")

class PetGetin():
    pet = None
    cnt = 0

    def __init__(self, pet, cnt):
        self.pet = pet
        self.cnt = cnt
        #print(pet.type)
        #print(pet.getPetType())

    def getPet(self):
        return self.pet

    def getCnt(self):
        return self.cnt

    def GetinPetType(self):
        return self.pet.getPetType()

class PetCatQueue():
    catq = deque()
    dogq = deque()
    cnt = 0

    def add(self, pet):
        if (pet.getPetType() == "dog"):
            self.dogq.append(PetGetin(pet, self.cnt)) 
            self.cnt += 1
            #print(self.dogq.popleft().getPet().getPetType())
        elif (pet.getPetType() == "cat"):
            self.catq.append(PetGetin(pet, self.cnt)) 
            self.cnt += 1
        else:
            print("not cat or dog")
            return

    def pollDog(self):
        if (len(self.dogq) != 0):
            return self.dogq.popleft().getPet()
        else:
            print("dog queue is empty")

    def pollCat(self):
        if (len(self.catq) != 0):
            return self.catq.popleft().getPet()
        else:
            print("cat queue is empty")

    def pollAll(self):
        if (len(self.dogq) != 0 and len(self.catq) != 0):
            dogTemp = self.dogq.popleft()
            catTemp = self.catq.popleft()
            if (dogTemp.getCnt() < catTemp.getCnt()):
                self.catq.appendleft(catTemp)
                return dogTemp.getPet()
            else:
                self.dogq.appendleft(dogTemp)
                return catTemp.getPet()
        elif (len(self.dogq) != 0):
            return self.dogq.popleft().getPet()
        elif (len(self.catq) != 0):
            return self.catq.popleft().getPet()
        else:
            print("queue is empty")

    def isDogEmpty(self):
        if(len(dogq) == 0):
            print("dog queue is empty")
        else:
            print("dog queue is not empty")

    def isCatEmpty(self):
        if(len(catq) == 0):
            print("cat queue is empty")
        else:
            print("cat queue is not empty")


if __name__ == "__main__":
    myPet1 = Dog()
    myPet2 = Cat()
    myPet3 = Dog()
    myPet4 = Dog()
    myPet5 = Cat()
    myPet6 = Cat()
    #getin = PetGetin(myPet1, 1)
    #getin = PetGetin(myPet2, 2)
    #print(getin.GetinPetType())
    #print(getin.getCnt())
    queueKO = PetCatQueue()
    queueKO.add(myPet1)
    queueKO.add(myPet2)
    queueKO.add(myPet3)
    queueKO.add(myPet4)
    queueKO.add(myPet5)
    queueKO.add(myPet6)
    print(queueKO.pollDog().getPetType())
    print(queueKO.pollCat().getPetType())
    print(queueKO.pollAll().getPetType())
    print(queueKO.pollAll().getPetType())
    print(queueKO.pollAll().getPetType())
    print(queueKO.pollAll().getPetType())
    #print(queueKO.pollCat().getPetType())



