*** Settings ***
Library        lib/SSHConnector.py


*** Test Case ***


Connect to Routers and Confgiure BGP Test 
  configure bgp R1  10.1.1.10  100  100  11.1.1.11  cisco
  configure bgp R2  10.1.1.11  100  100  11.1.1.10  cisco
  
verify BGP Session Success
  verify bgp R1  10.1.1.10  Success

Connect to Routers and Confgiure different Password in R1
  configure bgp R1  10.1.1.10  100  100  11.1.1.11  cisco1

Clear BGP Session on R1
  clear bgp command R1  10.1.1.10

verify BGP Session Failure
  verify bgp R1  10.1.1.10  Failure
  
Connect to Routers and unconfigure BGP Test
  unconfigure bgp R1  10.1.1.10  100
  unconfigure bgp R2  10.1.1.11  100
  

*** Keywords ***
configure bgp R1
  [Arguments]        ${arg1}  ${arg2}  ${arg3}  ${arg4}  ${arg5}
  ${result}          configure bgp  ${arg1}  ${arg2}  ${arg3}  ${arg4}  ${arg5}
  Log To Console     ${result}}
configure bgp R2
  [Arguments]        ${arg1}  ${arg2}  ${arg3}  ${arg4}  ${arg5}
  ${result}          configure bgp  ${arg1}  ${arg2}  ${arg3}  ${arg4}  ${arg5}
  Log To Console     ${result}}
unconfigure bgp R1
  [Arguments]        ${arg1}  ${arg2}
  ${result}          unconfigure bgp  ${arg1}  ${arg2}
  Log To Console     ${result}}
unconfigure bgp R2
  [Arguments]        ${arg1}  ${arg2}
  ${result}          unconfigure bgp  ${arg1}  ${arg2}
  Log To Console     ${result}}
verify bgp R1
  [Arguments]        ${arg1}  ${arg2}
  ${result}          verify bgp  ${arg1}  ${arg2}
  Log To Console     ${result}}
clear bgp command R1
  [Arguments]        ${arg1}
  ${result}          clear bgp session  ${arg1}
  