import pandas as pd
import numpy as np

def process_score_data(input_file, output_file):
    df = pd.read_excel(input_file)
    
    # DataFrame 
    result = pd.DataFrame()
    result['sbd'] = df['sbd']
    result['name'] = df['name']
    result['dob'] = df['dob']
    
    # 
    subjects = ['Toan', 'Van', 'Ly', 'Hoa', 'Sinh', 'KHTN', 'Su', 'Dia', 'GDCD', 'KHXH', 'Tieng Anh']
    for sub in subjects:
        result[sub] = np.nan
    
    # 
    for idx, row in df.iterrows():
        # Chuyển điểm sang chuỗi nếu không phải NaN
        scores = str(row['score']) if pd.notna(row['score']) else ''
        

        if 'Toán:' in scores:
            result.at[idx, 'Toan'] = float(scores.split('Toán:')[1].split()[0])
        
        if 'Ngữ văn:' in scores:
            result.at[idx, 'Van'] = float(scores.split('Ngữ văn:')[1].split()[0])
        
        if 'Vật lý:' in scores:
            result.at[idx, 'Ly'] = float(scores.split('Vật lý:')[1].split()[0])
        
        if 'Hóa học:' in scores:
            result.at[idx, 'Hoa'] = float(scores.split('Hóa học:')[1].split()[0])
        
        if 'Sinh học:' in scores:
            result.at[idx, 'Sinh'] = float(scores.split('Sinh học:')[1].split()[0])
        
        if 'KHTN:' in scores:
            result.at[idx, 'KHTN'] = float(scores.split('KHTN:')[1].split()[0])
        
        if 'Lịch sử:' in scores:
            result.at[idx, 'Su'] = float(scores.split('Lịch sử:')[1].split()[0])
        
        if 'Địa lí:' in scores:
            result.at[idx, 'Dia'] = float(scores.split('Địa lí:')[1].split()[0])
        
        if 'GDCD:' in scores:
            result.at[idx, 'GDCD'] = float(scores.split('GDCD:')[1].split()[0])
        
        if 'KHXH:' in scores:
            result.at[idx, 'KHXH'] = float(scores.split('KHXH:')[1].split()[0])
        if 'Tiếng Anh:' in scores:
            result.at[idx, 'Tieng Anh'] = float(scores.split('Tiếng Anh:')[1].split()[0])

    result.to_excel(output_file, index=False)

# Sử dụng hàm
process_score_data('input.xlsx', 'output.xlsx') # cac file input va output