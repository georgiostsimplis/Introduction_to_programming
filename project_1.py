"""
Authors: Georgios Tsimplis                 s200166
         Viktor Karl Wilhelm Törnblom      s200116
         Varun Channabasappagowda Biradar  s200235
         
GROUP MEMBERS CONTRIBUTED EQUALLY

"""



import numpy as np
import matplotlib.pyplot as plt

# FUNCTIONS    
############################
def dataLoad(filename):
    
    #Load filename
    data_old = np.loadtxt(filename) 
    Bacteria=[1,2,3,4]
    
    #Indexing valid data
    index=np.ones(len(data_old),dtype=bool)
    
    #Check data's validity
    for i in range(len(data_old)):
        if data_old[i,0]<10 or data_old[i,0]>60:
            index[i]=0
            print('In {} row the Temparature of the initial data is out of range[10,60]'.format(i+1))
        elif data_old[i,1]<0:
            index[i]=0
            print('In {} row the Growth rate of the initial data is non-positive'.format(i+1))
        elif data_old[i,2] not in Bacteria:
            index[i]=0
            print('In {} row Bacteria type is invalid'.format(i+1))
    data=data_old[index]
    return data

def dataStatistics(data):    
    while True:
        statistic = input("Select one of the following statistics: \n\n 1. Mean Temperature\n 2. Mean Growth Rate\n 3. Std Temperature\n 4. Std Growth rate\n 5. Rows\n 6. Mean Cold Growth rate\n 7. Mean Hot Growth rate\n 8. Back to main menu \n \n Your choice is:\t")
        
        #Cases according to the specific Statistic
        if statistic=='1':
            print("The Mean Temperature of the given data is :\t", np.mean(data[:,0]))
        elif statistic=='2':
            print("The Mean Growth Rate of the given data is :\t",np.mean(data[:,1]))
        elif statistic=='3':
            print("The Standard deviation of the Temperature is :\t",np.std(data[:,0]))
        elif statistic=='4':
            print("The Standard deviation of the Growth rate is :\t",np.std(data[:,1]))
        elif statistic=='5':
            print("The total number of rows is :\t",len(data))
        elif statistic =='6':
            index1=data[:,0]<20
            print("The Mean Growth rate when Temperature is less than 20 degrees is:\t",np.mean(data[index1,1]))
        elif statistic == '7':
            index2=data[:,0]>50
            print("The Mean Growth rate when Temperature is greater than 50 degrees is:\t",np.mean(data[index2,1]))
        elif statistic == '8':
            break
        else:
            print("Invalid input")
        print('\n=============================================================\n')


def dataPlot(data):
    
     #plot1
     # get the column with the bacteria type
     Bacteria_type=data[:,2]
     
     # count each type of bacteria
     Salmonela=np.count_nonzero(Bacteria_type==1)
     Bacillus=np.count_nonzero(Bacteria_type==2)
     Listeria=np.count_nonzero(Bacteria_type==3)
     Brochothrix=np.count_nonzero(Bacteria_type==4)
     
     #Plotting and adjusting the 1st plot(labels,titles...)
     names=['Salmonela','Bacillus','Listeria','Brochothrix']
     values1=[Salmonela,Bacillus,Listeria,Brochothrix]
     plt.bar(names,values1,color='red')
     plt.xlabel('Bacteria types')
     plt.ylabel('Units')
     plt.title("Units per Bacteria type")
     plt.show()
     #plot 2
   
     #get the rows of each bacteria type
     positions=[np.where(data[:,2]==1),np.where(data[:,2]==2),np.where(data[:,2]==3),np.where(data[:,2]==4)]
     
     # create a dictionary for each type
     keys1=data[positions[0],0]
     values1=data[positions[0],1]
     keys2=data[positions[1],0]
     values2=data[positions[1],1]
     keys3=data[positions[2],0]
     values3=data[positions[2],1]
     keys4=data[positions[3],0]
     values4=data[positions[3],1]
     
     #Plot each type to a linechart with condition to exist at least 2 data points fof each bacteria type
     if len(keys1[0])>=2:
         dict1=dict(zip(keys1.squeeze(),values1.squeeze()))
         plt.plot(*zip(*sorted(dict1.items())),label='Salmonela')
     if len(keys2[0])>=2:
         dict2=dict(zip(keys2.squeeze(),values2.squeeze()))
         plt.plot(*zip(*sorted(dict2.items())),label='Bacillus')
     if len(keys3[0])>=2:
         dict3=dict(zip(keys3.squeeze(),values3.squeeze()))
         plt.plot(*zip(*sorted(dict3.items())),label='Listeria')
     if len(keys4[0])>=2:
         dict4=dict(zip(keys4.squeeze(),values4.squeeze()))
         plt.plot(*zip(*sorted(dict4.items())),label='Brochothrix')
    
    #Titles - Labels - Legend outside the box to not takes up space
     plt.title('Dependency of Temperature with Growth Rate')
     plt.gca().legend(loc='lower left', bbox_to_anchor=(1, 0.7))
     plt.xlabel('Temperature')
     plt.ylabel('Growth Rate')
     plt.tight_layout()
     plt.show()


def filter(data):
    while True:
        filt =input("\nHow would you like to filter your data?\n 1. Exclude bacterial species. \n 2. Growth Rate\n 3. Go back\n")
        
        #Switch cases to filter in accordance to bacteria type
        if filt == '1':
            while True:
                selection = input("\nWhat species whould you like to exclude?\n 1. Salmonella enterica\n 2. Bacillus cerus\n 3. Listeria\n 4. Brochothrix thermosphacta\n 5. Go back\n")
                if selection == '1':
                    index = (data[:,2] != 1)
                    data = data[index]
                    print(data)
                elif selection == '2':
                    index = (data[:,2] != 2)
                    data = data[index]
                    print(data)
                elif selection == '3':
                    index = (data[:,2] != 3)
                    data = data[index]
                    print(data)
                elif selection == '4':
                    index = (data[:,2] != 4)
                    data = data[index]
                    print(data)
                elif selection == '5':
                    break
                else:
                    print("Invalid input")
        
        #Switch cases to filter in accordance to Growth
        elif filt == '2':
            selection = float(input("Lower limit:\n"))
            index = (data[:,1] > selection)
            data = data[index]
            print(data)
            selection = float(input("Upper limit:\n"))
            index = (data[:,1] < selection)
            data = data[index]
            print(data)
        #Exit from loop    
        elif filt == '3':
            break
        else:
            print("Invalid input")
    return data


#            Main script
#####################################
while True:
    
    print("\n \t \t \t BACTERIA ANALYSIS SOFTWARE\n")
    print('=============================================================\n')
    choice = input("Please choose one of the following options: \n 1. Load data.\n 2. Filter data.\n 3. Display statistics. \n 4. Generate plots. \n 5. Quit.\n \n Your choice is :\t")
    
    #Load data
    if choice == "1": 
        print('=============================================================\n')
        #Enter a valid filename or escape
        while True:
            try:
                X=input('Please write the filename or press 1 to Escape:\t ')
                if X=='1':
                    break
                else:
                    data = dataLoad(X)
                    print('\n Your data have been loaded successfully!!!')
                    break
        #Handle ERROR when the name is invalid to not stop the program
            except OSError:
                print('\n WARNING !!! \n *This filename does not exist in the same directory with the program!* \n Try again...')
        
    #Filter data    
    elif choice == "2":
        print('=============================================================\n')
        data = filter(data)
        
    #Statistics
    elif choice == "3":
        print('=============================================================\n')
        dataStatistics(data)
        
    #Generating plots     
    elif choice == "4":
        print('=============================================================\n')
        print("Generating plots.....")
        dataPlot(data)
        
    #Quit 
    elif choice == "5":
        print("\nBye bye!!!!\n")
        #Goodbye graphic :)
        for i in range((-3),5):
            x=4-abs(i)
            print("  "*(4-x)+"*"*x+x*"  "+x*"*")
        break
    
    else:
        print("\nInvalid input. Has to be a number between 1 and 5.")
