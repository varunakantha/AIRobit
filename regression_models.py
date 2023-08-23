import threading
import time

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import cmath
import pandas as pd


def perform_liner_regression(data_frame):
    print("Performing linear Regression...")
    x = pd.DataFrame(data_frame, columns=["time"])
    y = pd.DataFrame(data_frame, columns=["count"])

    lm = LinearRegression()
    model = lm.fit(x, y)

    m = model.coef_
    c = model.intercept_

    print("Liner Prediction : y = " + str(m) + "x + " + str(c))
    time.sleep(60)


def perform_polynomial_regression(data_frame, counter):
    print("Performing polynomial Regression...")
    font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
    next_minute = counter + 1

    x = data_frame.iloc[:, 0:1].values
    y = data_frame.iloc[:, 1].values

    total_likes = data_frame.iloc[-1, 1]

    # Fitting Polynomial Regression to the dataset

    poly_reg = PolynomialFeatures(degree=2)
    X_poly = poly_reg.fit_transform(x)
    pol_reg = LinearRegression()
    model = pol_reg.fit(X_poly, y)

    prediction = pol_reg.predict(poly_reg.fit_transform(x))

    coefficients = model.coef_
    a = coefficients[2]
    b = coefficients[1]
    c = model.intercept_

    predicted_value = (a * next_minute * next_minute) + (b * next_minute) + c

    data_frame.loc[counter, 'a'] = round(a, 3)
    data_frame.loc[counter, 'b'] = round(b, 3)
    data_frame.loc[counter, 'c'] = round(c, 3)
    data_frame.loc[counter, 'predicted_value'] = round(predicted_value, 3)

    # print("Data Frame : "+str(data_frame))

    # Save coordinates into an Excel file
    lock = threading.Lock()
    lock.acquire()
    writer = pd.ExcelWriter('Data\graph.xlsx', if_sheet_exists='replace',engine="openpyxl", mode='a')
    data_frame.to_excel(writer)
    writer.save()
    lock.release()

    print("Coefficients : " + str(model.coef_))
    print("Intercept : " + str(model.intercept_))
    # print("Score [r2] : " + str(r2_score(y, prediction)))
    # print("Saturated Time : " + str((b / (2 * a * (-1))) - counter) + " minutes")
    # print("Popularity Condition :" + str(c - ((b * b) / (4 * a))))

    saturated_time = b / (2 * a * (-1))

    a1 = 3 * b * b
    a2 = 4 * a * c
    a3 = 4 * a
    # print("DEBUG a1 | a2 | a3 : "+str(a1) + " | "+str(a2)+" | "+str(a3))

    # calculating  the discriminant
    dis = (b ** 2) - (4 * a * c)

    # find two results
    ans1 = (-b - cmath.sqrt(dis)) / (2 * a)
    ans2 = (-b + cmath.sqrt(dis)) / (2 * a)

    # printing the results
    print("Discriminant : " + str(dis))
    print('Solutions : ' + str(ans1) + " | " + str(ans2))
    # print("Predicted Total Likes : " + str(((3 * b * b) + (4 * a * c)) / (4 * a)))
    print("Predicted Likes in next minute-2 : " + str(
        ((a * next_minute * next_minute) + (b * next_minute) + c) - total_likes))
    print("Predicted Likes in next minute-1 : " + str(round(b)))
    print("Predicted Total Likes : " + str(((a * saturated_time * saturated_time) + (b * saturated_time) + c)))
    print("--------------------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------------------")
    print("Waiting for 1 minute...")
    time.sleep(10)
