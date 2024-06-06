import psutil


def DisplayProcessInfo():

    for proc in psutil.process_iter(['pid' , 'name' , 'username']):
        print(proc)

def main():

    DisplayProcessInfo()

if __name__ == "__main__":
    main()