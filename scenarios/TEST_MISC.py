
import dataiku
#import pytest

client = dataiku.api_client()
project = client.get_default_project()
scenario = project.get_scenario("Rebuild Daily")

scenario.run_and_wait()

