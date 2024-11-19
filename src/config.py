import os

from dotenv import load_dotenv
from src.feature_config import FeatureGroupConfig, FeatureViewConfig

from src.paths import PARENT_DIR

# load key-value pairs from .env file located in the parent directory
load_dotenv(PARENT_DIR / '.env')

HOPSWORKS_PROJECT_NAME = 'prediction'

try:
    # HOPSWORKS_PROJECT_NAME = os.environ['HOPSWORKS_PROJECT_NAME']
    HOPSWORKS_API_KEY = os.environ['HOPSWORKS_API_KEY']
except:
    raise Exception(
        'Create an .env file on the project root with the HOPSWORKS_API_KEY'
    )

#####################################################################################################################

# TODO: remove FEATURE_GROUP_NAME and FEATURE_GROUP_VERSION, and use FEATURE_GROUP_METADATA instead
FEATURE_GROUP_NAME = 'time_series_hourly_feature_group'
FEATURE_GROUP_VERSION = 1

FEATURE_GROUP_METADATA = FeatureGroupConfig(
    name=FEATURE_GROUP_NAME,
    version=FEATURE_GROUP_VERSION,
    description='Feature group with hourly time-series data of historical taxi rides',
    primary_key=['pickup_location_id', 'pickup_ts'],
    event_time='pickup_ts',
    online_enabled=True,
)

#####################################################################################################################

# TODO: remove FEATURE_VIEW_NAME and FEATURE_VIEW_VERSION, and use FEATURE_VIEW_METADATA instead
FEATURE_VIEW_NAME = 'time_series_hourly_feature_view'
FEATURE_VIEW_VERSION = 1

FEATURE_VIEW_METADATA = FeatureViewConfig(
    name=FEATURE_VIEW_NAME,
    version=FEATURE_VIEW_VERSION,
    feature_group=FEATURE_GROUP_METADATA,
)

#####################################################################################################################

MONITORING_FV_NAME = 'monitoring_feature_view'
MONITORING_FV_VERSION = 1


#####################################################################################################################

MODEL_NAME = 'taxi_demand_predictor_next_hour'
MODEL_VERSION = 1

# number of historical values our model needs to generate predictions
N_FEATURES = 24 * 28

# number of iterations we want Optuna to pefrom to find the best hyperparameters
N_HYPERPARAMETER_SEARCH_TRIALS = 15

# maximum Mean Absolute Error we allow our production model to have
MAX_MAE = 45.0