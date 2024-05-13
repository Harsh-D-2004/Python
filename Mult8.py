import multiprocessing

def main():

    print("No of cores : " , multiprocessing.cpu_count())

if __name__ == "__main__":
    main()
