# Advanced Project 1: Personal Task Manager 📋

import datetime

# Task Manager with lists and dictionaries
class SimpleTaskManager:
    def __init__(self):
        self.tasks = []
        self.task_id = 1
    
    def add_task(self, title, description="", priority="medium"):
        task = {
            "id": self.task_id,
            "title": title,
            "description": description,
            "priority": priority,
            "completed": False,
            "created_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        self.tasks.append(task)
        self.task_id += 1
        return task["id"]
    
    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                return True
        return False
    
    def list_tasks(self, show_completed=True):
        if not self.tasks:
            print("No tasks yet!")
            return
        
        print("\n📋 Your Tasks:")
        print("=" * 50)
        
        for task in self.tasks:
            if not show_completed and task["completed"]:
                continue
                
            status = "✅" if task["completed"] else "⏳"
            priority_icon = {"high": "🔴", "medium": "🟡", "low": "🟢"}.get(task["priority"], "⚪")
            
            print(f"{status} [{task['id']}] {priority_icon} {task['title']}")
            if task["description"]:
                print(f"    📝 {task['description']}")
            print(f"    📅 Created: {task['created_date']}")
            print()
    
    def delete_task(self, task_id):
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                removed_task = self.tasks.pop(i)
                return removed_task["title"]
        return None
    
    def get_stats(self):
        total = len(self.tasks)
        completed = len([t for t in self.tasks if t["completed"]])
        pending = total - completed
        
        if total == 0:
            completion_rate = 0
        else:
            completion_rate = (completed / total) * 100
        
        return {
            "total": total,
            "completed": completed,
            "pending": pending,
            "completion_rate": completion_rate
        }

def main():
    task_manager = SimpleTaskManager()
    
    print("🎯 Welcome to Your Personal Task Manager!")
    print("Type 'help' to see available commands")
    
    while True:
        print("\n" + "="*50)
        command = input("Enter command: ").lower().strip()
        
        if command == "help":
            print("\n📚 Available Commands:")
            print("  add - Add a new task")
            print("  list - Show all tasks")
            print("  pending - Show only pending tasks")
            print("  complete - Mark a task as completed")
            print("  delete - Delete a task")
            print("  stats - Show task statistics")
            print("  quit - Exit the program")
            
        elif command == "add":
            title = input("Task title: ")
            description = input("Description (optional): ")
            
            print("Priority level:")
            print("  1. High 🔴")
            print("  2. Medium 🟡")
            print("  3. Low 🟢")
            
            priority_choice = input("Choose priority (1-3, default 2): ").strip()
            priority_map = {"1": "high", "2": "medium", "3": "low"}
            priority = priority_map.get(priority_choice, "medium")
            
            task_id = task_manager.add_task(title, description, priority)
            print(f"✅ Task added with ID: {task_id}")
            
        elif command == "list":
            task_manager.list_tasks()
            
        elif command == "pending":
            task_manager.list_tasks(show_completed=False)
            
        elif command == "complete":
            try:
                task_id = int(input("Enter task ID to complete: "))
                if task_manager.complete_task(task_id):
                    print(f"🎉 Task {task_id} marked as completed!")
                else:
                    print("❌ Task not found!")
            except ValueError:
                print("❌ Please enter a valid task ID number!")
                
        elif command == "delete":
            try:
                task_id = int(input("Enter task ID to delete: "))
                deleted_title = task_manager.delete_task(task_id)
                if deleted_title:
                    print(f"🗑️ Deleted task: {deleted_title}")
                else:
                    print("❌ Task not found!")
            except ValueError:
                print("❌ Please enter a valid task ID number!")
                
        elif command == "stats":
            stats = task_manager.get_stats()
            print(f"\n📊 Task Statistics:")
            print(f"  Total tasks: {stats['total']}")
            print(f"  Completed: {stats['completed']}")
            print(f"  Pending: {stats['pending']}")
            print(f"  Completion rate: {stats['completion_rate']:.1f}%")
            
        elif command == "quit":
            print("👋 Thanks for using the Task Manager! Stay organized!")
            break
            
        else:
            print("❌ Unknown command. Type 'help' for available commands.")

if __name__ == "__main__":
    main()

# 🎯 Features of this project:
# - Uses lists to store multiple tasks
# - Uses dictionaries to store task information
# - Uses functions to organize code
# - Uses loops for the main program flow
# - Uses if/else statements for decision making
# - Combines multiple programming concepts!

# 💡 Ideas to extend this project:
# 1. Add due dates for tasks
# 2. Save tasks to a file so they persist
# 3. Add categories or tags for tasks
# 4. Add task search functionality
# 5. Create a simple GUI version