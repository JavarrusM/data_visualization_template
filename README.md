# TEMPLATES

## Adding content for checks


```python
import pandas as pd
import matplotlib.pyplot as plt

# Let's create a sample dataframe
data = {
    "name": ["John", "Jane", "Jim", "Janet"],
    "age": [25, 30, 35, 40],
    "location": ["New York", "Chicago", "Los Angeles", "Miami"],
}
df = pd.DataFrame(data)

# Now let's print out the dataframe
display(df)

# Create the plot
plt.bar(df['name'], df['age'])
plt.title('Age by Name')
plt.xlabel('Name')
plt.ylabel('Age')

# Save the plot as a PNG image file
plt.savefig('age_by_name_plot.png', dpi=300, bbox_inches='tight')

# Show the plot
plt.show()

```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>age</th>
      <th>location</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>John</td>
      <td>25</td>
      <td>New York</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Jane</td>
      <td>30</td>
      <td>Chicago</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Jim</td>
      <td>35</td>
      <td>Los Angeles</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Janet</td>
      <td>40</td>
      <td>Miami</td>
    </tr>
  </tbody>
</table>
</div>



    
![png](output_2_1.png)
    



```python

```
