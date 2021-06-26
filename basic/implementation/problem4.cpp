Stack = []

Stack.append(5)
Stack.append(6)
Stack.pop()

print(stack)
print(stack[::-1])
#[::n] 문법은, n > 0이면 0번 index부터 n스텝으로 고른 원소가 담겨진 list
              n < 0이면 끝 index부터 n스텝으로 고른 원소가 담겨진 list를 반환한다.
#즉, 위에선 그냥 거꾸로 (스택의 최상단부터) 출력하는 것이다.