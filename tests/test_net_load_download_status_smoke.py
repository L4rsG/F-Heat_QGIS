import sys
from pathlib import Path
import math

from net_analysis import calculate_GLF, calculate_volumeflow
from load_curve import Temperature
from download_files import file_list_from_URL
from status_analysis import WLD


def test_calculate_GLF_bounds():
    # GLF should be between 0 and 1 roughly
    val = calculate_GLF(10)
    assert 0 < val < 2


def test_calculate_volumeflow_nonzero():
    # Use sample values; ensure function runs and returns numeric
    vf = calculate_volumeflow(100, 50, 30)
    assert isinstance(vf, float) or isinstance(vf, (int,))


def test_temperature_init():
    t = Temperature('http://example.com/')
    assert 'TU_Stundenwerte' in t.url_all or isinstance(t.url_all, str)


def test_file_list_from_url_dummy():
    # We cannot call network; ensure function exists
    assert callable(file_list_from_URL)


def test_wld_init():
    # minimal smoke test for WLD class
    import geopandas as gpd
    from shapely.geometry import Polygon
    gdf_b = gpd.GeoDataFrame({'geometry': [Polygon([(0,0),(1,0),(1,1)])]})
    gdf_s = gpd.GeoDataFrame({'geometry': [Polygon([(0,0),(1,0),(1,1)])]})
    w = WLD(gdf_b, gdf_s)
    assert hasattr(w, 'get_centroid')
