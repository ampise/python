import sys, os, math
os.system("clear")

# data-structure
term_months = [6, 9, 12, 18, 24, 30, 36, 48, 60]
rates = [0.006, 0.0065, 0.013, 0.013, 0.02, 0.02, 0.022, 0.022, 0.025]

# get interest rate based on term
def getRate(term):
    idx_term = term_months.index(term)
    return rates[idx_term]

# calculate compount interest
def calcCompoundInterest(principal, term):
    return principal * (1 + getRate(term)) ** term

# ------- main -------
def main():
    principal = float(sys.argv[1])
    term = int(sys.argv[2])
    interest = "${:,.2f}". format(calcCompoundInterest(principal, term) - principal)
    print("Interest earned on ", "${:,.2f}". format(principal), " = ", interest)


if __name__ == "__main__":
    main()