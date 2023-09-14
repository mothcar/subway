import gc
import glob
import geopandas as gpd

# SHAPE 파일 경로 리스트
file_path = glob.glob("./555.zip")[0]

# Shape 파일을 GeoDataFrame으로 불러오기
gdf = gpd.GeoDataFrame.from_file(file_path, encoding='UTF-8')

# 경위도 좌표계 설정
gdf = gdf.to_crs({"init": "epsg:4326"})

# 데이터 정보
gdf.info()

# 데이터 예시
gdf.tail()

# CSV로 저장할 파일명
new_file_name = "sample.csv"

# GeoDataFrame을 CSV 파일로 저장
gdf.to_csv(f"./{new_file_name}", encoding='utf8', index=False)

# 메모리 정리
del gdf
gc.collect()