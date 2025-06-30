# **Demo Shop Automated Tests (Practice Project)**

This repository contains **automated tests** for a **Demo Shop web application**. These tests utilize the **Page Object Pattern**, **Selenium WebDriver**, and **pytest** for creating clean, maintainable UI tests in Python.

---

## **Overview**

### **Page Object Pattern**
Each page or screen of the Demo Shop is represented by a **separate class** (a "page object").  
This approach provides the following benefits:

- **Organized**: Page-specific locators and actions are separated from test logic.
- **Maintainable**: If changes occur in the UI, only the respective page's class needs an update.

---

### **Selenium WebDriver**
Selenium WebDriver enables **browser automation**. Here's what it's used for:

- **Locating elements**: (e.g., buttons, forms) via CSS or XPath.
- **Performing actions**: Includes clicking, typing text, and waiting for elements.

---

### **pytest**
pytest is a **Python testing framework** that offers the following functionality:

- Automatically **collects and runs test functions**.
- Provides **fixtures** (e.g., for setup and teardown processes).
- Generates **readable test results and reports**.

---