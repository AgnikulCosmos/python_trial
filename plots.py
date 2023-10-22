import pandas as pd
from nptdms import TdmsFile
import plotly.graph_objs as go
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots


for col in range(1,):

    # file1 = input("enter the input file:")

    tdms_file = TdmsFile("VP-003 ACC POST Y-AXIS_2023_Oct_03_20h_35m_50Sec.tdms")

    # file1_data = pd.DataFrame()

    # print(file1_data)
   


    for group in tdms_file.groups():
        df = group.as_dataframe()
        if(len(df.columns.to_list())>1):
            file1_data = df

    # print(file1_data)


    file1_data['AITime'] = pd.to_datetime(file1_data['AITime'], format='%m/%d/%Y %H:%M:%S.%f')

    file1_data['AITime'] = (file1_data['AITime'] - file1_data['AITime'][0]).dt.total_seconds()

    # Convert datetime columns to consistent datetime format
    file1_data['AITime'] = pd.to_timedelta(file1_data['AITime'], unit='s')

    # downsampling_factor = 200  # Adjust as needed
    # file1_data = file1_data.iloc[::downsampling_factor, :]

    # Define columns to plot
    columns_to_plot_file1 = [col for col in file1_data.columns if (col!='AITime')]  # Adjust these columns based on your file1

    ax = plt.gca()
    print(file1_data['v1'] )
 
    g =file1_data.plot(kind='line',
        x='AITime',
        y='v1',
        color='green',
        label='RTD1',
           ax=ax)
    plt.show()
    

    # # Create traces for each column in both datasets
    # traces_file1 = []
    # fig = make_subplots(rows=10, cols=2, vertical_spacing=0.1)
    # i=1;
    # j=1;
    # for col in columns_to_plot_file1:
    #     trace = go.Scatter(x=file1_data['AITime'], y=file1_data[col], mode='lines', name=f'{col}')
    #     print(col)
    #     if j<11:
            
    #         if i<3:
    #             fig.add_trace(trace,row=j, col=i)
    #             fig.update_xaxes(title_text="T(ms)", row=j, col=i)
    #             fig.update_yaxes(title_text="Temp(C)", row=j, col=i) 
    #             i=i+1
    #         else:
    #             i=1;
    #             j=j+1
    #             fig.add_trace(trace,row=j, col=i)
    #             fig.update_xaxes(title_text="T(ms)", row=j, col=i)
    #             fig.update_yaxes(title_text="Temp(C)", row=j, col=i)
    #             i=i+1
                
    # # Create layout
    # layout = go.Layout(title='Overlapping Plots',
    #                    xaxis=dict(title='Time'),
    #                    yaxis=dict(title='Tempersture in deg C'))

    # figname = input("Fig_name: ")

    # file1_data.write_html(figname, auto_open=True)

