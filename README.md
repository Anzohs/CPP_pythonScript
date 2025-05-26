# pythonScript

A collection of Python scripts designed to automate and streamline C++ development tasks, including class boilerplate generation and Makefile creation.

---

## 📁 Project Overview

This repository provides automation tools for:

- Generating C++ header (`.h`) and source (`.cpp`) files with constructors, destructors, and assignment operators.
- Creating a customizable Makefile that includes a colorful progress bar for compiling C++ projects.
- Scanning `.cpp` files in the current directory and subdirectories to build a valid compilation list.

---

## 🚀 Usage

### 1. Generate a C++ Class

To create a new C++ class with a header and source file:

```bash
python script.py ClassName
```

This generates:

- `ClassName.h`
- `ClassName.cpp`

Both files include basic class structure and default methods.

---

### 2. Generate a Makefile

To generate a Makefile that automatically includes all `.cpp` files in the current directory and subdirectories:

```bash
python script.py make
```

This will create a Makefile with:

- Build rules for all `.cpp` files
- Color-coded progress bar
- Targets: `all`, `clean`, `fclean`, and `re`

---

## 🧰 Requirements

- Python 3.x
- C++ compiler (`g++` or `clang++`)

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Pull requests are welcome. If you find issues or want to improve functionality, feel free to contribute!

---

## 📬 Contact
Maintained by Anzohs.
