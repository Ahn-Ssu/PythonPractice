#-*-coding: utf-8-*-

# 시퀀스 자료형
# 1. 문자열, 2. 리스트, 3. 튜플 


# 시퀀스 자료형 공통적 특징 
# 인덱싱 [k] 형식, k번 위치의 값 하나를 취한다.
# 슬라이싱 [s:t:p] 형식, s부터 t 사이 구간의 값을 p 간격으로 취한다
# 연결하기 + 연산자, 두 시퀀스형 데이터를 붙여서 새로운 데이터를 만든다
# 반복하기 * 연산자, 시퀀스형 데이터를 여러 번 반복해서 새로운 데이터를 만든다
# 멤버 검사 in 연산자, 어떤 값이 시퀀스 자료형에 속하는지를 검사한다
# 길이 정보 len() 내장 함수, 시퀀스형 데이터 크기 리턴

#문자열 포맷
number = 10
day = "three"
strEx = "I ate %d apples, so I was sick for %s days." % (number, day)
print(strEx)
# 자바 동일 %d 정수, %f 실수, %s 문자열
# 근데 %s로 쓰면 알아서 다 문자열로 바뀌어서 들어감 ( 자동 캐스팅 )
strEx2 = "who are you? {}".format("??")
strEx3 = "I am {name}.".format(name="수현")


# 문서 문자열 
# 모듈의 시작 부분에 있거나, def, class문 다음에 바로 나오는 문자열 

#... 모듈 문서 문자열 
'''
Module __doc__ string
line1
line2
'''
class Ham:
    "Ham class __doc__ string" # 클래스 문서 문자열
    def func(self):
        "Ham class func __doc__ string" # 함수나 메소드 문서 문자열 
        pass 

# 문서 문자열은 각 객체의 __doc__이라는 내장 멤버에 저장 됨 
# 자바의 javadoc 처럼 사용되는 친구들 