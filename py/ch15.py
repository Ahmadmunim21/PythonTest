
import sqlite3

class DatabaseManager:
    def __init__(self, db_name='example.db'):
        self.db_name = db_name
        self.init__database()

    def init__database(self):
        """Initializes the database with tables"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    age INTEGER,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS posts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    title TEXT NOT NULL,
                    content TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users (id)
                )
            ''')


    def create_user(self, name, email, age):
        """Creates a new user in the database"""
        try:    
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO users (name, email, age)
                    VALUES (?, ?, ?)
                ''', (name, email, age))
                return cursor.lastrowid
        except sqlite3.IntegrityError as e:
            print(f"Error adding user: {e}")
            return None
        
    def create_post(self, user_id, title, content):
        """Creates a new post for a user"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO posts (user_id, title, content)
                VALUES (?, ?, ?)
            ''', (user_id, title, content))
            return cursor.lastrowid
        
    def get_all_users(self):
        """Get all users"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users')
            return cursor.fetchall()
    
    def get_user_posts(self, user_id):
        """Get all posts for a specific user"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''  
                SELECT p.id, p.title, p.content, p.created_at
                FROM posts p
                WHERE p.user_id = ?
                ORDER BY p.created_at DESC
            ''', (user_id,))
            return cursor.fetchall()
    
    def update_user(self, user_id, name, email, age):
        """Updates an existing user's information"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE users 
                SET name = ?, email = ?, age = ? 
                WHERE id = ?
            ''', (name, email, age, user_id))
            return cursor.rowcount > 0 

    def update_post(self, post_id, title, content):
        """Updates an existing post's title and content"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE posts 
                SET title = ?, content = ? 
                WHERE id = ?
            ''', (title, content, post_id))
            return cursor.rowcount > 0
        
    def delete_user(self, user_id):
        """Deletes a user and their posts"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM posts WHERE user_id = ?', (user_id,))
            cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
            return cursor.rowcount > 0

    def display_menu():
        """Displays the main menu"""
        print("\n" + "="*40)
        print("                 Menu:")
        print("="*40)
        print("1. Create User")
        print("2. View All Users")
        print("3. Create Post")
        print("4. View User Posts")
        print("5. Update User")
        print("6. Delete User")
        print("7. Exit")
        print("="*40)

def main():
    """Main CLI function to run the application""" 
    db = DatabaseManager()

    while True:
        DatabaseManager.display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            print("Creating a new user...")
            name = input("Enter name: ").strip()
            email = input("Enter email: ").strip()
            try:
                age = int(input("Enter age: ").strip())
                user_id = db.create_user(name, email, age) 
                if user_id:
                    print(f"User created with ID: {user_id}")
                else:
                    print("Failed to create user.")
            except ValueError:
                print("Invalid age. Please enter a number.")

        elif choice == '2':
            print("\n--- All Users ---")
            users = db.get_all_users()
            if users:
                for user in users:
                    print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}, Age: {user[3]}")
            else:
                print("No users found.")
        
        elif choice == '3':
            print("\n--- Create a new post for a user ---")
            try:
                user_id = int(input("Enter user ID: ").strip())
                title = input("Enter post title: ").strip()
                content = input("Enter post content: ").strip()
                post_id = db.create_post(user_id, title, content)
                if post_id:
                    print(f"Post created with ID: {post_id}")
                else:
                    print("Failed to create post.")
            except ValueError:
                print("Invalid user ID. Please enter a number.")

        elif choice == '4':
            print("\n--- View posts for a user ---")
            try:
                user_id = int(input("Enter user ID: ").strip())
                posts = db.get_user_posts(user_id)
                if posts:
                    for post in posts:
                        print(f"ID: {post[0]}, Title: {post[1]}, Content: {post[2]}, Created At: {post[3]}")
                else:
                    print("No posts found for this user.")
            except ValueError:
                print("Invalid user ID. Please enter a number.")

        elif choice == '5':
            print("\n--- Update User ---")
            try:
                user_id = int(input("Enter the ID of the user to update: ").strip())
                new_name = input("Enter new name: ").strip()
                new_email = input("Enter new email: ").strip()
                new_age = int(input("Enter new age: ").strip())
            
                if db.update_user(user_id, new_name, new_email, new_age):
                    print("✓ User updated successfully!")
                else:
                    print("X User not found or update failed.")
            except ValueError:
                print("X Invalid input. ID and Age must be numbers.")

        elif choice == '6':
            print("\n--- Delete a user ---")
            try:
                user_id = int(input("Enter user ID to delete: ").strip())
                confirm = input(f" Are sure you want to delete user {user_id}? (y/N): ").strip().lower()
                if confirm == "y":
                    if db.delete_user(user_id):
                        print("User deleted successfully.")
                    else:
                        print("User not found or could not be deleted.")
                else:
                    print("Deletion cancelled.")
            except ValueError:
                print("Invalid user ID. Please enter a number.")

        elif choice == '7':
            print("Exiting the application. Goodbye!")
            break  

        else:
            print("Invalid choice. Please try again. Enter a number between 1 and 6.")
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()

