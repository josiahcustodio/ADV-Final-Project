import tkinter as tk
from tkinter import messagebox
import skillmatchDB  # Assuming your DB functions are in this module
from skill_match_app import SkillMatchApp  # Assuming you have a backend module

class SkillMatchGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Skill Match App")
        self.root.geometry("800x600")
        
        self.app = SkillMatchApp()  # Instantiate the backend logic
        self.logged_in_user = None
        
        self.create_login_widgets()  # Start with the login page
        
    def create_login_widgets(self):
        # Clear all widgets first
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.title_label = tk.Label(self.root, text="Welcome to Skill Match", font=("Arial", 24))
        self.title_label.pack(pady=20)

        self.username_label = tk.Label(self.root, text="Username:")
        self.username_label.pack(pady=5)
        
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)
        
        self.password_label = tk.Label(self.root, text="Password:")
        self.password_label.pack(pady=5)
        
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)
        
        self.login_button = tk.Button(self.root, text="Login", command=self.login_user)
        self.login_button.pack(pady=10)

        self.register_button = tk.Button(self.root, text="Register", command=self.show_register_window)
        self.register_button.pack(pady=5)

    def login_user(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        
        user = skillmatchDB.authenticate_user(username, password)
        
        if user:
            self.logged_in_user = user
            messagebox.showinfo("Login Successful", f"Welcome, {username}!")
            self.show_menu()  # Go to the menu screen
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")
    
    def show_menu(self):
        # Clear all widgets first
        for widget in self.root.winfo_children():
            widget.destroy()

        # Menu page (shown after login)
        self.title_label = tk.Label(self.root, text="Skill Match Menu", font=("Arial", 24))
        self.title_label.pack(pady=20)

        self.trade_skills_button = tk.Button(self.root, text="Trade Skills", command=self.trade_skills)
        self.trade_skills_button.pack(pady=5)

        self.learn_skill_button = tk.Button(self.root, text="Learn a Skill", command=self.learn_skill)
        self.learn_skill_button.pack(pady=5)

        self.top_up_button = tk.Button(self.root, text="Top Up Credits", command=self.show_top_up_window)
        self.top_up_button.pack(pady=5)

        self.view_users_button = tk.Button(self.root, text="View All Registered Users", command=self.show_all_users)
        self.view_users_button.pack(pady=5)

        self.view_transaction_history_button = tk.Button(self.root, text="View Transaction History", command=self.view_transaction_history)
        self.view_transaction_history_button.pack(pady=5)

        self.logout_button = tk.Button(self.root, text="Logout", command=self.logout_user)
        self.logout_button.pack(pady=5)

        self.delete_account_button = tk.Button(self.root, text="Delete Account", command=self.delete_account)
        self.delete_account_button.pack(pady=5)

        self.delete_all_users_button = tk.Button(self.root, text="Delete All Users", command=self.delete_all_users)
        self.delete_all_users_button.pack(pady=5)

        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.exit_button.pack(pady=5)

    def learn_skill(self):
        # Add functionality for learning skills here
        messagebox.showinfo("Learn a Skill", "Feature coming soon!")

    def show_register_window(self):
        register_window = tk.Toplevel(self.root)
        register_window.title("Register")
        register_window.geometry("400x500")
        
        first_name_label = tk.Label(register_window, text="First Name:")
        first_name_label.pack(pady=5)
        
        self.first_name_entry = tk.Entry(register_window)
        self.first_name_entry.pack(pady=5)
        
        last_name_label = tk.Label(register_window, text="Last Name:")
        last_name_label.pack(pady=5)
        
        self.last_name_entry = tk.Entry(register_window)
        self.last_name_entry.pack(pady=5)
        
        specialty_label = tk.Label(register_window, text="Specialty:")
        specialty_label.pack(pady=5)
        
        self.specialty_entry = tk.Entry(register_window)
        self.specialty_entry.pack(pady=5)
        
        skills_label = tk.Label(register_window, text="Skills (comma-separated):")
        skills_label.pack(pady=5)
        
        self.skills_entry = tk.Entry(register_window)
        self.skills_entry.pack(pady=5)
        
        skill_level_label = tk.Label(register_window, text="Skill Level (1: Newbie, 2: Intermediate, 3: Professional):")
        skill_level_label.pack(pady=5)
        
        self.skill_level_entry = tk.Entry(register_window)
        self.skill_level_entry.pack(pady=5)
        
        username_label = tk.Label(register_window, text="Username:")
        username_label.pack(pady=5)
        
        self.reg_username_entry = tk.Entry(register_window)
        self.reg_username_entry.pack(pady=5)
        
        password_label = tk.Label(register_window, text="Password:")
        password_label.pack(pady=5)
        
        self.reg_password_entry = tk.Entry(register_window, show="*")
        self.reg_password_entry.pack(pady=5)
        
        register_button = tk.Button(register_window, text="Register", command=lambda: self.register_user(register_window))
        register_button.pack(pady=10)
        
    def register_user(self, register_window):
        first_name = self.first_name_entry.get().strip()
        last_name = self.last_name_entry.get().strip()
        specialty = self.specialty_entry.get().strip()
        skills = self.skills_entry.get().strip()
        skill_level = self.skill_level_entry.get().strip()
        username = self.reg_username_entry.get().strip()
        password = self.reg_password_entry.get().strip()
        
        success = skillmatchDB.register_user(first_name, last_name, specialty, skills, skill_level, username, password)
        
        if success:
            messagebox.showinfo("Registration Successful", f"Welcome, {username}! You can now login.")
            register_window.destroy()  # Close the register window
        else:
            messagebox.showerror("Registration Failed", "Username already exists.")
    
    def show_all_users(self):
        all_users = skillmatchDB.get_all_users()
        
        users_window = tk.Toplevel(self.root)
        users_window.title("All Registered Users")
        
        text_box = tk.Text(users_window, wrap=tk.WORD, width=80, height=20)
        text_box.pack(padx=20, pady=20)
        
        text_box.insert(tk.END, "ID | First Name | Last Name | Specialty | Skills | Username | Skill Level | Rate\n")
        text_box.insert(tk.END, "=" * 80 + "\n")
        
        for user in all_users:
            text_box.insert(tk.END, f"{user[0]} | {user[1]} | {user[2]} | {user[3]} | {user[4]} | {user[5]} | {user[7]} | {user[8]}\n")
        
        text_box.config(state=tk.DISABLED)
    
    def logout_user(self):
        confirm = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if confirm:
            self.logged_in_user = None
            self.create_login_widgets()  # Go back to the login screen
            messagebox.showinfo("Logged Out", "You have been logged out.")
    
    def delete_account(self):
        confirm = messagebox.askyesno("Delete Account", "Are you sure you want to delete your account?")
        if confirm:
            success = skillmatchDB.delete_user_account(self.logged_in_user['id'])
            if success:
                messagebox.showinfo("Account Deleted", "Your account has been deleted.")
                self.logged_in_user = None
                self.create_login_widgets()  # Go back to the login screen
            else:
                messagebox.showerror("Deletion Failed", "There was an error deleting your account.")
    
    def view_transaction_history(self):
        # Add functionality for viewing transaction history here
        messagebox.showinfo("Transaction History", "Feature coming soon!")

    def delete_all_users(self):
        confirm = messagebox.askyesno("Delete All Users", "Are you sure you want to delete all users?")
        if confirm:
            success = skillmatchDB.delete_all_users()
            if success:
                messagebox.showinfo("All Users Deleted", "All user accounts have been deleted.")
            else:
                messagebox.showerror("Deletion Failed", "There was an error deleting all users.")


    def show_top_up_window(self):
        top_up_window = tk.Toplevel(self.root)
        top_up_window.title("Top Up Credits")
        top_up_window.geometry("400x300")
        
        options = {
            "1": (1000, 799),
            "2": (499, 449),
            "3": (200, 189),
            "4": (100, 99),
        }
        
        for option, (credits, price) in options.items():
            tk.Button(top_up_window, text=f"{credits} credits for {price} Pesos", command=lambda c=credits: self.top_up_credits(c)).pack(pady=5)
        
    def top_up_credits(self, credits):
        self.logged_in_user['credits'] += credits
        skillmatchDB.update_user_credits(self.logged_in_user['id'], self.logged_in_user['credits'])
        messagebox.showinfo("Top Up Successful", f"{credits} credits added to your account!")

    def perform_trade(self):
        selected_skill_index = self.skills_listbox.curselection()

        if selected_skill_index:
            selected_skill = self.skills_listbox.get(selected_skill_index)
            
            # Call the backend trade function
            success = self.app.trade_user_skills(self.logged_in_user['id'], selected_skill)
            
            if success:
                messagebox.showinfo("Trade Successful", f"You have successfully traded the skill: {selected_skill}")
                # Remove the traded skill from the listbox
                self.skills_listbox.delete(selected_skill_index)
            else:
                messagebox.showerror("Trade Failed", "There was an issue with trading your skill.")
        else:
            messagebox.showwarning("No Skill Selected", "Please select a skill to trade.")

    def __init__(self, root, skillmatch_app):
            self.root = root
            self.app = skillmatch_app  # The backend app instance
            self.skill_tag_var = tk.StringVar()
            self.matching_profiles = []
            self.current_profile_index = 0

            self.main_menu()

    def main_menu(self):
    # Clear the screen
        for widget in self.root.winfo_children():
            widget.destroy()

        # Main Menu Buttons
        tk.Label(self.root, text="Main Menu", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.root, text="Trade Skills", command=self.trade_skills_gui).pack(pady=5)
        tk.Button(self.root, text="Top Up Credits", command=self.top_up_credits).pack(pady=5)
        tk.Button(self.root, text="View Registered Users", command=self.show_register_window).pack(pady=5)
        tk.Button(self.root, text="Logout", command=self.logout_user).pack(pady=5)


    def trade_skills_gui(self):
            # Clear the screen
            for widget in self.root.winfo_children():
                widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Skill Match")
    root.geometry("400x300")

    skillmatch_app = SkillMatchApp()  # Instantiate the backend logic
    gui = SkillMatchGUI(root, skillmatch_app)  # Pass both arguments

    root.mainloop()
