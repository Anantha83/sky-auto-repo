*** Settings ***
Resource          keywords.resource

*** Variables ***
${ROUTER1}
${ROUTER2}
${DEVICE_TYPE}

*** Test Case ***
Login to Device  
  R1 login  ${ROUTER1}  ${DEVICE_TYPE}  ${PORT}  ${R1_USER}  ${R1_PASS}  ${SECRET_PASS}
  R2 login  ${ROUTER2}  ${DEVICE_TYPE}  ${PORT}  ${R2_USER}  ${R1_PASS}  ${SECRET_PASS}

verify BGP Session Success
  verify bgp R1  ${ROUTER1}  Success

Connect to Routers and Configure different Password in R1
  configure bgp R1  ${ROUTER1}  ${R1_ASN}  ${R2_ASN}  ${R2_BGP_INTF_IP}  ${TEST_INCORRECT_PASS}

Clear BGP Session on R1
  clear bgp command R1  ${ROUTER1}

verify BGP Session Failure
  verify bgp R1  ${ROUTER1}  Failure

Connect to Routers and Configure old Password in R1
  configure bgp R1  ${ROUTER1}  ${R1_ASN}  ${R2_ASN}  ${R2_BGP_INTF_IP}  ${TEST_INCORRECT_PASS}
    
Connect to Routers and unconfigure BGP Test
  unconfigure bgp R1  ${ROUTER1}  ${R1_ASN}
  unconfigure bgp R2  ${ROUTER2}  ${R2_ASN}
  
