# NATO Phonetic Alphabet Converter 🎙️

---

## 🔍 Project Overview

Turn any name into its **NATO phonetic alphabet** form using a CSV data source. This helps with clear verbal communication, especially over noisy channels like radio or phone.

---

## 🚦 How It Works

- Reads the mapping of letters to NATO code words from a CSV file.
- Converts user input (a name) into uppercase automatically.
- Translates each letter of the input to its corresponding phonetic code.

Example:

Input: "Alice"
Output: ["ALFA", "LIMA", "INDIA", "CHARLIE", "ECHO"]

---

## ⚙️ Setup Instructions

1. Place `nato_phonetic_alphabet.csv` in the same folder as this script.
2. Run the script with Python 3.6+.
3. Provide a name when prompted.
4. See the phonetic output!

---

## 🗃️ CSV Format Example

| letter | code   |
|--------|--------|
| A      | ALFA   |
| B      | BRAVO  |
| C      | CHARLIE|
| ...    | ...    |

---

## 💡 Tips & Notes

- Install pandas if missing:
- Make sure the CSV includes all alphabets (A-Z) in uppercase letters.
- Handle invalid letters with try-except (optional extension).

---

## ❤️ Contributing

Pull requests and issues are welcome! Improve or extend the script freely.

---

## 📄 License

MIT License. Refer to [LICENSE](LICENSE) for details.

---

> **Pro Tip:** Using the NATO phonetic alphabet enhances clarity in all verbal communication!  



