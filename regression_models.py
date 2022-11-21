import time

from matplotlib import pyplot as plt
from matplotlib import animation as animation
from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.preprocessing import PolynomialFeatures
import cmath

import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# plt.style.use('fivethirtyeight')


# plt.ion()
import executors


def perform_liner_regression(data_frame):
    print("Performing linear Regression...")
    x = pd.DataFrame(data_frame, columns=["time"])
    y = pd.DataFrame(data_frame, columns=["count"])

    lm = LinearRegression()
    model = lm.fit(x, y)

    m = model.coef_
    c = model.intercept_

    # print("Score : " + str(model.score(x, y)))
    # print("Coefficients : " + str(model.coef_))
    # print("Intercept : " + str(model.intercept_))
    print("Liner Prediction : y = " + str(m) + "x + " + str(c))
    print("--------------------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------------------")
    print("Waiting for 1 minute...")
    time.sleep(60)
    # data_frame = data_frame.astype('float64')  # <-seaborn library bug fix
    # sns.pairplot(data_frame, x_vars=['time'], y_vars='count', height=3, aspect=0.7, kind='reg')
    # plt.show()


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
    print("PREDICTION : "+str(prediction))

    # plt.scatter(x, y, color='red')
    # plt.plot(x, prediction, color='blue')
    # plt.xlabel("Time (minutes)", fontdict=font1)
    # plt.ylabel("Likes", fontdict=font1)

    coefficients = model.coef_
    a = coefficients[2]
    b = coefficients[1]
    c = model.intercept_

    predicted_value = (a * next_minute * next_minute) + (b * next_minute) + c

    data_frame.loc[counter, 'a'] = round(a, 3)
    data_frame.loc[counter, 'b'] = round(b, 3)
    data_frame.loc[counter, 'c'] = round(c, 3)
    data_frame.loc[counter, 'predicted_value'] = round(predicted_value, 3)

    # Save coordinates into an Excel file
    writer = pd.ExcelWriter('Data\graph.xlsx',mode='a',if_sheet_exists='replace')
    data_frame.to_excel(writer)
    writer.save()

    #x = open('title.txt', 'w').write("y = (" + str(round(a, 3)) + ")x^2 + (" + str(round(b, 3)) + ")x + " + str( round(c, 3)))

    # plt.title("y = (" + str(round(a, 3)) + ")x^2 + (" + str(round(b, 3)) + ")x + " + str(round(c, 3)), fontdict=font1)

    # figure_manager = plt.get_current_fig_manager()
    # figure_manager.full_screen_toggle()
    # plt.show()

    # # Kind of bug fix
    # plt.pause(1)

    # Save the screen-shot

    # ani = FuncAnimation(plt.gcf(), animate, interval=1000)

    # # plt.tight_layout()
    # plt.show()
    # # plt.pause(1)

    print("Coefficients : " + str(model.coef_))
    print("Intercept : " + str(model.intercept_))
    print("Score [r2] : " + str(r2_score(y, prediction)))
    print("Saturated Time : " + str((b / (2 * a * (-1))) - counter) + " minutes")
    print("Popularity Condition :" + str(c - ((b * b) / (4 * a))))

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
