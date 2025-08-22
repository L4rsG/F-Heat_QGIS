import sys
from pathlib import Path

from building_parameters_loader import load_building_parameters, get_values_as_dict


def test_load_building_parameters_exists():
    params = load_building_parameters()
    assert params is not None
    # should contain EFH and MFH as defined in the JSON
    keys = [k.lower() for k in params.building_types.keys()]
    assert 'efh' in keys or 'efh' in params.building_types
    assert 'mfh' in keys or 'mfh' in params.building_types


def test_get_values_by_year_efh_1980():
    params = load_building_parameters()
    vals = get_values_as_dict(params, 'EFH', construction_year=1980)
    assert vals is not None
    # For EFH 1971_1990 we expect room_heating 140, hot_water 25, total 165
    assert vals['room_heating_kWh_m2a'] == 140
    assert vals['hot_water_kWh_m2a'] == 25
    assert vals['total_kWh_m2a'] == 165


def test_get_values_by_age_key_mfh_recent():
    params = load_building_parameters()
    # explicit age key lookup
    vals = get_values_as_dict(params, 'MFH', age_key='2011_2025')
    assert vals is not None
    assert vals['room_heating_kWh_m2a'] == 50
    assert vals['hot_water_kWh_m2a'] == 15
    assert vals['total_kWh_m2a'] == 65


def test_get_values_unknown_type_returns_none():
    params = load_building_parameters()
    vals = get_values_as_dict(params, 'UNKNOWN_TYPE', construction_year=1990)
    assert vals is None
