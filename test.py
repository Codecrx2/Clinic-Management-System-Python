import pandas as pd
from matplotlib import pyplot as plt

v = pd.read_csv('Patients_main.csv')


print(v)



f = v.groupby('Gender')['Gender'].size()

print(f)


f.plot(kind = 'bar' , x = f.index , y = f)
plt.show()
