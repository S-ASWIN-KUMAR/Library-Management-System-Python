import json

def add_member():
    member_list=[]
    f = open("storage/members.json","r")
    member_list=json.load(f)
    f.close()

    id=int(input("Enter the new member ID  : "))
    name=(input("Enter the new member Name  : "))
    email=(input("Enter the new member Email  : "))
    phone=int(input("Enter the new member Phone  : "))


    found=0
    for i in member_list:
        if i["id"]==id and i["name"]==name:
            print("Member already exists!!")
            found+=1
            break
    if(found==0):    
        new_member={
            "id":id,
            "name":name,
            "email":email,
            "phone":phone
        }
        member_list.append(new_member)

        f = open("storage/members.json","w")
        json.dump(member_list,f)
        f.close()
        
        print("Member added successfully!!")
        
def display_member():
    f=open("storage/members.json","r")
    display_list=json.load(f)
    f.close()

    for i in display_list:
        print(f"ID:{i["id"]}\n Name  : {i["name"]}\n Email : {i["email"]}\n Phone : {i["phone"]}")


def search_member():
    f = open("storage/members.json","r")
    search_list=json.load(f)
    f.close()

    search=input("Enter 1 to search by Id \nEnter 2 to search by Name\nEnter 3 to exit :\n ")
    if search=='1':
        id=int(input("Enter ID to search: "))
        found=0
        for i in search_list:
            if i["id"]==id:
                print("Member found!!")
                found+=1
                print(f"ID:{i["id"]}\n Name  : {i["name"]}\n Email : {i["email"]}\n Phone : {i["phone"]}")
        if (found==0):
            print("Member not found!!")

    elif search=='2':
        name=(input("Enter Name to search: "))
        found=0
        for i in search_list:
            if i["name"].lower()==name.lower():
                print("Member found!!")
                found+=1
                print(f"ID:{i["id"]}\n Name  : {i["name"]}\n Email : {i["email"]}\n Phone : {i["phone"]}")   
        
        if (found==0):
            print("Member not found!!")
    
    elif search=='3':
        print("Exitted!!")
    
    else:
        print("Enter either 1 or 2 or 3")
        return search_member()

def update_member():
    f=open("storage/members.json","r")
    update_list=json.load(f)
    f.close()

    id=int(input("Enter ID of the member to update details: "))

    found=0
    for i in update_list:
        if i["id"]==id:
            found+=1

            while True:
                n=int(input("Details you want to update:\n1.ID\n2.Name\n3.Email\n4.Phone\n5.Exit\nEnter your choice between 1 to 5 : "))
                if n==1:
                    id=int(input("Enter new ID: "))

                    duplicate=0
                    for m in update_list: 
                        if m["id"]==id and m != i: 
                            duplicate+=1
                            break
                    
                    if(duplicate==0):
                        i["id"]=id
                        continue
                    else:
                        print("ID already exists! Try different one!")
                elif n==2:
                    name=(input("Enter new Name: "))
                    i["name"]=name
                    continue                
                elif n==3:
                    email=(input("Enter new Email: "))
                    i["email"]=email
                    continue
                elif n==4:
                    ph=int(input("Enter new Phone No : "))
                    i["phone"]=ph
                    continue
                else:
                    break
        break
    
    if(found==0):
        print("Member ID not found!!")
    else:
        f=open("storage/members.json","w")
        json.dump(update_list,f)
        f.close()


def delete_member():
    f=open("storage/members.json","r")
    delete_list=json.load(f)
    f.close()

    id=int(input("Enter ID to delete the member data : "))

    found=0
    for i in delete_list:
        if i["id"]==id:
            delete_list.remove(i)
            found+=1
    if(found==0):
        print("Member not found!!")
    else:
        f=open("storage/members.json","w")
        json.dump(delete_list,f)
        print("Member deleted successfully!!")
        f.close()