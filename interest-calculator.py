import sys, os, math
os.system("clear")

# data-structure
term_months = [6, 9, 12, 18, 24, 30, 36, 48, 60]
rates = [0.006, 0.0065, 0.013, 0.013, 0.02, 0.02, 0.022, 0.022, 0.025]

# get interest rate based on term
def getRate(term):
    try:
        idx_term = term_months.index(term)
        print("Interest rate for ", term, " months = ", "{:,.2f}%".format(rates[idx_term]*100))
        return rates[idx_term]
    except:
        print("Invalid term")
        return 0

# calculate compount interest
def calcCompoundInterest(principal, term):
    return principal * (1 + getRate(term)) ** (term/12)

# ------- main -------
def main():
    principal = float(sys.argv[1])
    term = int(sys.argv[2])
    interest = "${:,.2f}". format(calcCompoundInterest(principal, term) - principal)
    print("Interest earned on ", "${:,.2f}".format(principal), " = ", interest)


if __name__ == "__main__":
    main()