# Danh sách để lưu các công việc
tasks = []

def add_task(task_name):
    """Thêm một công việc mới vào danh sách."""
    task = {'name': task_name, 'completed': False}
    tasks.append(task)
    print(f"Đã thêm công việc: '{task_name}'")

def complete_task(task_index):
    """Đánh dấu một công việc là đã hoàn thành."""
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        print(f"Đã hoàn thành công việc: '{tasks[task_index]['name']}'")
    else:
        print("Chỉ số công việc không hợp lệ!")

def delete_task(task_index):
    """Xóa một công việc khỏi danh sách dựa trên chỉ số."""
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"Đã xóa công việc: '{removed_task['name']}'")
    else:
        print("Chỉ số công việc không hợp lệ!")

def list_tasks():
    """Duyệt qua danh sách tasks và in ra trạng thái [x] hoặc [ ]."""
    if not tasks:
        print("Danh sách công việc đang trống.")
        return
    
    print("\n--- DANH SÁCH CÔNG VIỆC ---")
    for i, task in enumerate(tasks, 1):
        status = "[x]" if task['completed'] else "[ ]"
        print(f"{i}. {status} {task['name']}")

# --- Điểm bắt đầu của chương trình
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")
    add_task("Nộp bài tập cho thầy")
    
    list_tasks()
    
    print("\n--- Thực hiện đánh dấu hoàn thành ---")
    complete_task(0)
    list_tasks()
    
    print("\n--- Thực hiện xóa công việc ---")
    delete_task(1)  # Xóa công việc "Làm bài tập thực hành ở nhà"
    list_tasks()