# etf-calculator
DRIP Simulation in PYTHON

# 📈 ETF Dividend Reinvestment Calculator (DRIP Simulator)

A simple command-line Python project that simulates the growth of your investment in an ETF or dividend-paying stock using the **Dividend Reinvestment Plan (DRIP)** strategy. Built for learning purposes and personal use.

---

## 🔧 Features

* Accepts user input for key investment parameters:

  * ETF/Stock name
  * Dividend yield (annual, in %)
  * Price per share (in USD)
  * Monthly deposit (in PHP)
  * Investment duration (in years)
  * Dividend pay-out frequency: Monthly, Quarterly, Semi-Annually, or Annually
* Simulates monthly deposits and fractional share purchases
* Reinvests all received dividends
* Tracks total shares, dividends, deposits, and portfolio growth over time
* Displays a clear summary and dividend log

---

## 📦 Sample Input

```
Stock/ETF name: VOO
Dividend Yield % (Indicated): 1.7
Price per Share ($): 420.50
Dividend Pay-out Frequency:
1: Monthly
2: Quarterly
3: Semi-Annually
4: Annually
Selection: 2
Monthly Deposit (₱): 5000
Investment Duration: 10
Note: PHP to USD exchange rate is set by default to $1 = ₱57.15
```

---

## 💡 Output

* Dividend log per period (based on selected frequency)
* Final portfolio summary:

  * Total shares
  * Total value
  * Total dividends earned
  * Total deposits made (USD & PHP)
  * ROI (Return on Investment)

---

## ✅ Example Output

```
Summary:

Stock/ETF name:              VOO
Dividend Yield:              1.7% per annum
Price per Share:             $420.50
Monthly Investment:          $87.45 | ₱5000.00
Investment Duration:         10 years

By the end of 10 years:
Total Deposits:              $10,494.00 | ₱599,000.00
Total Shares:                25.35
Total Amount of Shares:      $10,656.68 | ₱609,537.84
Return on Investment (ROI):  1.55%

Accumulated Dividend:        $1,453.82 | ₱83,165.33

Note: This is just an estimated amount as fees and taxes are not computed!
```

---

## 📘 Notes

* Built using pure Python, no external libraries required.
* Exchange rate is fixed at 1 USD = 57.15 PHP (can be adjusted in the code).
* No real-time data fetching — all inputs are manually provided.

---

## 🧠 Author's Intent

This project was created for **learning and mastery**, especially to reinforce concepts from [Harvard's CS50: Introduction to Python](https://cs50.harvard.edu/python/). It serves as a personal practice exercise and a way to apply programming skills to something practical: investing.

---

## 🚀 Future Plans (for when I'm ready)

* Add support for frequency-based contributions (monthly/quarterly/annual)
* Add fee/tax estimation toggle
* Refactor to use classes (OOP)
* Optional export to CSV
* Web version (Flask or Streamlit)

---

## 🧑‍💻 License

MIT License — feel free to use, fork, and modify.

---

## 📅 Started

Week 1 of learning Python — no prior programming experience.
