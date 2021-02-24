from animals import Animal, Person, Cat

if __name__ == '__main__':
    animal1 = Animal(10)
    animal1.set_name('Spot')
    # animal1.speak()

    # cat1 = Cat(5)
    # print(cat1)
    # cat1.speak()

    # person1 = Person("Kim", 25)
    # person1.add_friend('Jane')
    # person1.add_friend('Raj')
    # print(f'{str(person1)} has {len(person1.friends)} friends')

    cat1 = Cat(5)
    cat2 = Cat(5)
    cat3 = Cat(6)
    print(cat1 == cat2)
    print(cat2 == cat3)

    person1 = Person("Kim", 25)
    person2 = Person("Jane", 22)
    person1.age_diff(person2)