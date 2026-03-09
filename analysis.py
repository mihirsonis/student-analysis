import pandas as pd
import matplotlib.pyplot as plt

# load dataset
data = pd.read_excel("students.xlsx")

print(data.head())

# performance classification
def performance(gpa):
    if gpa >= 2.5:
        return "Good"
    else:
        return "Poor"

data["Performance"] = data["GPA"].apply(performance)

# count students
count = data["Performance"].value_counts()

print(count)

# bar graph
count.plot(kind="bar")
plt.title("Student Performance")
plt.xlabel("Performance")
plt.ylabel("Number of Students")
plt.show()

# pie chart
count.plot(kind="pie", autopct="%1.1f%%")
plt.title("Performance Distribution")
plt.ylabel("")
plt.show()

# GPA distribution
plt.figure()
data["GPA"].plot(kind="hist", bins=10)

plt.title("GPA Distribution")
plt.xlabel("GPA")
plt.ylabel("Number of Students")

plt.show()

# Gender vs GPA
gender_gpa = data.groupby("Gender")["GPA"].mean()

print(gender_gpa)

gender_gpa.plot(kind="bar")

plt.title("Average GPA by Gender")
plt.xlabel("Gender")
plt.ylabel("Average GPA")

plt.show()

# Age distribution
plt.figure()

data["Age"].value_counts().sort_index().plot(kind="bar")

plt.title("Age Distribution of Students")
plt.xlabel("Age")
plt.ylabel("Number of Students")

plt.show()