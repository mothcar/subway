import pandas as pd
import numpy as np
import pyproj
import folium
from json import JSONEncoder
import json

with open('line2.csv') as f:
    print(f)

df = pd.read_csv("./line2.csv",
                 encoding='UTF-8',
                 usecols=['X','Y'])

df['X'] = pd.to_numeric(df['X'], errors="coerce")
df['Y'] = pd.to_numeric(df['Y'], errors="coerce")

df = df.dropna()
df.index=range(len(df))
df.tail()
print(df.tail())

def project_array(coord, p1_type, p2_type):
    """
    좌표계 변환 함수
    - coord: x, y 좌표 정보가 담긴 NumPy Array
    - p1_type: 입력 좌표계 정보 ex) epsg:5179
    - p2_type: 출력 좌표계 정보 ex) epsg:4326
    """
    p1 = pyproj.Proj(init=p1_type)
    p2 = pyproj.Proj(init=p2_type)
    fx, fy = pyproj.transform(p1, p2, coord[:, 0], coord[:, 1])
    return np.dstack([fy, fx])[0]

# DataFrame -> NumPy Array 변환
coord = np.array(df)
# print(coord)

# 좌표계 정보 설정
p1_type = "epsg:5181"
p2_type = "epsg:4326"

# project_array() 함수 실행
result = project_array(coord, p1_type, p2_type)
print(type(result))
# convert array into dataframe
DF = pd.DataFrame(result)
# save the dataframe as a csv file
# DF.to_csv("test.csv")
class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)
# Serialization
print("serialize NumPy array into JSON and write into a file")
with open("test.json", "w") as write_file:
    json.dump(result, write_file, cls=NumpyArrayEncoder)
print("Done writing serialized NumPy array into file")