# Standard Error of Regression Calculator

Script intended for NumWorks Calculator to calculate the Standard Error of Regression, which isn't a feature available on NumWorks. This standard error value can then be used to determine the t-statistic in linear regression analysis. Learn more about it [here](https://stattrek.com/regression/slope-test.aspx).

To load this onto a NumWorks calculator, find the script [here](https://my.numworks.com/python/ethanolchennault/seor)

# Functions

`main() -> None`: Execute program asking for user input and outputting SEoR. This only needs to be called if this script is imported. If run as main, then `main` will automatically be called.

`SEoR(x_data, y_data) -> float`:
Calculate the standard error of regression value. Calls `LSRL()` internally. Validates `x_data` and `y_data` parameters internally through use of `validate` decorator.

`LSRL(x_data, y_data) -> tuple`:
Return a tuple containing `(slope, y_intercept, x_mean)` which are to be used in `SEoR()`. Parameters `x_data` and `y_data` are NOT validated through use of `validate` decorator.

`validate(func) -> ((x_data: list, y_data: list) -> func)`:
Decorator to validate parameters `x_data` and `y_data` by ensuring they are of same length and are not of length zero. Does not do any further data validation.
