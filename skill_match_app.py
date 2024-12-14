import os
import time
import skillmatchDB
from all_profiles import profiles  # Assuming this file has the profiles dictionary

class SkillMatchApp:
    def __init__(self):
        self.logged_in_user = None  # To store the logged-in user
        skillmatchDB.create_tables()  # Ensure tables exist when the app starts

    def clear_screen(self):
        """Clears the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def start(self):
        """Starts the app and shows the login/register or main menu based on login state."""
        while True:
            if not self.logged_in_user:  # If no user is logged in, show login/register
                self.show_login_or_register()
            else:  # Otherwise, show the main menu
                self.main_menu()

    def show_login_or_register(self):
        """Displays the login or registration menu."""
        self.clear_screen()
        print("\n--- Welcome to Skill Match ---")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            self.login_user()
        elif choice == "2":
            self.register_user()
        elif choice == "3":
            print("Goodbye!")
            exit()  # Exit the program
        else:
            print("Invalid choice. Please try again.")

    def register_user(self):
        """Registers a new user."""
        self.clear_screen()
        print("\n--- Register ---")
        first_name = input("Enter first name: ").strip()
        last_name = input("Enter last name: ").strip()
        specialty = input("Enter specialty (Music, Arts, Coding): ").strip()
        skill = input("Enter skills (e.g., Guitar, Piano): ").strip()
        skill_level = input("Enter your skill level (Newbie, Intermediate, Professional): ").strip()
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        success = skillmatchDB.register_user(first_name, last_name, specialty, skill, skill_level, username, password)
        if success:
            print("Registration successful! You can now log in.")
        else:
            print("Registration failed. Username may already exist.")

    def login_user(self):
        """Logs in the user."""
        self.clear_screen()
        print("\n--- Login ---")
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        user = skillmatchDB.authenticate_user(username, password)

        if user:
            self.logged_in_user = user
            print(f"Welcome, {username}! Your current credits: {self.logged_in_user['credits']}")
        else:
            print("Invalid username or password. Please try again.")

    def main_menu(self):
        """Displays the main menu after logging in."""
        self.clear_screen()

        if self.logged_in_user is None:  # If no user is logged in, prompt login
            print("No user is currently logged in. Please log in.")
            self.login_user()
            return  # Prevent further execution of main_menu

        # Show main menu options to the logged-in user
        print(f"\nWelcome back, {self.logged_in_user['username']}! - Credits: {self.logged_in_user['credits']}")
        print("1. Trade Skills")
        print("2. Learn a Skill")
        print("3. Top Up Credits")
        print("4. View All Registered Users")
        print("5. Logout")
        print("6. Delete Account")
        print("7. Delete all users")
        print("8. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            self.trade_skills()
        elif choice == "2":
            self.learn_skill()
        elif choice == "3":
            self.top_up_credits()
        elif choice == "4":
            self.show_all_users()
        elif choice == "5":
            self.logout_user()
        elif choice == "6":
            self.delete_account()
        elif choice == "7":
            self.delete_all_users()
        elif choice == "8":
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")
        self.main_menu()  # Recursively call the main menu in case of invalid input

    def trade_skills(self):
        """Allows the user to trade skills with others."""
        self.clear_screen()
        print("\n--- Trade Skills ---")
        print("Available tags: Music, Arts, Coding")
        skill_tag = input("Choose a skill tag (or type 'back' to return to the main menu): ").strip()
        if skill_tag.lower() == 'back':
            return
        matching_profiles = self.get_matching_profiles(skill_tag)
        if not matching_profiles:
            print("No matching profiles found. Try a different skill tag.")
        else:
            for profile in matching_profiles:
                if profile['id'] == self.logged_in_user['id']:  # Skip the logged-in user
                    continue

                self.clear_screen()  # Clear the screen before showing the next profile
                print(f"{profile['first_name']} ({profile['specialty']}, {profile['skills']})")
                match = input("Do you want to match with this profile? (Y/N) (x for exit): ").strip().lower()
                if match == "y":
                    print(f"Matched with {profile['first_name']} for skill trade! Press any key to continue.")
                    continue
                elif match == "n":
                    continue
                elif match == "x":
                    break
                else:
                    print("Invalid input. Press any key to move to the next profile.")
                    continue
                time.sleep(1)  # Optional: to slow down the loop if you want a brief pause between profiles

    def learn_skill(self):
        """Allows the user to learn a skill from other professionals."""
        self.clear_screen()  # Clear the screen once when the method is called
        print("\n--- Learn a Skill ---")
        print("Available tags: Music, Arts, Coding, Math")
        skill_tag = input("Choose a skill tag (or type 'back' to return to the main menu): ").strip()
        if skill_tag.lower() == 'back':
            return
        professional_profiles = self.get_matching_profiles(skill_tag)
        if not professional_profiles:
            print("No professional profiles available.")
        else:
            for profile in professional_profiles:
                if profile['id'] == self.logged_in_user['id']:  # Skip the logged-in user
                    continue

                self.clear_screen()  # Clear the screen before displaying each profile
                print(f"{profile['first_name']} ({profile['specialty']}, {profile['skills']}) - Rate: 50/session")
                match = input("Do you want to learn from this profile? (Y/N): ").strip().lower()
                if match == "y":
                    print(f"Matched with {profile['first_name']} for learning!")
                    input("Press any key to continue...")  # Pauses until user presses a key
                    self.logged_in_user['credits'] -= 50
                    continue
                elif match == "n":
                    continue
                elif match == "x":
                    break
                else:
                    print("Invalid input. Press any key to move to the next profile.")
                    continue
        time.sleep(1)

    def top_up_credits(self):
        """Allows the user to top up their credits."""
        self.clear_screen()
        print("\n--- Top Up Credits ---")
        print("Send payment through Gcash number: 09667021996.")
        input("Enter the number you used to send.")
        options = {
            "1": (1000, 799),
            "2": (499, 449),
            "3": (200, 189),
            "4": (100, 99),
        }
        print("\n".join([f"{k}. {v[0]} credits for {v[1]} Pesos" for k, v in options.items()]))
        choice = input("Choose an option (or type 'back' to return): ").strip()
        if choice.lower() == "back":
            return
        if choice in options:
            credits, _ = options[choice]
            self.logged_in_user['credits'] += credits
            print(f"Successfully added {credits} credits. New balance: {self.logged_in_user['credits']}.")

            # Update the new credits value in the database
            skillmatchDB.update_credits(self.logged_in_user['id'], self.logged_in_user['credits'])

            updated_user = skillmatchDB.authenticate_user(self.logged_in_user['username'], self.logged_in_user['password'])
            if updated_user:
                skillmatchDB.update_credits(self.logged_in_user['id'], self.logged_in_user['credits'])
            else:
                print("Error fetching updated user data.")
        else:
            print("Invalid choice. Please try again.")

    def show_all_users(self):
        """Displays all registered users."""
        self.clear_screen()
        print("\n--- All Registered Users ---")
        all_users = skillmatchDB.get_all_users()
        if not all_users:
            print("No users found.")
            return
        # Print table headers
        print(f"{'ID':<5} {'First Name':<15} {'Last Name':<15} {'Specialty':<15} {'Skills':<15} {'Username':<15} {'Skill Level':<18}")
        print("=" * 115)  # Separator for better readability
        # Print each user in a row
        for user in all_users:
            print(f"{user[0]:<5} {user[1]:<15} {user[2]:<15} {user[3]:<15} {user[4]:<15} {user[5]:<15} {user[7]:<18}")
        print(input("=" * 115))  # End separator

    def logout_user(self):
        """Logs out the current user."""
        log_out = input("Are you sure you want to logout? (Y/N): ").strip().lower()
        if log_out == "y":
            print(f"\nGoodbye, {self.logged_in_user['username']}!")
            self.logged_in_user = None
            self.start()  # Restart the app after logout
        elif log_out == "n":
            print("Logout canceled. Returning to the main menu.")
        else:
            print("Invalid input. Returning to the main menu.")

    def delete_account(self):
        """Deletes the logged-in user's account."""
        self.clear_screen()
        confirm = input("Are you sure you want to delete your account? (Y/N): ").strip().lower()
        if confirm == "y":
            user_id = self.logged_in_user['id']
            skillmatchDB.delete_user(user_id)
            self.logged_in_user = None
            print("Your account has been deleted successfully.")
        else:
            print("Account deletion canceled.")

    def delete_all_users(self):
        """Deletes all users in the system (irreversible)."""
        self.clear_screen()
        confirm = input("Are you sure you want to delete all users? This action cannot be undone. (Y/N): ").strip().lower()
        if confirm == "y":
            skillmatchDB.delete_all_users()
            print("All users have been deleted from the database.")
        else:
            print("Action canceled.")

    def get_matching_profiles(self, skill_tag):
        """Fetches profiles matching the given skill tag."""
        skill_tag = skill_tag.capitalize()
        return skillmatchDB.get_profiles_by_skill_tag(skill_tag)

if __name__ == "__main__":
    app = SkillMatchApp()
    app.start()
