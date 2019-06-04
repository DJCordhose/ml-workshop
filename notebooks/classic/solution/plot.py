# Change our pairplot to
# * plot more samples
# * reduce the number of variables to the first three (leave out the group)
# * make the plot a bit larger

# Optional
# * fit linear regression models to the scatter plots
# * give each group a different type of marker, use https://matplotlib.org/api/markers_api.html as a reference

sample_df = df.sample(n=300, random_state=42)
sns.set(font_scale=2)
sns.pairplot(sample_df, hue="group", palette={0: '#AA4444', 1: '#006000', 2: '#EEEE44'}, 
             vars=['speed', 'age', 'miles'], height=5, markers=["o", "s", "D"])