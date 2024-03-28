def delete_null_rows(data):
    thresh = int(0.2 * len(data.columns))# 80% of variables must to be not null. this is the condition to keep a row.
    rows_to_delete= data.index[
        (data.isnull().sum(axis=1) >= thresh) & (data['product_name'].isnull() & data['ingredients_text'].isnull())
        ]# check if row's axis is null of + 80% in the variable's total. if product_name and ingredients it's not null, it wouldn't be erased.
    df_cleaned = data.drop(rows_to_delete)# build a new dataframe without row's index to remove
    return df_cleaned

def delete_null_columns(data):
    thresh = int(0.3 * len(data))  # 70% value must be null to be erased
    columns_to_erase = data.columns[data.isnull().sum(axis=0) > thresh]
    data_treatment_clean = data.drop(columns=columns_to_erase, axis=1)
    return data_treatment_clean

