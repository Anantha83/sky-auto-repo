*** Settings ***
Library        ../lib/SSHConnector.py


*** Test Case ***


Connect to Routers and Confgiure BGP Test 
  configure bgp R1  10.1.1.10  100  100  11.1.1.11  cisco
  configure bgp R2  10.1.1.11  100  100  11.1.1.10  cisco


*** Keywords ***
configure bgp R1
  [Arguments]        ${arg1}  ${arg2}  ${arg3}  ${arg4}  ${arg5}
  ${result}          configure bgp  ${arg1}  ${arg2}  ${arg3}  ${arg4}  ${arg5}
  Log To Console     ${result}}
configure bgp R2
  [Arguments]        ${arg1}  ${arg2}  ${arg3}  ${arg4}  ${arg5}
  ${result}          configure bgp  ${arg1}  ${arg2}  ${arg3}  ${arg4}  ${arg5}
  Log To Console     ${result}}