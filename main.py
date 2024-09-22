from db import initialize_db
from scheduler import (
    schedule_match,
    view_assignments,
    update_existing_match,
    add_team,
    add_field,
    add_referee
)

def main():
    initialize_db()
    
    while True:
        print("\nSports Management System")
        print("1. Add Team")
        print("2. Add Field")
        print("3. Add Referee")
        print("4. Schedule Match")
        print("5. View Assignments")
        print("6. Update Existing Match")
        print("7. Exit")       
        choice = input("Enter choice: ")

        if choice == "1":
            schedule_match()
        elif choice == "2":
            view_assignments()
        elif choice == "3":
            update_existing_match()
        elif choice == "4":
            add_team()
        elif choice == "5":
            add_field()
        elif choice == "6":
            add_referee()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
