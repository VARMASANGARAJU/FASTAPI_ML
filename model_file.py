#Import for processing
import pandas as pd

#Imports for models
from statsmodels.tsa.holtwinters import ExponentialSmoothing

class Reader:
    def __init__(self):
        pass

    def excel_reader(self, path_to_file):
        '''
            Reads the input Excel File and converts it into a DataFrame

            Format of the excel file
            - Date | Value of Time Series
        '''
        #If there are multiple sheets this returns a dict {'sheet_name':dataframe}
        #TODO: Check if the uploaded file is an excel file or not
        if path_to_file:
            data = pd.read_excel(path_to_file, sheet_name=None)

            #Since the excel file contains multiple sheets we concat all the sheets into a single dataframe
            all_data = pd.DataFrame()
            for key in data:
                all_data = pd.DataFrame(pd.concat([all_data, data[key]], ignore_index=True))


            #Set the index as the date and sort according to date
            all_data.set_index('Date', inplace=True)
            all_data.sort_index(inplace=True)
            all_data.reset_index(inplace=True)
        else:
            print("Please provide the path to the excel file")

        return all_data

    def csv_reader(csv_data):
        '''
            Reads the input Excel File and converts it into a DataFrame

            Format of the csv file
            - Date | Value of Time Series
        '''
        data = None

        data = csv_data

        data = data.rename(columns={"Month": "Date"})

        #Set the index as the date and sort according to date
        data.set_index('Date', inplace=True)
        data.sort_index(inplace=True)
        # data.reset_index(inplace=True)


        return data

class Transformer:
    def __init__(self, data):
        self.dataframe = data

    def fill_gaps (self):
        '''
            Function to fill the missing dates, Filling with zeros for now
        '''
        output = []
        count = 0

        temp = self.dataframe
        start_date = temp.iloc[0]["Date"] #Format YYYY-MM-DD
        end_date = temp.iloc[-1]["Date"]

        #Creating a dummy df with all dates and sales values as 0
        all_dates = pd.date_range(start=start_date, end=end_date, freq='M')
        temp_df = pd.DataFrame()  # add columns to dataset
        temp_df['Date'] = all_dates
        sales = [0 for _ in range(temp_df.shape[0])] #Fix this to be zero or something
        temp_df.set_index('Date', inplace=True)

        #Making the original dataframe ready for merging
        # print("Temp is", temp)
        temp.set_index('Date', inplace=True)
        merged = temp.combine_first(temp_df)
        merged.reset_index(inplace=True)

        print("Merged is", merged)
        output.append(merged)
        count+=merged.shape[0]

        print("Total Count is", count)
        self.dataframe = pd.concat(output, axis=0)
        # print(self.dataframe)

class Forecast():
    def run_forecast(self, dataframe, period):
        print(dataframe)
        fitted_model = ExponentialSmoothing(dataframe['Value'],trend='mul',seasonal='mul',seasonal_periods=period).fit()
        test_predictions = fitted_model.forecast(period)
        return test_predictions
        # print(test_predictions)

# if __name__ == "__main__":
#     reader = Reader()
#     input_data = reader.csv_reader('airline.csv')
#     print(input_data)
#
#     transform = Transformer(input_data)
#
#     forecast = Forecast()
#     forecast.run_forecast(transform.dataframe, 12)
