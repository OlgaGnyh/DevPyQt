from PySide6 import QtWidgets
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView, QDialog, QFormLayout, QMessageBox
import datetime

class NotesDataBase:
    def __init__(self, db_name):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(db_name)

        if not self.db.open():
            raise Exception(f"Cannot open database: {self.db.lastError().text()}")

    def create_table(self):
        query = QSqlQuery()
        query.prepare("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            textnote TEXT NOT NULL,
            date TEXT NOT NULL,
            deadline TEXT NOT NULL)
        """)
        if not query.exec():
            raise Exception(f"Failed to create table: {query.lastError().text()}")

    def insert_note(self, name, textnote, date, deadline):  # Добавление в БД
        query = QSqlQuery()
        query.prepare("INSERT INTO notes (name, textnote, date, deadline) VALUES (?, ?, ?, ?)")
        query.addBindValue(name)
        query.addBindValue(textnote)
        query.addBindValue(date)
        query.addBindValue(deadline)

        if not query.exec():
            raise Exception(f"Failed to insert note: {query.lastError().text()}")

    def fetch_notes(self):  # Получение всех пользователей из БД
        query = QSqlQuery("SELECT id, name, textnote, date, deadline  FROM notes")
        notes = []
        while query.next():
            note = {
                "id": query.value(0),
                "name": query.value(1),
                "textnote": query.value(2),
                "date": query.value(3),
                "deadline": query.value(4)
            }
            notes.append(note)
        return notes

    def delete_note(self, note_id):  # Удаление заметки
        query = QSqlQuery()
        query.prepare("DELETE FROM notes WHERE id = ?")
        query.addBindValue(note_id)
        if not query.exec():
            raise Exception(f"Failed to delete note: {query.lastError().text()}")

    def update_note(self, note_id, name, textnote, date, deadline):    # Изменение данных в БД
        query = QSqlQuery()
        query.prepare("UPDATE notes SET name = ?, textnote = ?, date = ?, deadline = ? WHERE id = ?")
        query.addBindValue(name)
        query.addBindValue(textnote)
        query.addBindValue(date)
        query.addBindValue(deadline)
        query.addBindValue(note_id)
        if not query.exec():
            raise Exception(f"Failed to update note: {query.lastError().text()}")


class AddNoteDialog(QDialog):
    def __init__(self, db_manager):
        super().__init__()
        self.setWindowTitle("Добавление заметки")
        self.db_manager = db_manager
        self.initUi()

    def initUi(self):
        layout = QFormLayout()

        self.name_input = QtWidgets.QLineEdit()
        self.textnote_input = QtWidgets.QLineEdit()
        # self.date_input = QtWidgets.QLineEdit()
        self.deadline_input = QtWidgets.QDateTimeEdit()
        self.deadline_input.setCalendarPopup(True)
        self.deadline_input.setDateTime(datetime.datetime.now())

        layout.addRow("Заголовок:", self.name_input)
        layout.addRow("Текст заметки:", self.textnote_input)
        # layout.addRow("Дата создания:", self.date_input)
        layout.addRow("Деадлайн:", self.deadline_input)

        self.add_button = QtWidgets.QPushButton("Добавить заметку")
        self.add_button.clicked.connect(self.add_note)
        layout.addWidget(self.add_button)

        self.setLayout(layout)

    def add_note(self):
        name = self.name_input.text()
        textnote = self.textnote_input.text()
        date = str(datetime.datetime.now().strftime("%d.%m.%Y %H:%M "))
        deadline = self.deadline_input.text()


        try:
            self.db_manager.insert_note(name, textnote, date, deadline)
            QMessageBox.information(self, "Успех", "Заметка успешно добавлена")
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Заметки')

        self.db_manager = NotesDataBase("notes.db")
        self.db_manager.create_table()
        self.setGeometry(300, 300, 800, 500)
        self.setFixedSize(800, 600)
        self.initUi()


    def initUi(self) -> None:
        layout = QtWidgets.QVBoxLayout()
        self.label_notes = QtWidgets.QLabel('Заметки')
        self.update_data_button = QtWidgets.QPushButton('Обновить данные')
        self.update_data_button.clicked.connect(lambda: self.show_notes())

        self.table_notes = QTableWidget()
        self.table_notes.setColumnCount(5)
        self.table_notes.setHorizontalHeaderLabels(["ID", "Заголовок", "Текст заметки", "Дата добавления", "Дедлайн"])
        # self.table_notes.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_notes.setColumnWidth(0, 20)
        self.table_notes.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        self.table_notes.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        self.table_notes.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        self.table_notes.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)

        self.show_notes()
        self.add_note_button = QtWidgets.QPushButton('Добавить заметку')
        self.add_note_button.clicked.connect(self.open_add_note_dialog)

        self.delete_note_button = QtWidgets.QPushButton('Удалить заметку')
        self.delete_note_button.clicked.connect(lambda: self.delete_note(int(self.chose_id())))

        self.update_note_button = QtWidgets.QPushButton('Изменить')
        self.update_note_button.clicked.connect(lambda: self.update_note(self.chose_row()))

        layout.addWidget(self.label_notes)
        layout.addWidget(self.update_data_button)
        layout.addWidget(self.table_notes)
        layout.addWidget(self.add_note_button)
        layout.addWidget(self.delete_note_button)
        layout.addWidget(self.update_note_button)
        self.setLayout(layout)

    def show_notes(self):
        try:
            notes = self.db_manager.fetch_notes()
            self.table_notes.setRowCount(len(notes))
            for row, note in enumerate(notes):
                self.table_notes.setItem(row, 0, QTableWidgetItem(str(note["id"])))
                self.table_notes.setItem(row, 1, QTableWidgetItem(str(note["name"])))
                self.table_notes.setItem(row, 2, QTableWidgetItem(str(note["textnote"])))
                self.table_notes.setItem(row, 3, QTableWidgetItem(str(note["date"])))
                self.table_notes.setItem(row, 4, QTableWidgetItem(str(note["deadline"])))
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def open_add_note_dialog(self):
        dialog = AddNoteDialog(self.db_manager)
        dialog.exec()

    def chose_id(self):
        id_ = self.table_notes.selectedItems()
        if id_:
            row = id_[0].row()
            note_id = self.table_notes.item(row, 0).text()
            return note_id

    def chose_row(self):
        id_ = self.table_notes.selectedItems()
        if id_:
            row = id_[0].row()
            return row
    def delete_note(self, note_id):
        try:
            self.db_manager.delete_note(int(note_id))
            QMessageBox.information(self, "Успех", "Заметка успешно удалена!")
            self.show_notes()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def update_note(self, row):
        try:
            note_id  = int(self.table_notes.item(row, 0).text())
            name     = self.table_notes.item(row, 1).text()
            textnote = self.table_notes.item(row, 2).text()
            date     = self.table_notes.item(row, 3).text()
            deadline = self.table_notes.item(row, 4).text()

            self.db_manager.update_note(note_id, name, textnote, date, deadline)
            QMessageBox.information(self, "Успех", "Заметка обновлена")
            self.show_notes()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
