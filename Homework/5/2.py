import pandas as pd

with open('example.csv') as f:
    data = pd.read_csv(f)
    jdata = data.to_json()
    sred = data.mean()
    print(sred)

with open('example_json.json', 'w') as file:
    file.write(jdata)

