from library import (
    add_book, display_books, search_book, update_book, delete_book
)
from member import (
    add_member, display_member, search_member, update_member, delete_member
)
from transactions import (
    issue_book, return_book, display_issued_books, list_overdue_books, view_fine_summary_per_member
)

while True:
    print("\n📚 LIBRARY MANAGEMENT SYSTEM 📚")
    print("1.  Add Book")
    print("2.  Display All Books")
    print("3.  Search Book")
    print("4.  Update Book")
    print("5.  Delete Book")
    print("6.  Add Member")
    print("7.  Display All Members")
    print("8.  Search Member")
    print("9.  Update Member")
    print("10. Delete Member")
    print("11. Issue Book")
    print("12. Return Book")
    print("13. Display Issued Books")
    print("14. List Overdue Books")
    print("15. View Fine Summary")
    print("16. Exit")

    choice = input("Enter your choice (1-16): ")

    if choice == '1':
        add_book()
    elif choice == '2':
        display_books()
    elif choice == '3':
        search_book()
    elif choice == '4':
        update_book()
    elif choice == '5':
        delete_book()
    elif choice == '6':
        add_member()
    elif choice == '7':
        display_member()
    elif choice == '8':
        search_member()
    elif choice == '9':
        update_member()
    elif choice == '10':
        delete_member()
    elif choice == '11':
        issue_book()
    elif choice == '12':
        return_book()
    elif choice == '13':
        display_issued_books()
    elif choice == '14':
        list_overdue_books()
    elif choice == '15':
        view_fine_summary_per_member()
    elif choice == '16':
        print("Exiting...Byeeeeee👋")
        break
    else:
        print("Invalid choice! Please try again.")

    input("\nPress Enter to continue...")
