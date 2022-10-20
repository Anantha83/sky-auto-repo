*** Settings ***
Library        ../lib/SSHConnector.py

*** Variables ***
${R1_ASN}=  100
${R2_ASN}=  100
${R1_BGP_INTF_IP}=  11.1.1.10
${R2_BGP_INTF_IP}=  11.1.1.11
${R1_USER}=  cisco
${R2_USER}=  cisco
${R1_PASS}=  cisco
${R2_PASS}=  cisco
${SECRET_PASS}=  cisco
${TEST_INCORRECT_PASS}=  cisco1
${PORT}=  22


*** Keywords ***
R1 login
  [Arguments]  ${arg1}  ${arg2}  ${arg3}  ${arg4}  ${arg5}  ${arg6}
  ${r1_handle}=  login  ${arg1}  ${arg2}  ${arg3}  ${arg4}  ${arg5}  ${arg6}
  Set Global Variable  ${r1_handle}  ${r1_handle}
R2 login
  [Arguments]  ${arg1}  ${arg2}  ${arg3}  ${arg4}  ${arg5}  ${arg6}
  ${r2_handle}=  login  ${arg1}  ${arg2}  ${arg3}  ${arg4}  ${arg5}  ${arg6}
  Set Global Variable  ${r2_handle}  ${r2_handle}
configure bgp R1
  [Arguments]        ${arg1}  ${arg2}  ${arg3}  ${arg4}  ${arg5}
  ${result}          configure bgp  ${r1_handle}  ${arg1}  ${arg2}  ${arg3}  ${arg4}  ${arg5}
  Log To Console     ${result}}
configure bgp R2
  [Arguments]        ${arg1}  ${arg2}  ${arg3}  ${arg4}  ${arg5}
  ${result}          configure bgp  ${r2_handle}  ${arg1}  ${arg2}  ${arg3}  ${arg4}  ${arg5}
  Log To Console     ${result}}
unconfigure bgp R1
  [Arguments]        ${arg1}  ${arg2}
  ${result}          unconfigure bgp  ${r1_handle}  ${arg1}  ${arg2}
  Log To Console     ${result}}
unconfigure bgp R2
  [Arguments]        ${arg1}  ${arg2}
  ${result}          unconfigure bgp  ${r2_handle}  ${arg1}  ${arg2}
  Log To Console     ${result}}
verify bgp R1
  [Arguments]        ${arg1}  ${arg2}
  ${result}          verify bgp  ${r1_handle}  ${arg1}  ${arg2}
  Log To Console     ${result}}
clear bgp command R1
  [Arguments]        ${arg1}
  ${result}          clear bgp session  ${r1_handle}  ${arg1}