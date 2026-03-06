# Ghana-Disaster-Relief-Distribution-System
Class Exercise given to IB DP 1 students
Flood Relief Operations in Accra
After severe flooding in parts of Accra, a disaster relief organization needs a Python-based system to manage the distribution of food packages to affected families.

You have been hired to develop the system.

The program must register families, calculate relief eligibility, apply priority rules, and generate a final operational report.

Each family provides:

Head of family name

National ID number

Household size

Number of children under 5

Monthly income

Area risk level (low / medium / high)

The organization distributes Food Packages valued at ₵120 each.

 PHASE 1: Registration System

(Types + Indexing + Slicing + Replace + Type Conversion)

Ask for head of family full name.

Convert it to title case.

Remove extra spaces using .replace().

Extract:

First name using slicing

Last 4 digits of National ID using slicing

Generate a Relief ID:


First 2 letters of first name + last 4 of ID + household size

You must use:
String manipulation

Indexing

Slicing

 PHASE 2: Data Entry Loop

(While Loop)

The system must process multiple families.

Continue until the officer types "STOP" as the family name.

For each family collect:

Household size (int)

Children under 5 (int)

Monthly income (float)

Risk level (string)

Convert types properly using int() and float().

 PHASE 3: Eligibility & Allocation Engine

(Comparison + Logical Operators + Augmented Assignment)

Base allocation:

Every household gets 1 package.

Additional packages:

If household size ≥ 5 → +1 package

If children under 5 ≥ 2 → +1 package

If income < 1500 → +1 package

If risk level is "high" → +2 packages

Critical condition:

If income < 800 and risk level is high → +1 emergency package.

Use:

and

or

comparison operators

+=

 PHASE 4: Fraud Detection Rule

(Find + Comparison)

Ask for a referral code.

If the referral code contains "HELP" using .find():

Mark as reviewed case.

If referral code == "HELP2026":

Approve priority processing.

If referral code is empty or incorrect:

Print warning message.

 PHASE 5: Data Tracking

(Lists + Numbers + Augmented Assignment)

You must track:

Total families processed

Total packages distributed

Total estimated cost

Highest allocation

Lowest allocation

Store each family’s package allocation inside a list.

Use:

A for loop for analysis

Augmented assignments

 PHASE 6: Security Validation

(Advanced While Loop)

Before final report generation:

Officer must create a secure password that:

At least 8 characters

Contains at least 1 digit

Contains at least 1 uppercase letter

Contains at least 1 lowercase letter

Use:

.isdigit()

.isupper()

.islower()

A while loop until valid.

PHASE 7: Final Operational Report

(For Loop)

Print:


===== FLOOD RELIEF DISTRIBUTION REPORT =====
Total Families:
Total Packages Distributed:
Total Estimated Cost:
Highest Allocation:
Lowest Allocation:
Average Packages Per Family:

Use a for loop to print each family’s allocation summary.

 Required Concepts Checklist

Students MUST demonstrate:

✔ String type
✔ Integer type
✔ Float type
✔ Indexing
✔ Slicing
✔ Type conversion
✔ .find()
✔ .replace()
✔ Comparison operators
✔ Logical operators (and, or)
✔ if statements
✔ while loop
✔ for loop
✔ Augmented assignment
✔ Lists
