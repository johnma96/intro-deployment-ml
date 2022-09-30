import logging
from dvc import api
import pandas as pd
from io import StringIO
import sys
import logging

logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
    stream=sys.stderr,
)

logger = logging.getLogger(__name__)

logging.info("Fetching data ...")

# Call data's paths
movie_data_path = api.read("data/raw/movies.csv",
                           remote="data-tracker", encoding="utf8")
finaltial_data_path = api.read(
    "data/raw/finantials.csv", remote="data-tracker", encoding="utf8"
)
opening_data_path = api.read(
    "data/raw/opening_gross.csv", remote="data-tracker", encoding="utf8")

movie_data = pd.read_csv(StringIO(movie_data_path))
fin_data = pd.read_csv(StringIO(finaltial_data_path))
opening_data = pd.read_csv(StringIO(opening_data_path))

# Or you can use
# finantials_path = api.get_url('data/finantials.csv')
# df = pd.read_csv(finantials_path)
# breakpoint() # ~ import pdb; pdb.set_trace()

movie_data.cast_total_facebook_likes = (movie_data.cast_total_facebook_likes
                                        .astype(int))

numeric_cols_mask = (movie_data.dtypes == float) | (movie_data.dtypes == int)
numeric_cols = [
    column for column in numeric_cols_mask.index if numeric_cols_mask[column]
]
movie_data = movie_data[numeric_cols + ["movie_title"]]

fin_data = fin_data[["movie_title", "production_budget", "worldwide_gross"]]

fin_movie_data = pd.merge(fin_data, movie_data, on="movie_title", how="left")

full_movie_data = pd.merge(
    opening_data, fin_movie_data, on="movie_title", how="left")

full_movie_data = full_movie_data.drop(["gross", "movie_title"], axis=1)

full_movie_data.to_csv("data/interim/full_data.csv", index=False)

logger.info("Data Fetched and prepared ...")
