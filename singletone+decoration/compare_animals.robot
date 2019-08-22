*** Settings ***
Test Timeout    2 minutes
Library         compare_animals.py

*** Test Cases ***
Default Timeout
    [Documentation]         Timeout from the Setting table is used
    ${first_param}        ${second_param}=       compare animals
    should be equal   ${first_param}        ${second_param}      msg=Not equal