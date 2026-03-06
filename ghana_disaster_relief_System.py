name = input("Enter the full name of the family head: ").strip().title()

print("Please enter Ghana Card separated by -")
id_number = input("Enter Ghana Card: ")

household_size = int(input("Household size: "))

children = int(
    input("How many children are under the age of 5 in the house? "))

monthly_income = int(input("What is the monthly income of the family? "))

risk_factor = input("Type the level of risk - low/medium/high: ").lower()

relief_id = name[:2] + id_number[-4:] + str(household_size)

print(f"Hi {name}, kindly take note of your relief id for all your processing: {relief_id}")

# Data tracking
total_packages = 0
families = 0
allocations = []

while name.lower() != "stop":

    families += 1

    package = 1   # Base package

    # Allocation rules
    if household_size >= 5:
        package += 1

    if children >= 2:
        package += 1

    if monthly_income < 1500:
        package += 1

    if risk_factor == "high":
        package += 2

    if risk_factor == "high" and monthly_income < 800:
        package += 1

    # Referral code
    referral_request = input(
        "Kindly enter your code (or press enter to skip): ").strip().lower()

    if referral_request.find("help") != -1:
        print("Reviewed case")

    if referral_request == "help2026":
        print("Approved priority processing")
        package += 1

    if referral_request == "":
        print("Warning: No referral code provided")

    print("Packages allocated:", package)

    allocations.append(package)
    total_packages += package

    # Next family
    name = input(
        "\nEnter next family name (or type STOP to finish): ").strip().title()

    if name.lower() != "stop":
        id_number = input("Enter Ghana Card: ")
        household_size = int(input("Household size: "))
        children = int(input("Children under 5: "))
        monthly_income = int(input("Monthly income: "))
        risk_factor = input("Risk level (low/medium/high): ").lower()

# Final report
print("\n===== RELIEF DISTRIBUTION REPORT =====")
print("Total families processed:", families)
print("Total packages distributed:", total_packages)

for i in range(len(allocations)):
    print(f"Family {i+1}: {allocations[i]} packages")
