# **Task 3**

---

## 🌟 **PART A — Research Questions (Short Answers)**

### **1. What new improvements were introduced in Gemini 3.0?**

Gemini 3.0 introduced a more powerful model architecture with improved reasoning, faster performance, enhanced context handling, and better code generation. It also provides higher accuracy in long conversations and more stable outputs.

---

### **2. How does Gemini 3.0 improve coding & automation workflows?**

Gemini 3.0 provides more accurate code suggestions, better debugging help, and improved tool-calling for automation. It integrates smoothly with CLI workflows and supports structured outputs, making scripting and automation faster and more reliable.

---

### **3. How does Gemini 3.0 improve multimodal understanding?**

Gemini 3.0 can analyze images, PDFs, screenshots, charts, and videos with higher accuracy. It offers improved OCR, better visual reasoning, and stronger understanding of mixed modal inputs (text + images), resulting in more accurate responses.

---

### **4. Name any two developer tools introduced with Gemini 3.0.**

* **Gemini CLI 3.0**
* **Gemini Code Assist**

(Other acceptable answers: Vertex AI Studio updates, Gemini API Explorer, Function Calling tools, etc.)

---

## 🌟 **PART B — Practical Task (Screenshot Required)**

### **Update the Gemini Model to Version 3.0 Using CLI**

### ✅ **Step 1 — Check Installed Models**

```sh
gemini model list
```

### ✅ **Step 2 — Update Gemini Model to 3.0**

```sh
gemini model upgrade gemini-3.0
```

**or (depending on CLI version):**

```sh
gemini models update gemini-3.0
```

### ✅ **Step 3 — Confirm the Update**

```sh
gemini model info gemini-3.0
```

### 🔹 Output (Screenshot):

![CLI Screenshot](model-list-output.png)

---
