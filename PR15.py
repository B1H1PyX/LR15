import pandas as pd
cars_dict = {
    'Horsepower (HP)': ['100', '120', '110', '140', '150'],
    'Cost ($)': ['200', '300', '250', '400', '450']
    }
cd = pd.DataFrame(cars_dict)
print("Before aggregation:")
print(cd)
cd['Horsepower (HP)'] = pd.to_numeric(cd['Horsepower (HP)'])
cd['Cost ($)'] = pd.to_numeric(cd['Cost ($)'])
ad = cd.aggregate({
    'Horsepower (HP)': 'mean',
    'Cost ($)': 'sum'
    }).transpose()
print("\nAfter aggregation")
print(ad)