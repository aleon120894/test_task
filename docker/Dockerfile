FROM python:3.9.6
WORKDIR ./tests
RUN pip install pytest
RUN pip install pytest-fixtures
RUN pip install pytest-remotedata
CMD ["pytest", "preview" , "tests/", "-m",  "preview"]
RUN pytest tests/test_scenario.py

