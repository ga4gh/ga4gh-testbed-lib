import pytest
import json
import os
from ga4gh.testbed.report.report import Report

inputs = "i," \
    + "timestamp_start,timestamp_end," \
    + "testbed_name,testbed_version,testbed_description," \
    + "platform_name,platform_description," \
    + "input_parameters," \
    + "phases"
cases = [
    
    # case 0
    (
        "0",
        "2021-10-22T15:00:00Z",
        "2021-10-22T15:30:00Z",
        "Unspecified GA4GH Testbed",
        "v1.0.0",
        "A generic testbed",
        "GA4GH Starter Kit Reference Deployment",
        "Reference deployment of the GA4GH Starter Kit running on AWS",
        [
            {
                "secure": True,
                "key": "token",
                "value": "wqoerisdadhsldfj"
            },
            {
                "secure": False,
                "key": "url",
                "value": "https://some-site.genomics.org"
            }
        ],
        [
            {
                "phase_name": "Sequences",
                "phase_description": "Tests all sequence endpoints",
                "tests": [
                    {
                        "test_name": "Get Sequence",
                        "test_description": "Get a reference sequence",
                        "cases": [
                            {
                                "case_name": "Get e. coli",
                                "case_description": "Get e. coli reference sequence",
                                "message": "Retrieved successfully",
                                "status_setter": "set_status_pass"
                            },
                            {
                                "case_name": "Get s. cerevisiae",
                                "case_description": "Get s. cerevisiae reference sequence",
                                "message": "Skipping test",
                                "status_setter": "set_status_skip"
                            }
                        ]
                    },
                    {
                        "test_name": "List Sequences",
                        "test_description": "List reference sequences",
                        "cases": [
                            {
                                "case_name": "List bacterial sequences",
                                "case_description": "List all bacterial reference sequences",
                                "message": "Passed with some warnings",
                                "status_setter": "set_status_warn"
                            },
                            {
                                "case_name": "List fungal sequences",
                                "case_description": "List all fungal reference sequences",
                                "message": "All fungal sequences retrieved",
                                "status_setter": "set_status_pass"
                            }
                        ]
                    }
                ]
            },
            {
                "phase_name": "Variants",
                "phase_description": "Tests all variants endpoints",
                "tests": [
                    {
                        "test_name": "Get Variant",
                        "test_description": "Get an observed variant",
                        "cases": [
                            {
                                "case_name": "Get synonymous mutation",
                                "case_description": "Get the specified synonymous mutation",
                                "message": "Retrieved successfully",
                                "status_setter": "set_status_pass"
                            },
                            {
                                "case_name": "Get non-synonymous mutation",
                                "case_description": "Get the specified non-synonymous mutation",
                                "message": "Failed to retrieve the specified non-synonymous mutation",
                                "status_setter": "set_status_fail"
                            }
                        ]
                    },
                    {
                        "test_name": "List Variants",
                        "test_description": "Get filtered lists of desired variants" ,
                        "cases": [
                            {
                                "case_name": "List synonymous mutations",
                                "case_description": "List all synonymous mutations",
                                "message": "Test skipped",
                                "status_setter": "set_status_skip"
                            },
                            {
                                "case_name": "List non-synonymous mutations",
                                "case_description": "List all non-synonymous mutations",
                                "message": "Test skipped",
                                "status_setter": "set_status_skip"
                            }
                        ]
                    }
                ]
            }
        ]
    ),

    # case 1
]

@pytest.mark.parametrize(inputs, cases)
def test_report_finalization_serialization(i,
    timestamp_start, timestamp_end,
    testbed_name, testbed_version, testbed_description,
    platform_name, platform_description,
    input_parameters,
    phases):
    
    report = Report()

    # top-level info
    report.set_start_time(timestamp_start)
    report.set_end_time(timestamp_end)
    report.set_testbed_name(testbed_name)
    report.set_testbed_version(testbed_version)
    report.set_testbed_description(testbed_description)
    report.set_platform_name(platform_name)
    report.set_platform_description(platform_description)

    # input params
    for p in input_parameters:
        if p["secure"]:
            report.add_secure_input_parameter(p["key"])
        else:
            report.add_input_parameter(p["key"], p["value"])
    
    # phases
    for phase_attrs in phases:
        phase = report.add_phase()
        phase.set_start_time(timestamp_start)
        phase.set_end_time(timestamp_end)
        phase.set_phase_name(phase_attrs["phase_name"])
        phase.set_phase_description(phase_attrs["phase_description"])
        
        # tests
        for test_attrs in phase_attrs["tests"]:
            test = phase.add_test()
            test.set_start_time(timestamp_start)
            test.set_end_time(timestamp_end)
            test.set_test_name(test_attrs["test_name"])
            test.set_test_description(test_attrs["test_description"])

            # cases
            for case_attrs in test_attrs["cases"]:
                case = test.add_case()
                case.set_start_time(timestamp_start)
                case.set_end_time(timestamp_end)
                case.set_case_name(case_attrs["case_name"])
                case.set_case_description(case_attrs["case_description"])
                case.set_message(case_attrs["message"])

                status_set_fn = getattr(case, case_attrs["status_setter"])
                status_set_fn()
    
    report.finalize()
    actual_json_pretty = report.to_json(pretty=True)
    actual_json_regular = report.to_json(pretty=False)
    
    exp_dir = os.path.join("tests", "data", "e2e", "report_finalization_serialization")
    exp_file = i + ".json"
    exp_fp = os.path.join(exp_dir, exp_file)

    exp_json_pretty = open(exp_fp, "r").read()
    json_obj = json.loads(exp_json_pretty)
    exp_json_regular = json.dumps(json_obj, separators=(",",":"))

    assert actual_json_pretty == exp_json_pretty
    assert actual_json_regular == exp_json_regular
