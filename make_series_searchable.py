from models import Issue
from app import app
import time


def create_txt_file_of_all_series_names():
    issues = Issue.query.all()

    for issue in issues:
        series_id = issue.series_id
        series_name = issue.series
        time.sleep(0.01)

        with open(f'series_names/series_names_files/{series_id}.txt', 'w+') as f:
            f.write(series_name)
            f.write('\n')


create_txt_file_of_all_series_names()