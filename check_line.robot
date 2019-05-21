*** Settings ***
Test Timeout    2 minutes
Library         check_line.py

*** Test Cases ***
Default Timeout
    [Documentation]         Timeout from the Setting table is used
    ${result_string}=       check line
    ${expected_string}=     Set Variable        Hello World!
    Should Be Equal     ${result_string}        ${expected_string}      msg=Not equal
