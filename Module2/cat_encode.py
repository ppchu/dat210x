import pandas as pd 

df = pd.DataFrame({'vertebrates':[
	'Bird',
	'Bird',
	'Mammal',
	'Fish',
	'Amphibian',
	'Reptile',
	'Mammal',
]})

print df

df = pd.get_dummies(df, columns=['vertebrates'])

print df