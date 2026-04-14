def calculate_fcf(revenue, ebitda_margin, tax_rate, capex_percent):
    ebitda = revenue * ebitda_margin
    tax = ebitda * tax_rate
    capex = revenue * capex_percent
    
    fcf = ebitda - tax - capex
    
    return fcf


def validate_fcf(fcf, revenue, ebitda_margin, tax_rate, capex_percent):
    expected_fcf = calculate_fcf(revenue, ebitda_margin, tax_rate, capex_percent)
    
    if abs(fcf - expected_fcf) < 0.01:
        return "Valid"
    else:
        return "Invalid"


# Example
revenue = 1000
ebitda_margin = 0.2
tax_rate = 0.25
capex_percent = 0.1

fcf = calculate_fcf(revenue, ebitda_margin, tax_rate, capex_percent)

print("FCF:", fcf)
print("Validation:", validate_fcf(fcf, revenue, ebitda_margin, tax_rate, capex_percent))
