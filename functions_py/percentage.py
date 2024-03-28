def calculate_and_display_percentages(data):
    null_counts = data.isnull().sum()
    percentage_counts = (null_counts / len(data)) * 100
    
    return percentage_counts

