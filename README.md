# 🐍 Classic Snake Game in Python

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Object-Oriented Programming](https://img.shields.io/badge/OOP-Modular-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

A fully-featured, object-oriented implementation of the classic **Snake Game** built using Python's `turtle` graphics module, packaged into a standalone Windows executable (`.exe`).

</div>

---

<img width="980" height="951" alt="Animation" src="https://github.com/user-attachments/assets/3bd447e8-09ab-4393-93ff-49a3c6d0afc8" />

## 📌 Table of Contents
- [About The Project](#-about-the-project)
- [Features](#-features)
- [Project Architecture](#-project-architecture)
- [How to Run (Source Code)](#%EF%B8%8F-how-to-run-source-code)
- [Controls](#-controls)
- [What I Learned](#-what-I-learned)

---

## 🚀 About The Project
This project is a classic recreation of the retro Snake game. It was built with a strong focus on **Object-Oriented Programming (OOP)** principles, cleanly separating concerns into different modular files for maintainability and scalability. 

---

## ✨ Features
* **Modular OOP Design:** Logic is split across dedicated classes (`Snake`, `Food`, `Scoreboard`).
* **Dynamic Gameplay:** Real-time score tracking, collision detection with walls and self, and random food generation.
* **Standalone Executable:** Compiled using PyInstaller so it can run smoothly on Windows without requiring a Python environment.
* **Smooth Rendering:** Utilizes screen tracer controls to eliminate flickering during turtle animations.

---

## 📂 Project Architecture
The codebase is structured cleanly to separate game logic:
```text
Snake-Game/
├── main.py        # Main game loop, event listeners, and collision logic
├── snake.py       # Snake class (movement, growth, and direction controls)
├── food.py        # Food class (random spawning logic inheriting from Turtle)
└── score.py       # Scoreboard class (score tracking and Game Over states)
