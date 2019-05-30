#declara an empty list
'''
classmates = []

#add item to list
classmates.append('Sue')
classmates.append('shad')
classmates.append('Sayank')
classmates.append('Gus')
classmates.append('Chin')
classmates.append('Eva')
classmates.append('Jeremy')
classmates.append('Dan')
classmates.append('Julian')
classmates.append('Aaron')

'''

#access an item at a specific position
#print(classmates[0])

#print(classmates[5]) # fifth element

'''
#get the size of the list
print(len(classmates))

#remove an item from the end of the list
classmates.pop()

#insert at specific positon
classmates.insert(0, 'Aaron')

#remove an item from the list

classmates.remove('Gus')
'''

#edit an item in the list
'''
classmates[1]= 'Sue Work'
''' 

#iterate over a list
'''
for classmate in classmates:
    if(classmate == 'Gus'):
        print('Great, Gus is in the class!')


#edit element while iterating
for index, classmate in enumerate(classmates):
    classmates[index] = classmate.upper()

print(classmates)

'''

#create a list of all the marvel movies from Iron man to End game

new_list = []

marvel_movie = ['Iron Man', 
    'The Incredible Hulk', 
    'Iron Man 2', 
    'Thor', 
    'Captain America',
    'The Avengers',
    'Iron Man',
    'Thor: The Dark World',
    'Winter Soldier',
    'Guardians of the Galaxy', 
    'Avengers: Age of Ultron',
    'Ant-man',
    'Civil War',
    'Doctor Strange', 
    'Guardians of the Galaxy Vol. 2', 
    'Spider-Man',
    'Thor: Ragnarok',
    'Black Panther', 
    'Avengers: Infinity War',
    'Ant-Man and the Wasp',
    'Captain Marvel', 
    'Avengers: Endgame']
    

for movie in marvel_movie:
        if 'the' in movie.lower():
                new_list.append(movie)

print(new_list)

#get-index of list
for index in range(len(marvel_movie)):
        print(index)


'''
for index, movie in enumerate(marvel_movie):
    marvel_movie[index] = marvel_movie[index].lower()
    if "the" in marvel_movie.lower():
        marvel_movie.append(movie)
        #print(movie)


print(marvel_movie)

'''