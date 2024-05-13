class Book:

    NoofBooks = 0

    def __init__(self , Name , Author):

        self.Name = Name
        self.Author = Author
        Book.NoofBooks += 1

    def Display(self):

        print("Book : " , self.Name)
        print("Author : " , self.Author)
        print("No of Books : " , Book.NoofBooks)


def main():

    str1 = input("Enter the Book name : ")
    str2 = input("Enter the Author name : ")

    obj1 = Book(str1 , str2)

    obj1.Display()

    str1 = input("Enter the Book name : ")
    str2 = input("Enter the Author name : ")

    obj2 = Book(str1 , str2)

    obj2.Display()

if __name__ == "__main__":
    main()