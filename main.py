import sys
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QLabel, QDateTimeEdit, QPushButton, QWidget, QLineEdit, QTimeEdit, QPlainTextEdit

from PyQt6.QtCore import QDateTime, QTime

class HoursCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hours Calculator")
        self.setGeometry(100, 100, 400, 300)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Section 1: Time Difference Within a Day
        time_layout = QVBoxLayout()
        time_label = QLabel("Calculate Time Difference (Same Day):")

        # Start Time
        start_time_layout = QHBoxLayout()
        start_time_label = QLabel("Start Time:")
        self.start_time = QTimeEdit()
        self.start_time.setTime(QTime.currentTime())
        start_time_layout.addWidget(start_time_label)
        start_time_layout.addWidget(self.start_time)

        # End Time
        end_time_layout = QHBoxLayout()
        end_time_label = QLabel("End Time:")
        self.end_time = QTimeEdit()
        self.end_time.setTime(QTime.currentTime())
        end_time_layout.addWidget(end_time_label)
        end_time_layout.addWidget(self.end_time)

        # Calculate Button for Time Difference
        self.calculate_time_button = QPushButton("Calculate Time Difference")
        self.calculate_time_button.clicked.connect(self.calculate_time_difference)

        # Result for Time Difference
        time_result_layout = QHBoxLayout()
        time_result_label = QLabel("Difference:")
        self.time_result_field = QPlainTextEdit()
        self.time_result_field.setReadOnly(True)
        time_result_layout.addWidget(time_result_label)
        time_result_layout.addWidget(self.time_result_field)

        time_layout.addWidget(time_label)
        time_layout.addLayout(start_time_layout)
        time_layout.addLayout(end_time_layout)
        time_layout.addWidget(self.calculate_time_button)
        time_layout.addLayout(time_result_layout)

        # Section 2: Date and Time Difference
        datetime_layout = QVBoxLayout()
        datetime_label = QLabel("Calculate Difference Between Dates and Times:")

        # Start Date and Time
        start_layout = QHBoxLayout()
        start_label = QLabel("Start Date and Time:")
        self.start_datetime = QDateTimeEdit()
        self.start_datetime.setCalendarPopup(True)
        self.start_datetime.setDateTime(QDateTime.currentDateTime())
        start_layout.addWidget(start_label)
        start_layout.addWidget(self.start_datetime)

        # End Date and Time
        end_layout = QHBoxLayout()
        end_label = QLabel("End Date and Time:")
        self.end_datetime = QDateTimeEdit()
        self.end_datetime.setCalendarPopup(True)
        self.end_datetime.setDateTime(QDateTime.currentDateTime())
        end_layout.addWidget(end_label)
        end_layout.addWidget(self.end_datetime)

        # Calculate Button for Date and Time Difference
        self.calculate_button = QPushButton("Calculate Date and Time Difference")
        self.calculate_button.clicked.connect(self.calculate_difference)

        # Result for Date and Time Difference
        result_layout = QHBoxLayout()
        result_label = QLabel("Difference:")
        self.result_field = QPlainTextEdit()
        self.result_field.setReadOnly(True)
        result_layout.addWidget(result_label)
        result_layout.addWidget(self.result_field)

        datetime_layout.addWidget(datetime_label)
        datetime_layout.addLayout(start_layout)
        datetime_layout.addLayout(end_layout)
        datetime_layout.addWidget(self.calculate_button)
        datetime_layout.addLayout(result_layout)

        # Add sections to main layout
        layout.addLayout(time_layout)
        layout.addLayout(datetime_layout)

        self.setLayout(layout)

    def calculate_time_difference(self):
        start = self.start_time.time()
        end = self.end_time.time()

        if start >= end:
            self.time_result_field.setPlainText("Invalid range")
            return

        difference = start.msecsTo(end) // 1000  # Convert milliseconds to seconds
        hours = difference // 3600
        minutes = (difference % 3600) // 60
        difference_in_minutes = difference // 60

        self.time_result_field.setPlainText(
            f"{hours} hours, {minutes} minutes ({difference_in_minutes} total minutes)"
        )

    def calculate_difference(self):
        start = self.start_datetime.dateTime()
        end = self.end_datetime.dateTime()

        if start >= end:
            self.result_field.setPlainText("Invalid range")
            return

        total_seconds = start.msecsTo(end) / 1000
        days = int(total_seconds // (24 * 3600))
        total_seconds %= (24 * 3600)
        hours = int(total_seconds // 3600)
        total_seconds %= 3600
        minutes = int(total_seconds // 60)

        difference_text_parts = []
        if days > 0:
            difference_text_parts.append(f"{days} days")
        if hours > 0:
            difference_text_parts.append(f"{hours} hours")
        if minutes > 0:
            difference_text_parts.append(f"{minutes} minutes")
        if not difference_text_parts:
            difference_text_parts.append("Less than a minute")

        total_hours = days * 24 + hours
        total_minutes = total_hours * 60 + minutes

        difference_text_parts.append(f" or {total_hours} hours or {total_minutes} minutes")
        self.result_field.setPlainText(", ".join(difference_text_parts))

app = QApplication(sys.argv)
window = HoursCalculator()
window.show()
sys.exit(app.exec())
