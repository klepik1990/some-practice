*** Settings ***
Test Timeout    2 minutes
Library         check_request.py

*** Test Cases ***
Default Timeout
    [Documentation]         Timeout from the Setting table is used
    ${result_int}=       Check Response
    ${expected_int}=     Set Variable        ${200}
    should be equal        ${result_int}        ${expected_int}      msg=Not equal
