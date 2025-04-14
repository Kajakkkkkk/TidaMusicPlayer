from PyQt5.QtWidgets import QLabel, QPushButton, QSlider, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt


def build_ui(self):
    self.setStyleSheet("""
        QWidget {
            background-color: #121212;
            color: #FFFFFF;
            font-size: 14px;
        }
        QPushButton {
            background-color: #1E1E1E;
            border: 1px solid #333;
            border-radius: 5px;
            padding: 5px 10px;
        }
        QPushButton:hover {
            background-color: #2C2C2C;
        }
        QPushButton:pressed {
            background-color: #3A3A3A;
        }
        QSlider::groove:horizontal {
            height: 6px;
            background: #333;
            border-radius: 3px;
        }
        QSlider::handle:horizontal {
            background: #00BCD4;
            width: 12px;
            height: 12px;
            margin: -4px 0;
            border-radius: 6px;
        }
    """)

    self.song_title = QLabel("SONG")
    self.time_label = QLabel("00:00 / 00:00")
    self.bitrate_label = QLabel("BITRATE: 128 kbps")
    self.mixrate_label = QLabel("MIXRATE: 44 kHz")

    self.play_button = QPushButton("▶")
    self.pause_button = QPushButton("⏸")
    self.prev_button = QPushButton("⏮")
    self.next_button = QPushButton("⏭")
    self.restart_button = QPushButton("⟲")
    self.shuffle_button = QPushButton("SHUFFLE")
    self.loop_button = QPushButton("LOOP")

    self.volume_slider = QSlider(Qt.Horizontal)
    self.volume_slider.setRange(0, 100)
    self.volume_slider.setValue(50)

    top_layout = QHBoxLayout()
    top_layout.addWidget(self.song_title)
    top_layout.addStretch()
    top_layout.addWidget(self.time_label)

    info_layout = QHBoxLayout()
    info_layout.addWidget(self.bitrate_label)
    info_layout.addWidget(self.mixrate_label)

    control_layout = QHBoxLayout()
    control_layout.addWidget(self.prev_button)
    control_layout.addWidget(self.restart_button)
    control_layout.addWidget(self.play_button)
    control_layout.addWidget(self.pause_button)
    control_layout.addWidget(self.next_button)

    bottom_layout = QHBoxLayout()
    bottom_layout.addWidget(self.shuffle_button)
    bottom_layout.addWidget(self.loop_button)
    bottom_layout.addStretch()
    bottom_layout.addWidget(QLabel("Volume"))
    bottom_layout.addWidget(self.volume_slider)

    main_layout = QVBoxLayout()
    main_layout.addLayout(top_layout)
    main_layout.addLayout(info_layout)
    main_layout.addLayout(control_layout)
    main_layout.addLayout(bottom_layout)

    self.setLayout(main_layout)
