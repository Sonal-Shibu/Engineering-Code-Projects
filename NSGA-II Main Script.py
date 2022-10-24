# -------------- Multiobjective using Genetic Algorithims - NSGA-II by Binary Sequencing as Weighting Functions -------------- #
import numpy
import random
import sys

# READ THE USER MANUAL BEFORE STARTING # 
#%% Constants
Global_Population_Maximise=[] # For Fin problem this is being maximised
Global_Population_Minimise=[] # For Fin problem this is being minimised

Population_Maximise=int(12) #Elements - Maximise of the fin
Population_Minimise=int(9) #Elements - Minimise of the fin
Generations=int(20)
Population_Size=int(30) # Number of parents EVEN number

Binary_Population_Maximise=[]# Maximise Parent Population before generation # Maximumise
Binary_Population_Minimise=[] # Minimise Parent Population before generation # Minimise
#%%
if Population_Size %2 !=0:    
    print("The current population is not valid as",Population_Size, "is not even. Choose another even interger")
    sys.exit()

# Data from Pham and Karaboga 2000
if Population_Size <= 30: #Schaffer
    
    mutation_rate=(float(random.uniform(0.005, 0.01)))
    Crossover_rate=(float(random.uniform(0.75, 0.95)))

elif 31 >= Population_Size or Population_Size <= 50:  #Grefenstette
    
    mutation_rate=float(0.01)
    Crossover_rate=float(0.92)

elif Population_Size>51: #De Jong
    
    mutation_rate=float(0.001)
    Crossover_rate=float(0.6)


#%%
for z in range(0,Generations): # No. of iterations

    
    del Binary_Population_Maximise,Binary_Population_Minimise
    Binary_Population_Maximise=[]# Maximise Parent Population before generation # Maximumise
    Binary_Population_Minimise=[] # Minimise Parent Population before generation # Minimise
    
    for i in range(1,Population_Size+1): #Creating the Binary Array
        Binary_Population_Maximise.append((numpy.random.randint(2, size=Population_Maximise))) # Creating the binary array using numbers between 0 and 2 with a specific size
        Binary_Population_Minimise.append((numpy.random.randint(2, size=Population_Minimise)))
        
        
# ---------------------- Mutation ---------------------- #
#Maximise
#muation is when an element in the array when choosen switches information. For example when the element is 1 it will flip to 0.
    #mutation_rate=float(random.uniform(0.01, 0.1)) # this needs to change
    for i in range(0,(len(Binary_Population_Maximise))): #rows
        for j in range (0,(len(Binary_Population_Maximise[0]))): #columns
            if mutation_rate <= (float(random.uniform(0.001, 0.01))): #If left and part of the identies match swap the elements
                if Binary_Population_Maximise[i][j]==0:
                    Binary_Population_Maximise[i][j]=1
                else:
                        Binary_Population_Maximise[i][j]=0       
        
#Minimise
#Same principle here just for another array
    for i in range(0,(len(Binary_Population_Minimise))): #rows
        for j in range (0,(len(Binary_Population_Minimise[0]))): #columns
            if mutation_rate <= (float(random.uniform(0.001, 0.01))):
                if Binary_Population_Minimise[i][j]==0:
                    Binary_Population_Minimise[i][j]=1
                else:
                    Binary_Population_Minimise[i][j]=0

# ---------------------- Crossover ---------------------- #
#Crossover is when two elements are chosen in random and swapped. This differs from mutation as, when the elements are chosen they dont switch,
#flip bits as the can be the same bit being swapped. The main reason of this function is swaping elements in the least sigfinicant bits and most sigfinicant bits  
    del i,j
#Maximise
    
    for i in range(0,(len(Binary_Population_Maximise))): #rows
        for j in range (0,(len(Binary_Population_Maximise[0]))): #columns
            if Crossover_rate>=(float(random.uniform(0.74, 1.00))):
                
                a=random.randint(0, (Population_Maximise-1)) #choose a random number with the ranges of the Maximises of thearrays
                b=random.randint(0, (Population_Size-1))
                c=random.randint(0, (Population_Maximise-1))
                d=random.randint(0, (Population_Size-1))
                
                x=Binary_Population_Maximise[b][a] #store the elements in this array with indexing
                y=Binary_Population_Maximise[d][c]
                
                Binary_Population_Maximise[i][j]=x #here we can swap them as it being indexing from the "looking index for loop"
                Binary_Population_Maximise[i][j]=y
                
                del a,b,c,d,x,y
                
#Minimise
                
    for i in range(0,(len(Binary_Population_Maximise))):
        for j in range (0,(len(Binary_Population_Maximise[0]))):
            if Crossover_rate>=(float(random.uniform(0.74, 1.00))):
                a=random.randint(0, (Population_Maximise-1))
                b=random.randint(0, (Population_Size-1))
                c=random.randint(0, (Population_Maximise-1))
                d=random.randint(0, (Population_Size-1))
                    
                x=Binary_Population_Maximise[b][a]
                y=Binary_Population_Maximise[d][c]
                    
                Binary_Population_Maximise[i][j]=x
                Binary_Population_Maximise[i][j]=y
                del a,b,c,d,x,y
     
            
# ---------------------- Binary Sequence ---------------------- #            

#Maximise
            
    Binary_Sequence_Maximise=numpy.zeros(Population_Maximise)#,dtype=numpy.int32)#Intialising the array
    Binary_Sequence_Maximise[0]=1 # This is an important parameter as this is reference element used to double the next element in the following for loop

    for i in range(1,Population_Maximise): #This creates a binary array [1 2 4 8 etc] which will be element by element multipied for the fitness functions later
        PreviousElementNumber=Binary_Sequence_Maximise[i-1] # this eqn says store the last element from the current index element
        Binary_Sequence_Maximise[i]=PreviousElementNumber*2 # and double it and store it in the current looking index
        if i==Binary_Population_Maximise: # this is to prevent spillages exceeding the array size
            break


    Real_Sequence_Maximise=Binary_Sequence_Maximise*Binary_Population_Maximise #element by element multiplication
    del PreviousElementNumber,i,j

#Minimise

    Binary_Sequence_Minimise=numpy.zeros(Population_Minimise)#,dtype=numpy.int32)#Intialising the array
    Binary_Sequence_Minimise[0]=1

    for i in range(1,Population_Minimise):
        PreviousElementNumber=Binary_Sequence_Minimise[i-1]
        Binary_Sequence_Minimise[i]=PreviousElementNumber*2
        if i==Binary_Population_Minimise:
            break

    Real_Sequence_Minimise=Binary_Sequence_Minimise*Binary_Population_Minimise
    
# ---------------------- Fitness ---------------------- # 
    
    Summed_Maximise_Vector = numpy.zeros(shape=(Population_Size, 1)) #Initialising Array 
    Summed_Minimise_Vector=numpy.zeros(shape=(Population_Size, 1)) #Initialising Array
        
    Summed_Maximise_Vector = Real_Sequence_Maximise.sum(axis=1) #Summing the arrays, to get intergers
    Summed_Minimise_Vector = Real_Sequence_Minimise.sum(axis=1) #Summing the arrays

    Summed_Maximise_Vector_Top_Half = Summed_Maximise_Vector [:len(Summed_Maximise_Vector )//2] #Split the arrays up
    Summed_Maximise_Vector_Bottom_Half  = Summed_Maximise_Vector [len(Summed_Maximise_Vector )//2:] #Split the arrays up

    Summed_Minimise_Vector_Top_Half = Summed_Minimise_Vector [:len(Summed_Minimise_Vector )//2] #Split the arrays up
    Summed_Minimise_Vector_Bottom_Half  = Summed_Minimise_Vector [len(Summed_Minimise_Vector )//2:] #Split the arrays up
    
# ---------------------- Competition ---------------------- # 
    del i
    
    x=float(random.uniform(0.001, 0.01)) # this is an important dummy variable. This is used to filter out the weaker parents from the compentation, real intergers can be used because all real intergers 
                                         #be summed up the use of binary sequencing
    # This is the competition case where we pit the elements against each other to see whos best, for the maximising function, the largest number should win and the minisming number should win
    # However it's all relative, as in the final array it is important to have some "poor" parents in final array to maximise the quality of results
    
    for i in range(0,(int((Population_Size/2)))):
        
        if Summed_Maximise_Vector_Top_Half [i] >= Summed_Maximise_Vector_Bottom_Half [i]:
            Summed_Maximise_Vector_Bottom_Half [i]=x
        else:
            Summed_Maximise_Vector_Top_Half [i]=x
                
    for j in range(0,(int((Population_Size/2)))):
        
        if Summed_Minimise_Vector_Top_Half [j] >= Summed_Maximise_Vector_Bottom_Half [j]:
            Summed_Minimise_Vector_Top_Half [j] =x
        else:            
            Summed_Minimise_Vector_Bottom_Half[j] =x

    Fitness_Maximise = numpy.hstack((Summed_Maximise_Vector_Top_Half,Summed_Maximise_Vector_Bottom_Half)) # This horzontailly stacks the array 
    Fitness_Maximise = [i for i in Fitness_Maximise if i != x]# this removes the weaker parents if the elemnts is equal to the dummy number
    
    Fitness_Minimise = numpy.hstack((Summed_Minimise_Vector_Top_Half,Summed_Minimise_Vector_Bottom_Half))
    Fitness_Minimise = [i for i in Fitness_Minimise if i != x]
    
    for i in range(0,(int((Population_Size/2)))): #append the strongest population into the global population
        Global_Population_Maximise.append(Fitness_Maximise [i])
        Global_Population_Minimise.append(Fitness_Minimise [i])
        
    del i
    del j
    del Summed_Maximise_Vector
    del Summed_Minimise_Vector
    del Summed_Maximise_Vector_Top_Half
    del Summed_Maximise_Vector_Bottom_Half
    del Summed_Minimise_Vector_Top_Half
    del Summed_Minimise_Vector_Bottom_Half
    del PreviousElementNumber
    del Real_Sequence_Maximise
    del Real_Sequence_Minimise
    del Fitness_Maximise,Fitness_Minimise
    
    No_Iter=z+1
    Per_Complete=(z/Generations)*100
    
    print("The number of iterations:",No_Iter)
    print("Script is: ", round(Per_Complete,3) ," % complete")

print("The Script is now 100 % Complete")
Data_Points=(int(len(Global_Population_Maximise)))+(int(len(Global_Population_Maximise)))
print("This simulation has ",Data_Points," data points")

del No_Iter,Per_Complete,Data_Points

#%% Checking if zeros are present in the array
n_zeros_maximise = numpy.count_nonzero(Global_Population_Maximise==0)
n_zeros_minimise = numpy.count_nonzero(Global_Population_Minimise==0)

if n_zeros_maximise > 0 or n_zeros_minimise > 0:
    print('\033[31m' "Warning Array Contains Zero" )
    
del n_zeros_maximise,n_zeros_minimise,Binary_Population_Maximise,Binary_Population_Minimise,Binary_Sequence_Maximise,Binary_Sequence_Minimise
del Crossover_rate,mutation_rate,Generations,x,z,Population_Maximise,Population_Minimise,Population_Size
