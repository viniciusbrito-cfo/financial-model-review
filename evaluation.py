def calculate_fcf(revenue, ebitda_margin, tax_rate, capex_percent):
    ebitda = revenue * ebitda_margin
    tax = ebitda * tax_rate
    capex = revenue * capex_percent
    
    fcf = ebitda - tax - capex
    
    return fcf


def validate_fcf(provided_fcf, revenue, ebitda_margin, tax_rate, capex_percent):
    expected_fcf = calculate_fcf(revenue, ebitda_margin, tax_rate, capex_percent)
    
    if abs(provided_fcf - expected_fcf) < 0.01:
        return "Valid"
    else:
        return "Invalid"


# Data model
revenue = 1000
ebitda_margin = 0.2
tax_rate = 0.25
capex_percent = 0.1

# Simulation of value coming from outside (AI, person, system)
provided_fcf = 51  # External value to be validated

print("Expected FCF:", calculate_fcf(revenue, ebitda_margin, tax_rate, capex_percent))
print("Provided FCF:", provided_fcf)
print("Validation:", validate_fcf(provided_fcf, revenue, ebitda_margin, tax_rate, capex_percent))
