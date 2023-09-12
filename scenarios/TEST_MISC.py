
import dataiku
#import pytest

client = dataiku.api_client()
project = client.get_default_project()
scenario = project.get_scenario("REBUILDDAILY")

scenario.run_and_wait()

