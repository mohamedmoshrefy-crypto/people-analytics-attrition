import pandas as pd

# Load synthetic HR dataset
data = {
    "Employee_ID": ["E1", "E2", "E3", "E4", "E5", "E6"],
    "Department": ["Sales", "HR", "IT", "IT", "Sales", "HR"],
    "Overtime": ["Yes", "No", "Yes", "No", "Yes", "No"],
    "Satisfaction_Score": [2, 4, 1, 5, 2, 4],
    "Attrition": ["Yes", "No", "Yes", "No", "Yes", "No"]
}

df = pd.DataFrame(data)

# Calculate Attrition Rate by Department
attrition_rate = df.groupby("Department")["Attrition"].apply(lambda x: (x == "Yes").mean() * 100)

print("--- Attrition Rate by Department (%) ---")
print(attrition_rate)
