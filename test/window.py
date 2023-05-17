import sys
from PyQt6. QtWidgets import QApplication,QMainWindow, QLineEdit, QLabel,QPushButton,QDialog, QWidget,QVBoxLayout,QWidget, QMessageBox
from test import Test
from engine import session,text
import random

class Auth(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.login = QLabel("Логин")
        self.login_box = QLineEdit()
        self.password = QLabel("Пароль")
        self.password_box = QLineEdit()
        self.auth_btn = QPushButton("Вход")
        self.exit_btn = QPushButton("Выход")

        self.auth_btn.clicked.connect(self.auth)
        self.exit_btn.clicked.connect(self.exit)
        
        layout.addWidget(self.login)
        layout.addWidget(self.login_box)
        layout.addWidget(self.password)
        layout.addWidget(self.password_box)
        layout.addWidget(self.auth_btn)
        layout.addWidget(self.exit_btn)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


    def auth(self):
        sql = text("SELECT * FROM public.student")
        obj = session.execute(sql)
        for row in obj:
            for login in  row:
                self.login = login
            for password in row:
                self.password = password
            if self.login_box.text() == self.login and self.password_box.text() == self.password:
                self.sw = Test()
                self.sw.show()
                exe.close()
            else:
        
                self.captcha_dialog.start_timer()
                
                if self.captcha.exec() == QDialog.DialogCode.Accepted:
                    QMessageBox.information(self, "Успех", "Вход выполнен после капчи")
                
                else:
                    QMessageBox.warning(self, "Ошибка", "Неверные данные и капча")
                    self.login_attempts = 0
                    self.generate_captcha()




    def exit(self):
        exe.close()



class Captcha(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.captcha = QLabel(str(random.randint(1000,9999)))
        self.captcha_box = QLineEdit()
        self.captcha_ver = QPushButton()

        layout.addWidget(self.captcha)
        layout.addWidget(self.captcha_box)
        layout.addWidget(self.captcha_ver)

        self.captcha_ver.clicked.connect(self.ver)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        with open("style.css","r") as css:
            widget.setStyleSheet(css.read())


    def ver(self):
        if self.captcha.text() == self.captcha_box.text():
            self.window1 = Auth()
            self.window1.show()
        else:
            QMessageBox.critical(self,"Ошибка", "Не правильно введена капча")





app = QApplication(sys.argv)
exe = Auth()
exe.show()
app.exec()