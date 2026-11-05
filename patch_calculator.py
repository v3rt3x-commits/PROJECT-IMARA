# PROJECT IMARA - PATCH ANTENNA CALCULATOR
import math
c = 3e8
# 1. Calculate patch width
def calculate_width(frequency, epsilon_r):
    W = (c / (2 * frequency)) * ((2 / (epsilon_r + 1)) ** 0.5)
    return W
# 2. Calculate effective dielectric constant
def calculate_epsilon_eff(epsilon_r, h, W):
    epsilon_eff = ((epsilon_r + 1) / 2) + ((epsilon_r - 1) / 2) * (
        (1 + (12 * h / W)) ** -0.5
    )
    return epsilon_eff
# 3. Calculate fringing length extension
def calculate_delta_L(epsilon_eff, W, h):
    delta_L = 0.412 * h * (
        ((epsilon_eff + 0.3) * ((W / h) + 0.264)) /
        ((epsilon_eff - 0.258) * ((W / h) + 0.8))
    )
    return delta_L
# 4. Calculate effective patch length
def calculate_effective_length(c, frequency, epsilon_eff):
    L_eff = c / (2 * frequency * (epsilon_eff ** 0.5))
    return L_eff
# 5. Calculate actual physical patch length
def calculate_actual_length(L_eff, delta_L):
    L = L_eff - (2 * delta_L)
    return L
# 6. Calculate inset depth for microstrip feed
def calculate_inset_depth(L, R_edge, Z0=50):
    y0 = (L / math.pi) * math.acos(math.sqrt(Z0 / R_edge))
    return y0
# 7. Calculate microstrip line impedance
def calculate_line_impedance(epsilon_r, u):
    epsilon_eff_line = ((epsilon_r + 1) / 2) + (
        (epsilon_r - 1) / 2
    ) * ((1 + (12 / u)) ** -0.5)

    if u < 1:
        epsilon_eff_line += 0.04 * ((1 - u) ** 2)

    if u <= 1:
        Z = (60 / (epsilon_eff_line ** 0.5)) * math.log(
            (8 / u) + (u / 4)
        )
    else:
        Z = (120 * math.pi) / (
            (epsilon_eff_line ** 0.5) *
            (u + 1.393 + 0.667 * math.log(u + 1.444))
        )
    return Z, epsilon_eff_line
# 8. Calculate microstrip feed-line width
def calculate_feedline_width(epsilon_r, h, Z0=50):
    low = 0.01
    high = 100

    for _ in range(100):
        u = (low + high) / 2
        calculated_Z, _ = calculate_line_impedance(epsilon_r, u)

        if calculated_Z > Z0:
            low = u
        else:
            high = u

    width = u * h
    return width
# 9. Calculate quarter wavelength for the feedline 
def calculate_quarter_wavelength(frequency, epsilon_eff_line):
    length = c / (
        4 * frequency * (epsilon_eff_line ** 0.5)
    )
    return length
# 10. Calculate phase length for the feedline
def calculate_phase_length(frequency, epsilon_eff_line, phase_degrees):
    guided_wavelength = c / (
        frequency * (epsilon_eff_line ** 0.5)
    )
    length = guided_wavelength * (phase_degrees / 360)
    return length
# 11. Calculate inset notch width
def calculate_notch_width(feedline_width, gap):
    notch_width = feedline_width + (2 * gap)
    return notch_width
# 12. Validate basic antenna geometry
def validate_design(W, L, y0, notch_width, feedline_width, butler_width):
    errors = []
    if W <= 0:
        errors.append("Patch width is invalid.")
    if L <= 0:
        errors.append("Actual patch length is invalid.")
    if not (0 < y0 < L / 2):
        errors.append("Inset feed depth is outside the valid range.")
    if notch_width <= 0 or notch_width >= W:
        errors.append("Notch width is invalid for the patch.")
    if feedline_width <= 0:
        errors.append("50-ohm feed-line width is invalid.")
    if butler_width <= 0:
        errors.append("Butler Matrix line width is invalid.")
    return errors
# 13. Loop to get valid user input for frequency, dielectric constant, and substrate thickness
def get_valid_number(prompt, minimum):
    while True:
        try:
            value = float(input(prompt))

            if math.isfinite(value) and value > minimum:
                return value
            else:
                print(f"Enter a finite number greater than {minimum}.")
        except ValueError:
            print("Invalid input! Please enter a number.")

# MAIN PROGRAM
print("PROJECT IMARA - PATCH ANTENNA CALCULATOR")
print("----------------------------------------")

frequency = get_valid_number(
    "Enter operating frequency in GHz: ", 0
) * 1e9
R_edge = get_valid_number(
    "Enter patch edge resistance from simulation (ohms): ", 50
)
epsilon_r = get_valid_number(
    "Enter dielectric constant: ", 1
)

h = get_valid_number(
    "Enter substrate thickness in mm: ", 0
) / 1000
gap = get_valid_number(
    "Enter notch clearance on each side in mm: ", 0
) / 1000
# Validate inputs
if frequency <= 0 or epsilon_r <= 1 or h <= 0:
    print("Invalid antenna specifications!")
    exit()

# Perform calculations by calling functions
W = calculate_width(frequency, epsilon_r)
epsilon_eff = calculate_epsilon_eff(epsilon_r, h, W)
delta_L = calculate_delta_L(epsilon_eff, W, h)
L_eff = calculate_effective_length(c, frequency, epsilon_eff)
L = calculate_actual_length(L_eff, delta_L)
y0 = calculate_inset_depth(L, R_edge)
# 50-ohm standard feed line
feedline_width = calculate_feedline_width(epsilon_r, h, 50)
feedline_width_mm = feedline_width * 1000
# 35.35-ohm Butler Matrix line
butler_width = calculate_feedline_width(epsilon_r, h, 35.35)
butler_width_mm = butler_width * 1000
notch_width = calculate_notch_width(feedline_width, gap)
notch_width_mm = notch_width * 1000
_, epsilon_eff_50 = calculate_line_impedance(
    epsilon_r, feedline_width / h
)
phase_length_45 = calculate_phase_length(
    frequency, epsilon_eff_50, 45
)
phase_length_90 = calculate_phase_length(
    frequency, epsilon_eff_50, 90
)
phase_length_90_mm = phase_length_90 * 1000
phase_length_45_mm = phase_length_45 * 1000
_, epsilon_eff_35 = calculate_line_impedance(
    epsilon_r, butler_width / h
)
# 45-degree phase length for 35.35-ohm line
phase_length_45_35 = calculate_phase_length(
    frequency, epsilon_eff_35, 45
)
# 90-degree phase length for 35.35-ohm line
phase_length_90_35 = calculate_phase_length(
    frequency, epsilon_eff_35, 90
)
length_50 = calculate_quarter_wavelength(
    frequency, epsilon_eff_50
)
length_35 = calculate_quarter_wavelength(
    frequency, epsilon_eff_35
)
errors = validate_design(
    W, L, y0, notch_width, feedline_width, butler_width
)
if errors:
    print("\nDESIGN VALIDATION WARNINGS")
    for error in errors:
        print("-", error)
else:
    print("\nDESIGN VALIDATION: PASSED")
# Convert results into millimetres
W_mm = W * 1000
delta_L_mm = delta_L * 1000
L_eff_mm = L_eff * 1000
L_mm = L * 1000
y0_mm = y0 * 1000
length_50_mm = length_50 * 1000
length_35_mm = length_35 * 1000
phase_length_45_35_mm = phase_length_45_35 * 1000
phase_length_90_35_mm = phase_length_90_35 * 1000
# Display results
print("\nANTENNA CALCULATION RESULTS")
print("----------------------------------------")
print("Operating Frequency:", frequency / 1e9, "GHz")
print("Dielectric Constant:", epsilon_r)
print("Substrate Thickness:", h * 1000, "mm")
print("Patch Width:", round(W_mm, 3), "mm")
print("Effective Dielectric Constant:", round(epsilon_eff, 3))
print("Fringing Length Extension:", round(delta_L_mm, 3), "mm")
print("Effective Patch Length:", round(L_eff_mm, 3), "mm")
print("Actual Patch Length:", round(L_mm, 3), "mm")
print("Patch Edge Resistance:", R_edge, "ohms")
print("Inset Feed Depth:", round(y0_mm, 3), "mm")
print("50-ohm Feed-line Width:", round(feedline_width_mm, 3), "mm")
print("35.35-ohm Butler Matrix Line Width:", round(butler_width_mm, 3), "mm")
print("Notch Clearance (each side):", round(gap * 1000, 3), "mm")
print("Total Inset Notch Width:", round(notch_width_mm, 3), "mm")
print("Quarter-Wavelength (50-ohm):", round(length_50_mm, 3), "mm")
print("Quarter-Wavelength (35.35-ohm):", round(length_35_mm, 3), "mm")
print("45-degree Phase-shifter Length (50-ohm):",
      round(phase_length_45_mm, 3), "mm")
print("90-degree Phase-shifter Length (50-ohm):",
      round(phase_length_90_mm, 3), "mm")
print("45-degree Phase Length (35.35-ohm):",
      round(phase_length_45_35_mm, 3), "mm")
print("90-degree Phase Length (35.35-ohm):",
      round(phase_length_90_35_mm, 3), "mm")
print("\nENGINEERING NOTES")
print("----------------------------------------")
print("1. These dimensions are preliminary calculations.")
print("2. Verify antenna performance using electromagnetic simulation.")
print("3. Confirm substrate specifications before fabrication.")
print("4. Obtain patch edge resistance from antenna simulation.")
print("5. Confirm Butler Matrix topology before using its line dimensions.")
print("----------------------------------------")