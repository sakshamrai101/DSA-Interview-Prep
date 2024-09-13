# What exactly does the system does do ?
# Members can borrow books and return books, 
# system should track availibilty, member accounts, book reservations and overdue books. 

# Questions to ask ?
# 1. Borrowing Limits? are there any limits on how many books a member can borrow at a time ?
# 2. Reservation Handling? Should the system allow users to reserve books that are currently checked out. 
# 3. How should the system handle late fees and overdue books ?
# 4. Should to book support searching by name, author or both ?
# 5. Multiple branches? Does the library have multiple locations ? Or does it have a single branch ?
# 6. How should payment and late fees be handled ?

# Assumptions made:
# 1. Members can borrow up to 5 books at a time. 
# 2. Each book can be reserved even if it is checked out.
# 3. Late Fees are calculated per day for overdue books. 
# 4. Book can be searched by title and author.
# 5. The system support one branch.

# Higher Level Class Overiview:
# 1. Library Class: Manages all the books, members and reservations. 
# 2. Book Class: represents the book title, author, ISBN, availibility status and borrowed date. 
# 3. Reservation: Handles book reservations, ensuring that members can reserve books and get notified when available. 
# 4. Librarian: Manages book checkouts, returns, and overdue penalties. 
# 5. Notification Class: send notifications to members about due dates and availibility of reserved books.
# 6. Member Class: represents a lib member with account details, borrowed books and late fees. 

from datetime import datetime, timedelta

class Book:
    def __init__(self, book_title, author, bar_code_no):
        self.book_title = book_title
        self.author = author 
        self.bar_code_no = bar_code_no
        self.available = True
        self.borrowed_date = None 

    
    def borrow(self):
        self.available = False 
        self.borrowed_date = datetime.now()

    def return_book(self):
        self.available = True
        self.borrowed_date = None 


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
        self.late_fees = 0

    
    def borrow_book(self, book):
        if len(self.borrowed_books) >= 5:
            print (f"{self.name} has reached borrowing limit.")
            return 
        book.borrow()
        self.borrowed_books.append(book)

    def return_book(self, book):
        book.return_book()
        self.borrowed_books.remove(book)
        self.calculate_late_fees(book)

    def calculate_late_fees(self, book):
        if book.borrowed_date:
            days_borrowed = (datetime.now() - book.borrowed_date).days
            if days_borrowed > 14: 
                self.late_fees += (days_borrowed - 14) * 0.5 # base fee for per day late. 

class Reservation:
    def __init__(self, book, member):
        self.book = book
        self.member = member
        self.created_at = datetime.now()

class Librarian:
    def __init__(self):
        self.reservations = []


    def checkout_book(self, book, member):
        if book.available:
            member.borrow_book(book)
        else:
            print(f"{book.book_title} is currently not availble. Adding a reservation.")
            self.reservations.append(Reservation(book, member))

    
    def return_book(self, book, member):
        member.return_book()
        for reservation in self.reservations:
            if reservation.book == book:
                print(f"{reservations.member.name}, your reserved book ")
                self.reservations.remove(book)
                break

    def charge_late_fees(self, memeber):
        print()



class Library:
    def __init__(self):
        self.books = []
        self.members = []


    def add_book(self, book):
        self.books.append(book)
    

    def register_member(self, member):
        self.members.append(member)

    def search_books_by_title(self, title):
        return [book for book in self.books if book.title == title]
    

    def search_books_by_author(self, author):
        for books in self.books:
            if book.author == author:
                return book





