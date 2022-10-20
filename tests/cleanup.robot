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


Connect to Routers and unconfigure BGP Test
  unconfigure bgp R1  ${ROUTER1}  ${R1_ASN}
  unconfigure bgp R2  ${ROUTER2}  ${R2_ASN}
  


  