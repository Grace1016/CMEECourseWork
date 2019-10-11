birds = ( ('Passerculus sandwichensis','Savannah sparrow',18.7),
          ('Delichon urbica','House martin',19),
          ('Junco phaeonotus','Yellow-eyed junco',19.5),
          ('Junco hyemalis','Dark-eyed junco',19.6),
          ('Tachycineata bicolor','Tree swallow',20.2),
         )

#(1) Write three separate list comprehensions that create three different
# lists containing the latin names, common names and mean body masses for
# each species in birds, respectively.
latin_name = [w[0] for w in birds] 
common_name = [w[1] for w in birds]
mean_body_masses = [w[2] for w in birds]
print("The latin names: ", latin_name)
print("The common names: ",common_name)
print("The mean body masses: ",mean_body_masses)

# (2) Now do the same using conventional loops (you can choose to do this 
# before 1 !). 

latin_name=[]
common_name=[]
mean_body_masses=[]
for w in birds:
    latin_name.append(w[0])
    common_name.append(w[1])
    mean_body_masses.append(w[2])
print("The latin names: ", latin_name)
print("The common names: ",common_name)
print("The mean body masses: ",mean_body_masses)