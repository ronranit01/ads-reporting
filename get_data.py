import pandas as pd

KPI = {'purchase': ['Ad name', 'Amount spent (USD)', 'Cost per results', 'Purchases',
                    'CPM (cost per 1,000 impressions) (USD)', 'CPC (cost per link click) (USD)',
                    'Unique CTR (link click-through rate)', 'Reach', 'Impressions', 'Hook', 'Hold'],

       "cpm": ['Ad name', 'Amount spent (USD)', 'Purchases', 'CPM (cost per 1,000 impressions) (USD)',
               'CPC (cost per link click) (USD)', 'Reach', 'Impressions'],

       "ctr": ['Ad name', 'Amount spent (USD)', 'Purchases', 'Reach', 'Unique CTR (link click-through rate)',
               'Hook', 'Hold'],

       "name": ["ron", "ian"]
       }

path = "D:\Development Software\Dev Project\Excel Reports\The-Blanket-Hoodies-Ads-Dec-30-2019-Jan-30-2023.csv"
new_file_path = r"D:\Development Software\Dev Project\Excel Reports\New file.csv"

class DataFrame:
    def __init__(self, kpis, data=pd.read_csv(path)):
        self.number = 0
        self.value = ''
        self.data = data
        self.kpis = kpis

    def get_kpi(self):
        """ Get all the required KPI base on kpi(input) """
        for _ in self.data:
            if _ not in KPI[self.kpis]:
                del self.data[_]
        return self.data

    def remove_zero(self):
        """ Get values from get_kpi and remove all NaN from 'Purchases' column """
        return self.get_kpi()[pd.notnull(self.get_kpi()['Purchases'])]

    def new_excel_sort_by(self):
        """ sort remove_zero value with value and top number criteria """
        incorrect_value = True
        while incorrect_value:
            try:
                self.value = input("Enter Value: ").capitalize()
                self.number = int(input("Enter Top 1-10: "))
                for _ in KPI[self.kpis]:
                    if self.value in _:
                        extract = self.remove_zero().sort_values(by=_, ascending=False).head(self.number)
                        extract.to_excel(new_file_path, index=False)
                        incorrect_value = False

            except ValueError:
                print("Enter Valid Number of Values")

    def create_new_excel(self):
        """ Get the value from remove_zero function and create new excel """
        self.remove_zero().to_excel('Facebook Report.xlsx', index=False)


# data = pd.read_excel("testing.xlsx")  # Pandas read excel

try:
    kpi = input("Input KPI [Purchase|CPM|CTR]: ").lower()
    data_frame = DataFrame(kpi)
    data_sort = input("Do you want to sort?: y/n ").lower()

    if data_sort == 'yes' or data_sort == 'y':
        data_frame.new_excel_sort_by()
    else:
        data_frame.create_new_excel()
except KeyError:
    pass
