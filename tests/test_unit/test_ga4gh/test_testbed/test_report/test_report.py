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

testbed_name_inputs = "testbed_name"
testbed_name_cases = [
    ("RNAget Compliance Suite"),
    ("FASP Challenge 2022")
]

testbed_version_inputs = "testbed_version"
testbed_version_cases = [
    ("1.0.0"),
    ("11.12.13")
]

testbed_description_inputs = "testbed_description"
testbed_description_cases = [
    ("Assess server compliance to the RNAget specification"),
    ("Participate in the FASP challenge involving DRS, Passports, and WES")
]

platform_name_inputs = "platform_name"
platform_name_cases = [
    ("GA4GH Starter Kit Reference Deployment"),
    ("Caltech RNAget Deployment")
]

platform_description_inputs = "platform_description"
platform_description_cases = [
    ("Reference deployment of the GA4GH Starter Kit running on AWS"),
    ("Caltech reference implementation of RNAget specification")
]

input_parameters_inputs = "key,value,secure,exp_value"
input_parameters_cases = [
    (
        "url",
        "https://api.ga4gh.org",
        False,
        "https://api.ga4gh.org"
    ),
    (
        "passport_token",
        "hfqwuhfeqhfksajdfhalkhdf",
        True,
        "[SECURE]"
    )
]

report_add_phases_inputs = "phase_names"
report_add_phases_cases = [
    (
        [
            "Projects",
            "Studies",
            "Expressions",
            "Continuous"
        ]
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

@pytest.mark.parametrize(testbed_name_inputs, testbed_name_cases)
def test_testbed_name(testbed_name):
    report = Report()
    report.set_testbed_name(testbed_name)
    assert report.get_testbed_name() == testbed_name

@pytest.mark.parametrize(testbed_version_inputs, testbed_version_cases)
def test_testbed_version(testbed_version):
    report = Report()
    report.set_testbed_version(testbed_version)
    assert report.get_testbed_version() == testbed_version

@pytest.mark.parametrize(testbed_description_inputs, testbed_description_cases)
def test_testbed_description(testbed_description):
    report = Report()
    report.set_testbed_description(testbed_description)
    assert report.get_testbed_description() == testbed_description

@pytest.mark.parametrize(platform_name_inputs, platform_name_cases)
def test_platform_name(platform_name):
    report = Report()
    report.set_platform_name(platform_name)
    assert report.get_platform_name() == platform_name

@pytest.mark.parametrize(platform_description_inputs, platform_description_cases)
def test_platform_description(platform_description):
    report = Report()
    report.set_platform_description(platform_description)
    assert report.get_platform_description() == platform_description

@pytest.mark.parametrize(input_parameters_inputs, input_parameters_cases)
def test_add_remove_input_parameters(key, value, secure, exp_value):
    report = Report()
    if secure:
        report.add_secure_input_parameter(key)
    else:
        report.add_input_parameter(key, value)
    
    assert report.get_input_parameter(key) == exp_value
    report.remove_input_parameter(key)
    assert report.get_input_parameter(key) == None

@pytest.mark.parametrize(report_add_phases_inputs, report_add_phases_cases)
def test_report_add_phases(phase_names):
    report = Report()
    for phase_name in phase_names:
        phase = report.add_phase()
        phase.set_phase_name(phase_name)
    
    returned_phases = report.get_phases()
    for i in range(0, len(phase_names)):
        assert returned_phases[i].get_phase_name() == phase_names[i]
    
    for i in range(0, len(phase_names)):
        assert report.get_phase(i).get_phase_name() == phase_names[i]

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

    exp_json_path_prefix = os.path.join("tests", "data", "report", "expected_report_" + exp_int)
    exp_json_path = exp_json_path_prefix + ".json"
    exp_json_path_pretty = exp_json_path_prefix + ".pretty.json"

    exp_json = open(exp_json_path, "r").read()
    exp_json_pretty = open(exp_json_path_pretty, "r").read()

    assert report.to_json() == exp_json
    assert report.to_json(pretty=True) == exp_json_pretty
