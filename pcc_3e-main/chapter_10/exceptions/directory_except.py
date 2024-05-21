import os 
now_path=os.getcwd()
try : 
    os.mkdir(now_path)
    print(f"{now_path} 디렉토리 경로 지정했습니다.")
except:
    print("{e}에러발생")