def Display():

    for i in range(1 , 6):
        for j in range(1 , 6):
            
            if( i+j <= 6):
                print("*" , end=" ")

        print()

def main():

    Display()

if __name__ == "__main__":

    main()