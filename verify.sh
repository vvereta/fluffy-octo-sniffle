#! /bin/bash
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
pytest --cov=fluffy --cov-branch \
       --cov-report=html:pytest_coverage \
       --cov-config=.coveragerc \
       --html=pytest_result.html --self-contained-html \
       --cache-clear
