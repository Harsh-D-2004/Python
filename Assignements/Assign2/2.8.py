def Display():

    for i in range(6 , 0 , -1):
        for j in range(1 , 6):

            if(i <= j):
                print(j , end=" ")

        print()

def main():

    Display()

if __name__ == "__main__":

    main()