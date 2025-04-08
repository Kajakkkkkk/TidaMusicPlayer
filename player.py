import os
import random
import pygame
from mutagen.mp3 import MP3
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget, QMessageBox
from ui import build_ui


class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MUSIC PLAYER")
        self.setGeometry(200, 200, 400, 200)

        self.playlist = []
        self.current_index = 0
        self.is_looping = False
        self.is_shuffling = False
        self.total_length = 0

        pygame.mixer.init()
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_time)

        self.build_ui()
        self.load_music_folder()

    def build_ui(self):
        build_ui(self)
        self.play_button.clicked.connect(self.play_song)
        self.pause_button.clicked.connect(self.pause_song)
        self.prev_button.clicked.connect(self.prev_song)
        self.next_button.clicked.connect(self.next_song)
        self.restart_button.clicked.connect(self.restart_song)
        self.shuffle_button.clicked.connect(self.toggle_shuffle)
        self.loop_button.clicked.connect(self.toggle_loop)
        self.volume_slider.valueChanged.connect(self.set_volume)

    def load_music_folder(self):
        for file in os.listdir('.'):
            if file.endswith('.mp3'):
                self.playlist.append(file)

        if self.playlist:
            self.load_song(self.current_index)

    def load_song(self, index):
        try:
            file = self.playlist[index]
            pygame.mixer.music.load(file)
            audio = MP3(file)
            self.total_length = int(audio.info.length)
            bitrate = int(audio.info.bitrate / 1000)
            mixrate = int(audio.info.sample_rate / 1000)

            self.song_title.setText(f"{index + 1}. {file}")
            self.bitrate_label.setText(f"BITRATE: {bitrate} kbps")
            self.mixrate_label.setText(f"MIXRATE: {mixrate} kHz")
            minutes = self.total_length // 60
            seconds = self.total_length % 60
            self.time_label.setText(f"00:00 / {minutes:02}:{seconds:02}")
        except Exception as e:
            QMessageBox.critical(self, "Błąd ładowania", str(e))

    def play_song(self):
        pygame.mixer.music.play()
        self.timer.start()

    def pause_song(self):
        pygame.mixer.music.pause()
        self.timer.stop()

    def restart_song(self):
        pygame.mixer.music.rewind()
        self.timer.start()
        self.time_label.setText(f"00:00 / {self.total_length // 60:02}:{self.total_length % 60:02}")

    def prev_song(self):
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.load_song(self.current_index)
        self.play_song()

    def next_song(self):
        if self.is_shuffling:
            self.current_index = random.randint(0, len(self.playlist) - 1)
        else:
            self.current_index = (self.current_index + 1) % len(self.playlist)
        self.load_song(self.current_index)
        self.play_song()

    def toggle_loop(self):
        self.is_looping = not self.is_looping
        self.loop_button.setStyleSheet("color: green" if self.is_looping else "")

    def toggle_shuffle(self):
        self.is_shuffling = not self.is_shuffling
        self.shuffle_button.setStyleSheet("color: green" if self.is_shuffling else "")

    def update_time(self):
        if pygame.mixer.music.get_busy():
            pos = pygame.mixer.music.get_pos() // 1000
            minutes = pos // 60
            seconds = pos % 60
            total_minutes = self.total_length // 60
            total_seconds = self.total_length % 60
            self.time_label.setText(f"{minutes:02}:{seconds:02} / {total_minutes:02}:{total_seconds:02}")
        else:
            if self.is_looping:
                self.restart_song()
            else:
                self.next_song()

    def set_volume(self, value):
        pygame.mixer.music.set_volume(value / 100.0)
