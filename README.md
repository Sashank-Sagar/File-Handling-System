# File Management App

A simple file management system built using Python. This app provides an easy-to-use, menu-driven interface for managing files, including creating, editing, reading, deleting, and viewing files in the current directory.

---

## Features

- **Create Files:** Create new files in the current directory.
- **Edit Files:** Append content to an existing file.
- **Read Files:** View the contents of a file.
- **Delete Files:** Delete files from the directory.
- **View All Files:** List all files in the current directory.

---

## How to Use

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/file-management-app.git
   ```

2. Navigate to the project directory:
   ```bash
   cd file-management-app
   ```

3. Run the program:
   ```bash
   python file_management_app.py
   ```

4. Follow the on-screen menu to perform file management tasks.

---

## Menu Options

1. **Create file:** Enter the name of the file to create.
2. **Edit file:** Enter the name of the file and add content to it.
3. **Read file:** Enter the name of the file to view its contents.
4. **Delete file:** Enter the name of the file to delete.
5. **View all files:** List all files in the current directory.
6. **Exit:** Close the program.

---

## Error Handling

The app includes error handling for common issues, such as:
- Attempting to create a file that already exists.
- Trying to delete or edit a file that doesn't exist.
- Handling unexpected errors gracefully.

---

## Creating an Executable File

The program has also been converted into an executable file for easy access without requiring a Python environment. Use tools like [PyInstaller](https://pyinstaller.org/en/stable/) to create the executable:

```bash
pyinstaller --onefile file_management_app.py
```

The executable will be available in the `dist` folder.

---

## Technologies Used

- Python (Standard Library)

---

## Contributing

Contributions are welcome! If you have suggestions for improvements or additional features, feel free to fork this repository and create a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contact

If you have any questions or feedback, feel free to reach out to me on [LinkedIn](https://www.linkedin.com/in/yourprofile/) or open an issue in this repository.

