#!/usr/bin/env -S python3 -X utf8
import os
import sys
from pathlib import Path
import traceback
from psycopg2.extensions import AsIs

from src.init_data import load_config, get_db_connect
from script.migration_text_wrapper import migration_wrapper

CI_COMMIT_SHA = os.environ.get('CI_COMMIT_SHA')
MIGRATION_FUNC_FILE_PATH = f'{Path(__file__).parent.absolute()}/script/migration_text_wrapper.py'
PRE_DEPLOY_TABLE_NAME = 'pre_deploy'


def main() -> int:
    priny(MIGRATION_FUNC_FILE_PATH)


if __name__ == '__main__':
    sys.exit(main())

