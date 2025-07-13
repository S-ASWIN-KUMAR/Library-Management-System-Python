import json
import datetime

def issue_book():
    member_id=int(input("Enter member ID: "))
    book_id=int(input("Enter book ID: "))

    f=open("storage/members.json","r")
    member_list=json.load(f)
    f.close()

    member_found=0
    for i in member_list:
        if i["id"]==member_id:
            member_found+=1
            break
    if member_found==0:
        print("Member doesn't exist!!")
        return print("Book can't be issued for an invalid member")
    else:
        print("Member exist!!")    

    f=open("storage/books.json","r")
    books_list=json.load(f)
    f.close()

    book_found=0
    book_issued=0
    for i in books_list:
        if i["id"]==book_id:
            book_found+=1
            if (i["quantity"]) > 0 and member_found != 0:
                i["quantity"]-=1 
                book_issued+=1    
            break
    if book_found==0:
        print("Book not found!!")
    elif book_issued==0:
        print("Book is out of stock!!!")
    else:
        
        f=open("storage/books.json","w")
        json.dump(books_list,f)
        f.close()
        print("Book issued successfully!!")


        f=open("storage/issued_books.json","r")
        issued_list=json.load(f)
        f.close()
        
        issue_date=datetime.date.today().strftime("%Y-%m-%d")
        new_issue={
            "member_id": member_id,
            "book_id"  :book_id,
            "issue_date":issue_date

        }

        issued_list.append(new_issue)


        f=open("storage/issued_books.json","w")
        json.dump(issued_list,f)
        f.close()



def return_book():
    member_id=int(input("Enter member ID: "))
    book_id=int(input("Enter book ID: "))

    f=open("storage/issued_books.json","r")
    return_list=json.load(f)
    f.close()

    found=0
    for i in return_list:
        if(i["member_id"]==member_id and i["book_id"]==book_id):
            found+=1

            issue_date = datetime.datetime.strptime(i["issue_date"], "%Y-%m-%d").date()
            return_date = datetime.date.today()
            total_days = (return_date - issue_date).days

            fine=0
            if(total_days>7):
                fine=(total_days-7)*2

            return_list.remove(i) # Remove the issued record
            
            f=open("storage/books.json","r")
            books_list=json.load(f)
            f.close()
            
            for j in books_list:
                if j["id"]==book_id:
                    j["quantity"]+=1
                    break
            


            f=open("storage/books.json","w")
            json.dump(books_list,f)
            f.close()    

            f = open("storage/issued_books.json", "w")
            json.dump(return_list, f)
            f.close()        
            
            print("Book returned successfully!")
            print(f"Issue Date  : {issue_date}")
            print(f"Return Date : {return_date}")
            print(f"Total Days  : {total_days}")
            print(f"Fine        : Rs.{fine}")
            break
    if found==0:
        print("No such book issued for this member")


def display_issued_books():
    f=open("storage/issued_books.json","r")
    issued_list=json.load(f)
    f.close() 

    f=open("storage/members.json","r")
    members=json.load(f)
    f.close() 

    f=open("storage/books.json","r")
    books=json.load(f)
    f.close() 

    if issued_list==[]:
        print("No books have been issued.")
        return
        

    for i in issued_list:
        member_name=""
        book_title=""

        for m in members:
            if(m["id"]==i["member_id"]):
                member_name= m["name"]
                break

        for b in books:
            if b["id"]==i["book_id"]:
                book_title=b["title"]
                break
        print(f"-------------------------\nMember Name:{member_name} \nBook Title:{book_title}\nIssue Date  : {i['issue_date']}\n")





def list_overdue_books():
    import datetime
    import json

    f = open("storage/issued_books.json", "r")
    issued_list = json.load(f)
    f.close()

    if not issued_list:
        print("No issued books found.")
        return

    f = open("storage/members.json", "r")
    members = json.load(f)
    f.close()

    f = open("storage/books.json", "r")
    books = json.load(f)
    f.close()

    today = datetime.date.today()

    for record in issued_list:
        issue_date = datetime.datetime.strptime(record["issue_date"], "%Y-%m-%d").date()
        days_diff = (today - issue_date).days

        if days_diff > 7:
        
            member_name = ""
            for m in members:
                if m["id"] == record["member_id"]:
                    member_name = m["name"]
                    break

            
            book_title = ""
            for b in books:
                if b["id"] == record["book_id"]:
                    book_title = b["title"]
                    break

            print("Overdue Book")
            print(f"Member Name : {member_name}")
            print(f"Book Title  : {book_title}")
            print(f"Issue Date  : {issue_date}")
            print(f"Days Overdue: {days_diff - 7}")
            print("-----------")


def view_fine_summary_per_member():
    f = open("storage/issued_books.json", "r")
    issued_list = json.load(f)
    f.close()

    f = open("storage/members.json", "r")
    members = json.load(f)
    f.close()

    today = datetime.date.today()
    fine_summary = {}

    for record in issued_list:
        issue_date = datetime.datetime.strptime(record["issue_date"], "%Y-%m-%d").date()
        days_late = (today - issue_date).days - 7

        if days_late > 0:
            fine = days_late * 2
            member_id = record["member_id"]
            if member_id in fine_summary:
                fine_summary[member_id] += fine
            else:
                fine_summary[member_id] = fine

    if fine_summary == {}:
        print("No fines for any members.")
        return

    for member_id, total_fine in fine_summary.items():
        member_name = ""
        for m in members:
            if m["id"] == member_id:
                member_name = m["name"]
                break
        print(f" {member_name} (ID: {member_id}) --> Total Fine: ₹{total_fine}")


