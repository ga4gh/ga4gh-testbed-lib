import os
import pytest
from ga4gh.testbed.report.report import Report

constants_inputs = "attr,getter,exp_value,test_value"
constants_cases = [
    (
        "schema_name",
        "get_schema_name",
        "ga4gh-testbed-report",
        "ga4gh"
    ),
    (
        "schema_version",
        "get_schema_version",
        "0.1.0",
        "1.0.0"
    )
]

to_json_inputs = "testbed_name," \
    + "testbed_version," \
    + "testbed_description," \
    + "platform_name," \
    + "platform_description," \
    + "input_parameter_key," \
    + "input_parameter_value," \
    + "input_parameter_secure," \
    + "start_time," \
    + "end_time," \
    + "exp_int"
to_json_cases = [
    (
        "Horizontal Demo",
        "1.0.0",
        "Federated Analysis Systems Project (FASP) Horizontal Demo",
        "GA4GH Starter Kit Reference",
        "Reference deployment of the GA4GH Starter Kit",
        "url",
        "https://testsite.ga4gh.org/api",
        False,
        "2021-10-20T12:00:00Z",
        "2021-10-20T13:00:00Z",
        "00"
    )
]

@pytest.mark.parametrize(constants_inputs, constants_cases)
def test_report_constants(attr, getter, exp_value, test_value):
    report = Report()
    getter_method = getattr(report, getter)
    assert getter_method() == exp_value

    exception_raised = False
    try:
        setattr(report, attr, test_value)
    except Exception as e:
        exception_raised = True
    assert exception_raised

@pytest.mark.parametrize(to_json_inputs, to_json_cases)
def test_report_to_json(testbed_name, testbed_version, testbed_description,
    platform_name, platform_description,
    input_parameter_key, input_parameter_value, input_parameter_secure,
    start_time, end_time, exp_int):

    report = Report()
    report.set_testbed_name(testbed_name)
    report.set_testbed_version(testbed_version)
    report.set_testbed_description(testbed_description)
    report.set_platform_name(platform_name)
    report.set_platform_description(platform_description)
    if input_parameter_secure:
        report.add_secure_input_parameter(input_parameter_key)
    else:
        report.add_input_parameter(input_parameter_key, input_parameter_value)
    report.set_start_time(start_time)
    report.set_end_time(end_time)

    exp_json_path_prefix = os.path.join("test", "data", "report", "expected_report_" + exp_int)
    exp_json_path = exp_json_path_prefix + ".json"
    exp_json_path_pretty = exp_json_path_prefix + ".pretty.json"

    exp_json = open(exp_json_path, "r").read()
    exp_json_pretty = open(exp_json_path_pretty, "r").read()

    assert report.to_json() == exp_json
    assert report.to_json(pretty=True) == exp_json_pretty
