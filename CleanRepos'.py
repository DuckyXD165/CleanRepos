import os
import tkinter as tk
from tkinter import messagebox
import subprocess
import sys

home_dir = os.path.expanduser("~")
path = os.path.join(home_dir, 'CleanRepos')

def check_git_installed():
    try:
        subprocess.run(['git', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def check_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
    StartApp()

def pull_repo(repo_url, path):
    try:
        repo_name = os.path.basename(repo_url).replace('.git', '')
        repo_path = os.path.join(path, repo_name)
        subprocess.run(['git', 'clone', repo_url, repo_path], check=True)
        messagebox.showinfo("Success", "Repository cloned successfully!")
        os.startfile(repo_path)
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to clone the repository.")

def StartApp():
    m = tk.Tk()
    m.title("GitHub Repo Puller")

    bg_color = "#2e2e2e"
    fg_color = "#ffffff"
    btn_color = "#444444"
    btn_fg_color = "#ffffff"
    entry_bg_color = "#3e3e3e"
    entry_fg_color = "#ffffff"

    m.configure(bg=bg_color)

    tk.Label(m, text="Enter GitHub Repository URL:", bg=bg_color, fg=fg_color).pack(pady=10)
    repo_url_entry = tk.Entry(m, width=50, bg=entry_bg_color, fg=entry_fg_color)
    repo_url_entry.pack(pady=5)

    def on_pull_button_click():
        repo_url = repo_url_entry.get()
        if repo_url:
            pull_repo(repo_url, path)
        else:
            messagebox.showwarning("Input Error", "Please enter a repository URL.")

    pull_button = tk.Button(m, text="Pull Repository", command=on_pull_button_click, bg=btn_color, fg=btn_fg_color)
    pull_button.pack(pady=20)

    m.mainloop()

if __name__ == '__main__':
    if not check_git_installed():
        messagebox.showerror("Git Not Found", "Git is not installed on your system. Please install Git and try again.")
        sys.exit(1)
    check_dir(path)
