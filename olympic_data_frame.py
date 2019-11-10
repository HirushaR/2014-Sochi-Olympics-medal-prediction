import pandas as pd
import numpy as np

contries = ['Russia Fed.', 'Norway', 'Canada', 'United States', 'Netherlands', 'Germany',
            'Switzerland', 'Belarus', 'Austria', 'France', 'Poland', 'Chine', 'Korea',
            'Sweden', 'Czech Republic', 'Slvenia', 'Japan', 'Finland', 'Great Britian', 'Ukrain',
            'Slovakia', 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan'] # 26

Gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0] # 26
Silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
Bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

d = {'Country_name' : pd.Series(contries), 'Gold': pd.Series(Gold), 'Silver': pd.Series(Silver), 'Bronze': pd.Series(Bronze)}

df = pd.DataFrame(d)
# c = df[df['Gold'] >= 1]
# #weathe vale is 1 or greate than one
# e = [df['Gold'].map(lambda x: x >= 1)]
# print(e)

#show the Bronze medals atleast have one gold
brnz_one_gold =df['Bronze'][df['Gold'] >= 1]
avg = np.mean(brnz_one_gold)
print(avg)

