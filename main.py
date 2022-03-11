from math import sqrt


def validate(func):
    def inner(x_data, y_data):
        if len(x_data) != len(y_data):
            print("ERROR: Data sets are not of equal length.")
            quit()

        if len(x_data) == 0 or len(y_data) == 0:
            print("ERROR: One or more data sets are of 0 length.")
            quit()

        return func(x_data, y_data)
    return inner


def LSRL(x_data, y_data):
    x_mean = sum(x_data) / len(x_data)
    y_mean = sum(y_data) / len(y_data)

    slope_numerator = 0
    slope_denominator = 0

    for i in range(0, len(x_data)):
        slope_numerator += (x_data[i] - x_mean) * (y_data[i] - y_mean)
        slope_denominator += (x_data[i] - x_mean) ** 2

    slope = slope_numerator / slope_denominator

    y_intercept = y_mean - slope * x_mean

    return slope, y_intercept, x_mean


@validate
def SEoR(x_data, y_data):
    slope, y_intercept, x_mean = LSRL(x_data, y_data)

    y_residuals_squared = 0
    x_residuals_squared = 0

    for i in range(0, len(x_data)):
        y_residuals_squared += (y_data[i] -
                                (slope * x_data[i] + y_intercept)) ** 2
        x_residuals_squared += (x_data[i] - x_mean) ** 2

    dF_coef = 1 / (len(x_data) - 2)

    print(dF_coef, y_residuals_squared, x_residuals_squared)

    return sqrt(dF_coef * (y_residuals_squared / x_residuals_squared))


def main():
    print("Tips: Have data set pre-typed and to be pasted. No need to include spaces in comma separation.")

    x_data = [float(x) for x in input('Enter x data values, comma seperated:\n').replace(
        ' ', '').split(',')]

    y_data = [float(y) for y in input('Enter y data values, comma seperated:\n').replace(
        ' ', '').split(',')]

    print(SEoR(x_data, y_data))


if __name__ == '__main__':
    main()
