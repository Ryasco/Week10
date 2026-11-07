class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
   '''
    
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        self.friends.append(friend)

Ryan = Person("Ryan")
Heather = Person("Heather")
print(Ryan.friends)
Ryan.add_friend(Heather)
print(Ryan.friends[0].name)  



class SocialNetwork:
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''
    
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        if person1_name in self.people and person2_name in self.people:
            person1 = self.people[person1_name]
            person2 = self.people[person2_name]

            person1.add_friend(person2)
            person2.add_friend(person1)

    def print_network(self):
        for person in self.people.values():
            friend_names = [friend.name for friend in person.friends]
            print(f"{person.name}: {', '.join(friend_names)}")

network = SocialNetwork()
network.add_person("Ryan")
network.add_person("Heather")
print(network.people)

network.add_person("Alice")
network.add_person("Bob")
network.add_person("Charlie")
network.add_person("David")
network.add_person("Ryan")

network.add_friendship("Alice", "Bob")
network.add_friendship("Bob", "Charlie")
network.add_friendship("Alice", "Charlie")
network.add_friendship("Ryan", "Heather")
network.add_friendship("David", "Susan")
network.add_friendship("Alice", "David")
network.add_friendship("Bob", "David")
network.add_friendship("Charlie", "David")

network.print_network()



# Test your code here