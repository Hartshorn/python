class Point(object):
    
    def __init__(self, x, y, has_animal, has_plant, animal):
        self.x = x
        self.y = y
        self.has_animal = has_animal
        self.has_plant = has_plant
        self.Animal = animal
    
    def __str__(self):
        return "({}, {})\nHas animal: {}\nHas plant: {}\n{}".format(
            self.x, self.y, self.has_animal, self.has_plant, self.Animal)
    
    def location(self):
        return (self.x, self.y)
            
class Animal(object):
    
    def __init__(self, energy, direction, genes):
        self.energy = energy
        self.direction = direction
        self.genes = genes
        
    def __str__(self):
        return "Energy: {}, Direction: {}, Genes: {}".format(
            self.energy, self.direction, self.genes)
            
    def copy(self):
        return Animal(self.energy, self.direction + 1, self.genes)
            
def animal_reproduce(Animal):
    
    
        Animal.energy /= 2
        temp_animal = Animal.copy()
        temp_animal.direction += 1
        temp_animal.genes[3] += 1
        
        return True
    # else:
    #     return False
        
def attempt_to_add(new_point, world):
    for i in range(len(world)):
        if world[i].location() == (new_point.x, new_point.y):
            new_point.x += 1
            new_point.y += 1
            return new_point
            # attempt_to_add(new_point, world)
        else:
            return new_point
    
def draw_world(world):
    
    for y in range(width):
        print("|", end="")
        for x in range(height):
            for point in world:
                if point.x == x and point.y == y:
                    if point.has_animal:
                        print("M", end="")
                    elif point.has_plant:
                        print("*", end="")
                    else:
                        print(" ", end="")
                else:
                    print(".", end="")
        print("|\n", end="")
        

width   = 10
height  = 10
plt_nrg = 80
rep_nrg = 200

world = []
keep  = []

animal_1 = Animal(1000, 0, [1,2,3,4,5,6,7,8])

first = Point(1,2, True, False, animal_1)

world.append(first)

for n in range(2):
    for i in range(len(world)):
        if animal_reproduce(world[i].Animal):
            print('in')
            world.append(Point(world[i].x, world[i].y, 
                               world[i].has_animal, world[i].has_plant,
                               attempt_to_add(world[i], world)))
                     


for i in world:
    print(i)
print("Total: {}".format(len(world)))

draw_world(world)