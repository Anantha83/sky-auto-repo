*** Settings ***
Library        ../lib/SSHConnector.py


*** Test Case ***


Connect to Routers and unconfigure BGP Test
  unconfigure bgp R1  10.1.1.10  100
  unconfigure bgp R2  10.1.1.11  100
  

*** Keywords ***
unconfigure bgp R1
  [Arguments]        ${arg1}  ${arg2}
  ${result}          unconfigure bgp  ${arg1}  ${arg2}
  Log To Console     ${result}}
unconfigure bgp R2
  [Arguments]        ${arg1}  ${arg2}
  ${result}          unconfigure bgp  ${arg1}  ${arg2}
  Log To Console     ${result}}

  