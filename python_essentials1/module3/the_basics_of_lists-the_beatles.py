# step 1
beatles = []
print("Step 1:", beatles)

# step 2
beatles.append ('John Lennon')
beatles.append ('Paul McCartney')
beatles.append ('George Harrison')
print("Step 2:", beatles)

# step 3
for i in range (2):
    beatles.append (input ("Add to the Beatles list Stu Sand Pete one after another: "))
print("Step 3:", beatles)

# step 4
del beatles [-1]
del beatles [-1]
print("Step 4:", beatles)

# step 5
beatles.insert (0, 'Ringo Starr')
print("Step 5:", beatles)


# testing list length
print("The Fab", len(beatles))