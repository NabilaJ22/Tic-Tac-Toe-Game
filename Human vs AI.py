import tkinter as tk
from tkinter import messagebox
import random


class TicTacToe:
    def __init__(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe - Human Vs AI")
        self.root.configure(bg='white') 
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text="", font=('Arial', 30), width=4, height=2,
                                                command=lambda i=i, j=j: self.on_button_click(i, j), bg= 'yellow') 
                self.buttons[i][j].grid(row=i, column=j)
        self.status_label = tk.Label(self.root, text="Player Human's turn", font=('Arial', 14), bg='white')
        self.status_label.grid(row=3, columnspan=3)

    def on_button_click(self, row, col):
        if self.board[row][col] == "" and not self.check_winner() and not self.check_draw():
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner():
                self.show_result(f"Player {self.current_player} wins!")
            elif self.check_draw():
                self.show_result("It's a draw!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"Player {self.current_player}'s turn")
                if self.current_player == "O":
                    self.ai_move()

    def ai_move(self):
        best_score = float("-inf")
        move = None
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    self.board[i][j] = "O"
                    score = self.minimax(False)
                    self.board[i][j] = ""
                    if score > best_score:
                        best_score = score
                        move = (i, j)
        row, col = move
        print("AI chose ", move, "& best score:", best_score)
        self.board[row][col] = "O"
        self.buttons[row][col].config(text="O")
        if self.check_winner():
            self.show_result("AI wins!")
        elif self.check_draw():
            self.show_result("It's a draw!")
        else:
            self.current_player = "X"
            self.status_label.config(text="Player Humans's turn")

    def minimax(self, is_maximizing):
        if self.check_winner():
            stateEval = -1 if is_maximizing else 1 
            print("End State:", stateEval)
            return stateEval
        elif self.check_draw():
            print("End State: draw")
            return 0

        if is_maximizing:
            best_score = float("-inf")
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == "":
                        print(f"Human may choose ({i},{j})")
                        self.board[i][j] = "O"
                        score = self.minimax(False)
                        self.board[i][j] = ""
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float("inf")
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == "":
                        print(f"AI is considering ({i},{j})...")
                        self.board[i][j] = "X"
                        score = self.minimax(True)
                        self.board[i][j] = ""
                        best_score = min(score, best_score)
            return best_score

    def check_winner(self):
        
        for row in self.board:
            if row[0] == row[1] == row[2] != "":
                return True
        
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != "":
                return True
      
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == "":
                    return False
        return True

    def show_result(self, message):
        print(message)
        messagebox.showinfo("Game Over", message)
        self.root.quit()

if __name__ == "__main__":
    game = TicTacToe()
    game.root.mainloop()


