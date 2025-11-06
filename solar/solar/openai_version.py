import sys
import importlib

def load_openai(version):
    if version == 'latest':
        path = './openai_latest'
    elif version == '0.28':
        path = './openai_028'
    else:
        raise ValueError("Unknown version specified")

    # 현재 경로를 임시로 sys.path에 추가
    sys.path.insert(0, path)
    
    try:
        # openai 모듈을 동적으로 로드
        if 'openai' in sys.modules:
            del sys.modules['openai']
        openai = importlib.import_module('openai')
    finally:
        # 경로를 다시 제거하여 원래 상태로 복원
        sys.path.pop(0)
    
    return openai

# 최신 버전 사용
openai_latest = load_openai('latest')
print("Latest version:", openai_latest.__version__)

# 0.28 버전 사용
openai_028 = load_openai('0.28')
print("Version 0.28:", openai_028.__version__)
