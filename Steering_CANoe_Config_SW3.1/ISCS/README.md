# ISCS Automated Test Suite

This directory contains automated test scripts for validating the ISCS ECU.

## Folder Structure
```
ISCS/
│── Scripts/
│   ├── DynamicISCS.can
│   ├── icscTest.can
│   ├── DTC_Buffering.can
│   ├── ReadSWVersion.cin
│── Reports/
│   ├── latest_test_report.html
│── README.md
```

## Description of Scripts
- **DynamicISCS.can**: Handles dynamic signal testing for ISCS.
- **icscTest.can**: Main test case script for validating ISCS functionality.
- **DTC_Buffering.can**: Reads and buffers Diagnostic Trouble Codes (DTCs) before and after test execution.
- **ReadSWVersion.cin**: Reads the software version of the ISCS module.

## Running Tests
1. Open the `.can` scripts in CANoe or CANalyzer.
2. Execute the test cases.
3. View the generated report in the `Reports/` folder.

## Managing Reports
- The `Reports/` folder stores the latest HTML report from the test execution.
- Ensure to replace the latest report after each test run.

## Contribution
- Follow the existing structure when adding new scripts.
- Update this README if new test cases are introduced.

