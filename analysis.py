import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Math": [80, 70, 90, 60, 85],
    "Science": [75, 65, 95, 55, 80],
    "English": [85, 60, 88, 70, 75]
}

df = pd.DataFrame(data)
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)
top_student = df.loc[df["Average"].idxmax()]
print("Top Student:\n", top_student)
df.plot(x="Name", y=["Math", "Science", "English"], kind="bar")
plt.title("Student Performance")
plt.show()