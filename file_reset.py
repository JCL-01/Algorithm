files = ["테스트/input.txt", "테스트/output.txt", "테스트/출력 예시.txt", "테스트/test.py"]

for file in files:
    with open(file, "w") as f:
        pass  # 빈 파일로 만들기

print("파일 초기화 완료!")

'''
그리고 현령님이 팀즈 회의에서 알려주신 디버깅으로 input, output.txt 파일 활용해서 vs code에서 먼저 돌려보시는 분들, 풀고 지우고 하기 불편하시지 않나요? 그래서 저는 파일들을 자동으로 초기화 해주는 file_reset.py를 하나 만들었는데요

아래 코드를 만들어주고, 초기화용 터미널을 하나 두고, 
python 연습장\file_reset.py 실행하면 그 뒤부터는 터미널에서 ⬆ 방향키(최근 명령어 복사)로 바로 실행할 수 있어서 그렇게 쓰고 있어요!

------- file_reset.py

files = ["연습장/input.txt", "연습장/output.txt", "연습장/출력예시.txt", "연습장/test.py"]

for file in files:
    with open(file, "w") as f:
        pass  # 빈 파일로 만들기

print("파일 초기화 완료!")'
'''