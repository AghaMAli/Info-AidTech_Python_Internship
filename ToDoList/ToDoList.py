import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QListWidget, QFileDialog, QMessageBox

class Task:
    def __init__(self, title, description, status):
        self.title = title
        self.description = description
        self.status = status

class ToDoListApp(QWidget):
    def __init__(self):
        super().__init__()
        self.tasks = []
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('IAT To-Do List')
        self.setGeometry(100, 100, 800, 400)

        self.title_label = QLabel('Title:')
        self.title_entry = QLineEdit()
        self.description_label = QLabel('Description:')
        self.description_entry = QTextEdit()
        self.add_button = QPushButton('Add Task')
        self.add_button.clicked.connect(self.add_task)
        self.delete_button = QPushButton('Delete Task')
        self.delete_button.clicked.connect(self.delete_task)
        self.view_button = QPushButton('View Tasks')
        self.view_button.clicked.connect(self.view_tasks)
        self.save_button = QPushButton('Save Tasks')
        self.save_button.clicked.connect(self.save_tasks)
        self.load_button = QPushButton('Load Tasks')
        self.load_button.clicked.connect(self.load_tasks)
        self.task_list = QListWidget()

        layout_left = QVBoxLayout()
        layout_left.addWidget(self.title_label)
        layout_left.addWidget(self.title_entry)
        layout_left.addWidget(self.description_label)
        layout_left.addWidget(self.description_entry)
        layout_left.addWidget(self.add_button)
        layout_left.addWidget(self.delete_button)
        layout_left.addWidget(self.view_button)
        layout_left.addWidget(self.save_button)
        layout_left.addWidget(self.load_button)

        layout_right = QVBoxLayout()
        layout_right.addWidget(self.task_list)

        layout_main = QHBoxLayout()
        layout_main.addLayout(layout_left)
        layout_main.addLayout(layout_right)

        self.setLayout(layout_main)

    def add_task(self):
        title = self.title_entry.text()
        description = self.description_entry.toPlainText()
        if title:
            task = Task(title, description, "Not Completed")
            self.tasks.append(task)
            self.update_task_list()
            self.clear_fields()

    def delete_task(self):
        selected_task_index = self.task_list.currentRow()
        if selected_task_index >= 0:
            del self.tasks[selected_task_index]
            self.update_task_list()

    def view_tasks(self):
        self.task_list.clear()
        for task in self.tasks:
            self.task_list.addItem(f"Title: {task.title}\nDescription: {task.description}\nStatus: {task.status}\n")

    def save_tasks(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save Tasks", "", "Text Files (*.txt);;All Files (*)")
        if filename:
            with open(filename, "w") as file:
                for task in self.tasks:
                    file.write(f"{task.title},{task.description},{task.status}\n")
            QMessageBox.information(self, "Saved", "Tasks saved successfully.")

    def load_tasks(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Load Tasks", "", "Text Files (*.txt);;All Files (*)")
        if filename:
            self.tasks = []
            try:
                with open(filename, "r") as file:
                    for line in file:
                        components = line.strip().split(",")
                        if len(components) >= 2:
                            title, description = components[:2]
                            status = components[2] if len(components) > 2 else "Not Completed"
                            task = Task(title, description, status)
                            self.tasks.append(task)
            except FileNotFoundError:
                QMessageBox.warning(self, "File Not Found", "File not found.")
            self.update_task_list()

    def clear_fields(self):
        self.title_entry.clear()
        self.description_entry.clear()

    def update_task_list(self):
        self.task_list.clear()
        for task in self.tasks:
            self.task_list.addItem(f"Title: {task.title}\nDescription: {task.description}\nStatus: {task.status}\n")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    todo_app = ToDoListApp()
    todo_app.show()
    sys.exit(app.exec_())