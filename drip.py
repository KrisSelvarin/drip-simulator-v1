# This is a recreation of etf calculator
# mostly for mastery
# and uses DRIP (Dividend Re-Investment Plan) Simulation
# my original laptop is out of commission


# main
def main():
    greet()
    data_0 = info()
    data_1 = compute(data_0)
    result = data_0 | data_1
    summary(result)

# greet
def greet():
    print("\nDividend Reinvestment Plan\n")


# info of ETF/STOCK
def info():

    # name
    def name_input():
        return input("Stock/ETF name: ").upper()

    # dividend yield
    def div_yield():
        while True:
            try:
                div = round(float(input("Dividend Yield % (Indicated): ")), 2)
                if 0 <= div <= 100:
                    return div
                else:
                    print("Enter values between 0 to 100!\n")
            except ValueError:
                print("Invalid Input!\n")

    # price per share
    def price_ps():
        while True:
            try:
                pps = round(float(input("Price per Share ($): ")), 2)
                if pps > 0:
                    return pps
                else:
                    print("Enter value greater than 0!\n")
            except ValueError:
                print("Invalid Input!\n")

    # frequency dividend pay-out
    def freq_input():
        print("Dividend Pay-out Frequency:")

        f = {
            1 : "Monthly",
            2 : "Quarterly",
            3 : "Semi-Annually",
            4 : "Annually",

        }

        for freq in f:
            print(freq, f[freq], sep=": ")

        while True:
            try:
                sel = int(input("Selection: "))

                x = {1: 12, 2: 4, 3: 2, 4: 1}

                if sel in f:
                    return x[sel], f[sel]
                else:
                    print("Enter value between 1 to 4!\n")
            except ValueError:
                print("Invalid Input!\n")

    # monthly deposit/contribution
    def month_dep():
        while True:
            try:
                dep = round(float(input("Monthly Deposit (₱): ")), 2)
                if dep > 0:
                    return dep
                else:
                    print("Enter value greater than 0!\n")
            except ValueError:
                print("Invalid Input!\n")

    # Investment Years
    def time_input():
        while True:
            try:
                t = int(input("Investment Duration: "))
                if t > 0:
                    return t
                else:
                    print("Enter value greater than 0!\n")
            except ValueError:
                print("Invalid Input!\n")

    # usd conversion
    def usd_conv():
        print("Note: PHP to USD exchange rate is set by default to $1 = ₱57.15")
        return 57.15

    # call functions
    name = name_input()
    d_yield = div_yield()
    pps = price_ps()
    freq, freq_name = freq_input()
    dep = month_dep()
    time = time_input()
    usd = usd_conv()

    # return values
    return {
        "name": name, 
        "d_yield": d_yield, 
        "pps": pps, 
        "freq": freq, 
        "freq_name": freq_name, 
        "dep": dep, 
        "time": time, 
        "usd": usd,

        }


# computations
def compute(data_0):
    print("\nDividend Log: ")

    # convert
    dep_usd = data_0["dep"] / data_0["usd"]
    div_decimal = data_0["d_yield"] / 100

    # constants
    bp_bal= 0
    s_total = 0
    div_sum = 0

    # dividend per share per frequency
    dps = (div_decimal * data_0["pps"]) / data_0["freq"]

    # for year
    for t in range(data_0["time"]):
        # for freq per year
        for i in range(data_0["freq"]):
            # for months per freq
            for j in range(12 // data_0["freq"]):
                bp_bal += dep_usd                                   # adds deposit to buying power
                n_shares = bp_bal / data_0["pps"]                   # fractional shares purchasable by bp
                s_total += n_shares                               # total shares on account
                bp_used = n_shares * data_0["pps"]                  # amount used to buy shares
                bp_bal -= bp_used                                   # remaining balance on buying power
                
                s_total = round(s_total, 6)
                bp_bal = round(bp_bal, 6)

            dividend = dps * s_total                    # amount of dividends receivable per quarter
            bp_bal += dividend                          # dividends added to buyng power
            div_sum += dividend

            # transparency
            print(f"Dividend in Year {t + 1}, Pay-out {i + 1}: ${dividend:,.2f}, Shares: {s_total:.2f}")

        print()
    
    print()

    # return values
    return {"bp_bal": bp_bal, 
            "s_total": s_total, 
            "dividend": dividend, 
            "dep_usd": dep_usd,
            "div_sum": div_sum,
            "total_deposit_usd": data_0["time"] * 12 * dep_usd,
            "total_deposit_php": data_0["time"] * 12 * data_0["dep"],
            
    }


# summary
def summary(result):
    print("Summary:")

    final_value = (result["s_total"] * result["pps"]) + result["bp_bal"]
    roi = (final_value - result["total_deposit_usd"]) / result["total_deposit_usd"]

    print(f""" 
Stock/ETF name:                 {result["name"]}
Dividend Yield:                 {result["d_yield"]}% per annum
Price per Share:                ${result["pps"]}
Monthly Investment:             ${result["dep_usd"]:.2f} | ₱{result["dep"]:,.2f}
Investment Duration:            {result["time"]} years

By the end of {result["time"]} years:
Total Deposits:                 ${result["total_deposit_usd"]:,.2f} | ₱{result["total_deposit_php"]:,.2f}
Total Shares:                   {result["s_total"]:,.2f}
Total Amount of Shares:         ${result["s_total"]*result["pps"]:,.2f} | ₱{result["s_total"]*result["pps"]*result["usd"]:,.2f}
Return on Investment (ROI):     {roi:.2%}

Accumulated Dividend:           ${result["div_sum"]:,.2f} |  ₱{result["div_sum"]*result["usd"]:,.2f}

Note:   This is just an estimated amount as fees and taxes are not computed!

""")



if __name__ == "__main__":
    main()