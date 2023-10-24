# Automated UI Testing with Selenium and PyTest

## Introduction

This project demonstrates automated UI testing using Selenium and PyTest. The goal of the project is to perform end-to-end testing on the SauceDemo website. The tests include logging in, adding items to the cart, and completing the checkout process.

## Technologies

The project uses the following technologies:

- **Selenium**: A powerful tool for controlling web browsers through programs and automating browser tasks.
- **PyTest**: A testing framework for Python that allows for simple unit tests as well as complex functional testing.
- **Logging**: Python's built-in logging module is used to capture log information during test execution.

## Running the Tests

Before running the tests, make sure you have the necessary libraries installed. You can install them using `pip`:

```bash
pip install selenium pytest webdriver-manager
```
To run the tests, execute the following command in your terminal:
```bash
pytest test_selenium.py
```

## Test Description
The provided test script (test_sel()) performs the following actions:

Logs in to the SauceDemo website.
Adds items to the cart.
Completes the checkout process.
Logs relevant information during the test, such as order summary.
Please ensure you have a compatible version of Chrome browser installed, as the tests are configured to use Chrome.