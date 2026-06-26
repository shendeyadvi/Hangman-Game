# 🎮 Hangman Game in Python

A simple command-line **Hangman Game** built using Python. The game randomly selects a word from a predefined list, and the player has **6 attempts** to guess the word one letter at a time.

---

## 📌 Features

* Random word selection using the `random` module.
* User-friendly command-line interface.
* Displays correctly guessed letters and hidden letters.
* Prevents duplicate guesses.
* Validates user input.
* Gives a maximum of **6 incorrect attempts**.
* Displays a win or lose message at the end.

---

## 🛠️ Technologies Used

* Python 3
* `random` module

---

## 📂 Project Structure

```
Hangman-Game/
│
├── hangman.py
└── README.md
```

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/Hangman-Game.git
```

2. Navigate to the project folder:

```bash
cd Hangman-Game
```

3. Run the program:

```bash
python hangman.py
```

---

## 🎯 How to Play

* The game randomly selects a word.
* The word is displayed as underscores (`_`).
* Enter one letter at a time.
* If the letter exists in the word, it is revealed.
* If the letter is incorrect, one attempt is lost.
* You have **6 incorrect guesses** before the game ends.

---

## 💻 Sample Output

```
------- HANGMAN GAME -------

Word: _ _ _ _ _

Enter a letter: a
Correct!

Word: a _ _ _ _
```

---

## 📚 Concepts Used

* Variables
* Lists
* Loops (`while`, `for`)
* Conditional Statements (`if-else`)
* String Manipulation
* User Input
* Random Module

---

## 🚀 Future Improvements

* Add difficulty levels (Easy, Medium, Hard)
* Use a larger word database
* Display ASCII Hangman graphics
* Add score tracking
* Allow hints
* Save high scores

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request.

---

## 📄 License

This project is open-source and available under the **MIT License**.

---

## 👨‍💻 Author

**Yadavi Shende**

If you like this project, don't forget to ⭐ the repository!
