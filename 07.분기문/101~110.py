### 101~110


# 101
# 파이썬에서 True 혹은 False를 갖는 데이터 타입은 무엇인가?
# bool


# 102
# 아래 코드의 출력 결과를 예상하라
#
# print(3 == 5)
# false
print(3 == 5)


# 103
# 아래 코드의 출력 결과를 예상하라
#
# print(3 < 5)
# true
print(3 < 5)


# 104
# 아래 코드의 결과를 예상하라.
#
# x = 4
# print(1 < x < 5)
# true
x = 4
print(1 < x < 5)


# 105
# 아래 코드의 결과를 예상하라.
#
# print ((3 == 3) and (4 != 3))
# ture
print ((3 == 3) and (4 != 3))


# 106
# 아래 코드에서 에러가 발생하는 원인에 대해 설명하라.
#
# print(3 => 4)
# syntaxerror가 난다 > 등호부터 쓰고 = 등호를 써야한다.
print(3 >= 4)


# 107
# 아래 코드의 출력 결과를 예상하라
#
# if 4 < 3:
#     print("Hello World")
# 아무것도 출력하지 않는다
if 4 < 3:
    print("Hello World")


# 108
# 아래 코드의 출력 결과를 예상하라
#
# if 4 < 3:
#     print("Hello World.")
# else:
#     print("Hi, there.")
# "Hi, there."를 출력한다.
if 4 < 3:
    print("Hello World.")
else:
    print("Hi, there.")


# 109
# 아래 코드의 출력 결과를 예상하라
#
# if True :
#     print ("1")
#     print ("2")
# else :
#     print("3")
# print("4")
# 1, 2, 4를 출력한다.
if True :
    print ("1")
    print ("2")
else :
    print("3")
print("4")


# 110
# 아래 코드의 출력 결과를 예상하라
#
# if True :
#     if False:
#         print("1")
#         print("2")
#     else:
#         print("3")
# else :
#     print("4")
# print("5")
# 3, 5를 출력한다.
if True :
    if False:
        print("1")
        print("2")
    else:
        print("3")
else :
    print("4")
print("5")