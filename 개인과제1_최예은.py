quiz={"이화여대 멋사 대표님":"은진",
      "이화여대 멋사 회장님":"연주",
      "멋사 대장":"두희",
      "이화여대 멋사 튜터님":"유진"}

for i in quiz.keys():
    print("다음은 누구에 대한 설명일까요?")
    print(i)
    print("(1)은진 (2)연주 (3)두희 (4)유진")
    answer=input()
    if(answer==quiz[i]):
        print("정답입니다!")
    else:
        print("오답입니다!")
    print()
        
    
