# My first Git repository Project

Hello, my name is Anantha, Here is my first GitHub repository.

Goal for this repo is to create mini framework having ability to configure required routing protocols on the mentioned network devices. 
It has UI that gets the details from user about configuration and sends rest API calls to the framework, framework takes care to connect and configure on the mentioned devices

    User -----HTTP/REST/CLI----> [Your Automation Program] ---Netconf/Cli-----> Device

Basic UI to provide device info and what needs to be done
Setup - Helps in configuring BGP commands on both routers
cleanup - Helps to unconfigure BGP commands which was earlier configured by Setup
test - Helps in running BGP MD5 test with matching and mismatch password. It wont unconfigure
all - does all steps done as part of setup,cleanup and test 

![User UI](https://github.com/Anantha83/sky-auto-repo/blob/main/images/front_basic_ui.png)
Below is the device topology.
Topology created using GNS3
LoopBack Network Adapter created to reach the instance inside the GNS3 tool

![Topology](https://github.com/Anantha83/sky-auto-repo/blob/main/images/topology.png)

Sample report while selecting all in UI. Which is passed to Flask, Which inturn calls all.robot and reports below  page post successful completion

![report](https://github.com/Anantha83/sky-auto-repo/blob/main/images/sample_report.png) 

Thanks for reading! ☺