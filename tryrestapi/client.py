import requests
import argparse

def upload_csv(file_path, keys, colored):
    url = 'http://localhost:8000/api/upload/'
    
    headers = {
        'Authorization': 'Bearer d28049e4d242e1dbe3684ee8bda8f0c95c69b77e',  
    }
    
    params = {
        'keys': ','.join(keys) if keys else '',
        'colored': 'true' if colored else 'false',
    }
    
    with open(file_path, 'rb') as file:
        files = {'file': file}
        response = requests.post(url, headers=headers, files=files, data=params)
    
    print("Response Status Code:", response.status_code)
    print("Response Text:", response.text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Upload CSV file to the server.')
    parser.add_argument('-k', '--keys', nargs='*', help='Keys for additional columns')
    parser.add_argument('-c', '--colored', action='store_true', help='Whether to color rows')
    parser.add_argument('file', type=str, help='C:\\Users\\mega_\\OneDrive\\Masaüstü\\tryrestapi\\vehicle_project')
    args = parser.parse_args()
    
    upload_csv(args.file, args.keys, args.colored)
