import json

def add_book():
    try:
        file=[]

        id=int(input("Enter Book ID: "))
        title=(input("Enter Title: "))
        author=(input("Enter Author: "))
        category=(input("Enter Category: "))
        quantity=int(input("Enter Quantity: "))

        f = open("storage/books.json","r")
        file = json.load(f)
        f.close()
        
        found=0
        for i in file:
            if i["id"]==id:
                print("Book already exists!!")
                found+=1
                break
        if(found==0):       
            new_book={
                    "id":id,
                    "title":title,
                    "author":author,
                    "category":category,
                    "quantity":quantity
                    }
            file.append(new_book)

            f = open("storage/books.json","w")
            json.dump(file,f)
            f.close()
            
            print("Book added successfully!!")
        

    except Exception:
        print("Something wrong")

def display_books():
    f = open("storage/books.json","r")
    books_list=json.load(f)
    for i in books_list:
        print(f'ID : {i["id"]} \n Title    : {i["title"]} \n Author   : {i["author"]} \n Category : {i["category"]}\n Quantity : {i["quantity"]}\n')
    f.close()

def search_book():
    f = open("storage/books.json","r")
    search_list=json.load(f)

    choice = int(input("Enter 1 to search by title or 2 to search by author: "))
    found=0
    if choice==1:
        title=input("Enter book title: ")
        for i in search_list:
            if i["title"].lower()==title.lower():
                print(f"Book available!! with quantity {i["quantity"]}")
                found+=1
                break
        if found == 0:
            print("Book not found!!")

    elif choice==2:  
        author=input("Enter author name: ")
        for i in search_list:
            if i["author"].lower()==author.lower():
                print(f"Book available!! with quantity {i["quantity"]}")
                found+=1
                break
        if found == 0:
            print("Book not found!!")
    elif(choice not in [1,2]):
        print("Enter number either 1 or 2")
        return search_book()

    f.close()
    
def update_book():
    f = open("storage/books.json","r")
    update_list=json.load(f)

    id=int(input("Enter book ID to update: "))
    found=0

    for i in update_list:
        if(i["id"])==id:
            found+=1

            while True:
                update=input("what do you want to update? \n Enter your choice between 1 to 5:\n1 for title\n2 for author\n3 for category\n4 for quantity\n5 to exit\n")

                if update=="1":
                    new_title=input("Enter new title to be updated : ")
                    i["title"]=new_title
                    continue
                    
                    
        
                elif update=="2":
                    new_title=input("Enter new author name to be updated : ")
                    i["author"]=new_title
                    continue

                
                elif update=="3":
                    new_title=input("Enter new category to be updated : ")
                    i["category"]=new_title
                    continue
                
                elif update=="4":
                    new_title=int(input("Enter new quantity to be updated : "))
                    i["quantity"]=new_title
                    continue

                else:
                    break
            break
    if found==0:
        print("Book not found!")
            
    
    f.close()

    f=open("storage/books.json","w")
    json.dump(update_list,f)
    f.close()
            

def delete_book():

    f=open("storage/books.json","r")
    delete_list=json.load(f)

    id=int(input("Enter book ID to delete: "))
    found=0
    for i in delete_list:
        if i["id"]==id:
            found+=1
            delete_list.remove(i)
            print("Book deleted successfully!!")
            break
    

    if found==0:
        print("Book not found!")
    
    f.close()

    f=open("storage/books.json","w")
    json.dump(delete_list,f)
    f.close()






if __name__ == "__main__":
    pass
