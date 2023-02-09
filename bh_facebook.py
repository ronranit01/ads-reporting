import pandas as pd
# import numpy as np
#
# overall_kpi = ['Ad name', 'Amount spent (USD)', 'Cost per results', 'Purchases',
#                'CPM (cost per 1,000 impressions) (USD)',
#                'CPC (cost per link click) (USD)',
#                'Unique CTR (link click-through rate)', 'Reach', 'Impressions', 'Hook', 'Hold', 'aww', 'New ']
#
# cpm_kpi = ['Ad name', 'Amount spent (USD)', 'Purchases', 'CPM (cost per 1,000 impressions) (USD)',
#            'CPC (cost per link click) (USD)', 'Reach', 'Impressions']
# # grab = ['ron', 'ian', 'ranit']  # criteria
# data_read_pandas = pd.read_csv("The-Blanket-Hoodies-Ads-Dec-30-2019-Jan-30-2023.csv")  # Pandas read excel
#
#
# for index, x in enumerate(data_read_pandas):
#     if x not in overall_kpi:
#         del data_read_pandas[x]
#
# df = data_read_pandas[pd.notnull(data_read_pandas['Purchases'])]  # Get all rows of Purchases that have not 0 or
# # NaN
#
# df.sort_values(by='Amount spent (USD)', ascending=False).head(20).to_excel('Facebook Report.xlsx', index=False)
#
# # data_read_pandas.to_excel('Facebook Report.xlsx', index=False)
#
# # wb.save(filename='testing.xlsx')

table = np.array([
    [1,3],
    [2,4]
])
