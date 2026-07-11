# Security Risk Level Calculator

likelihood = int(input("Likelihood (1-5): "))
impact = int(input("Impact (1-5): "))

risk = likelihood * impact

print("Risk Score:", risk)

if risk <= 5:
    print("Risk Level: Low")
elif risk <= 14:
    print("Risk Level: Medium")
else:
    print("Risk Level: High")
