import os
from django.contrib.gis.utils import LayerMapping
from .models import Countries


countries_mapping = {
    'country_type': 'TYPE',
    'name': 'NAME_LONG',
    'abbrev': 'ABBREV',
    'formal_name': 'FORMAL_EN',
    'pop_est': 'POP_EST',
    'gdp_md_est': 'GDP_MD_EST',
    'pop_year': 'POP_YEAR',
    'lastcensus': 'LASTCENSUS',
    'gdp_year': 'GDP_YEAR',
    'continent': 'CONTINENT',
    'region_un': 'REGION_UN',
    'region_wb': 'REGION_WB',
    'geom': 'MULTIPOLYGON',
}

countries_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/ne_10m_admin_0_countries.shp'))

def run():
    lm = LayerMapping(Countries,countries_shp,countries_mapping,transform=4326)
    lm.save(strict=True,verbose=True)
