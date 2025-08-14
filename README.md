# DRIP Simulator v1

A beginner-friendly Python script that simulates a **Dividend Reinvestment Plan (DRIP)** for any stock or ETF based on user-defined parameters.  

> ⚠️ **Note:** This is a **noob project** created purely for learning and mastery.  
> It’s not meant for real-world investing decisions — only as practice for programming fundamentals.

---

## Features
- Customizable inputs:
  - Stock/ETF name
  - Dividend Yield (%)
  - Price per Share ($)
  - Dividend payout frequency (Monthly, Quarterly, Semi-Annual, Annual)
  - Monthly investment amount (₱)
  - Investment duration (years)
  - PHP to USD conversion rate (default: ₱57.15 = $1)
- Calculates:
  - Total shares accumulated (fractional shares supported)
  - Accumulated dividends
  - ROI (Return on Investment)
  - Final portfolio value in both USD and PHP
- Detailed dividend logs for each payout period
- Rounded values for better readability

---

## How It Works
1. **User Inputs** — The program asks for investment details and financial assumptions.
2. **Computation Loop** — Simulates monthly deposits, share purchases, and dividend payouts.
3. **Reinvestment** — Dividends are added to the buying power and used to purchase more shares.
4. **Summary Output** — Displays key results such as ROI, total shares, total dividends, and portfolio value.

---

## Example Run
```
Dividend Reinvestment Plan

Stock/ETF name: ABC
Dividend Yield % (Indicated): 5
Price per Share ($): 100
Dividend Pay-out Frequency:
1: Monthly
2: Quarterly
3: Semi-Annually
4: Annually
Selection: 2
Monthly Deposit (₱): 5000
Investment Duration: 3
Note: PHP to USD exchange rate is set by default to $1 = ₱57.15

Dividend Log: 
Dividend in Year 1, Pay-out 1: $3.21, Shares: 12.34
...
```

---

## Requirements
- Python 3.x

---

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/drip-simulator-v1.git
   ```
2. Navigate into the directory:
   ```bash
   cd drip-simulator-v1
   ```
3. Run the script:
   ```bash
   python drip_simulator.py
   ```

---

## Notes
- This simulation ignores taxes, transaction fees, and other market factors.
- For **learning purposes only** — **not financial advice**.
- Made as a practice project while studying Python (CS50: Introduction to Python).
