import numpy as np
import plotly.express as px
import pandas as pd
import os



def float_range(start: float, stop: float, step: float=0.1)->float:
    while start < stop:
        yield start
        start += step

def eulers_method(step: float, start: float, stop: float, y_initial: float, function)->list:
    y_n: float = y_initial
    output_nums: float = [(start, y_n)]
    for i in float_range(start, stop, step):
        y_n = y_n + step*function(i, y_n)
        output_nums.append((i, y_n))
    return output_nums

def ploter(data_frame, name)->None:
    fig = px.line(data_frame, x = 'x', y='y', title='Graph of y(x)')
    if not os.path.exists("images"):
        os.mkdir("images")    
    fig.write_image(f"images/{name}.png")
    print("graph image saved succesfully")
    fig.show()

def create_data_frame(input_list: list)->pd.DataFrame:
    return pd.DataFrame(dict(x = [i[0] for i in input_list], y = [i[1] for i in input_list]))

def main()->None:
    graph_name: str = input("Chose a name for the output graph: ")
    start: float = float(input("Input starting value: "))
    stop: float = float(input("Input stop value: "))
    step: float = float(input("Input step size: "))
    y_initial: float = float(input("Input y_0: "))
    function = eval("lambda x, y: " + input("Input your differntial eqation in terms of x and y: "))
    vals = eulers_method(step, start, stop, y_initial, function)
    for i in vals:
        print(i)
    df = create_data_frame(vals)
    ploter(df, graph_name)
    return None

if __name__ == "__main__":
    main()
