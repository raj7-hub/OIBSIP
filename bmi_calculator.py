# Beginner BMI Calculator - Command Line Version

def calculate_bmi(weight, height):
    """Calculate BMI using formula: weight / height^2"""
    return weight / (height ** 2)

def classify_bmi(bmi):
    """Classify BMI into categories"""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    try:
        # Take user input
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        # Validate input
        if weight <= 0 or height <= 0:
            print("❌ Weight and height must be positive numbers.")
            return

        # Calculate BMI
        bmi = calculate_bmi(weight, height)

        # Classify BMI
        category = classify_bmi(bmi)

        # Display result
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Category: {category}")

    except ValueError:
        print("❌ Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    main()
