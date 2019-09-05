# list 자료형, 함수사용.
num_list = [1,2,3,4,5,6,11,2,14,53,6,2,4]

# 리스트 길이재기
print("\n리스트 길이재기")
print(len(num_list))

# 리스트에 요소 추가(append)
print("\n리스트에 요소 추가(append)")
num_list.append(7)
print(num_list)
print(num_list.append(8)) # print문 안에서 실행안됨.
print(num_list)

# 리스트 정렬(sort)
print("\n리스트 정렬(sort)")
print(num_list.sort()) # print문안에서 실행안됨.
num_list.sort()
print(num_list)

# 리스트 뒤집기
print("\n리스트 뒤집기")
num_list.reverse()
print(num_list)

# 위치 반환(index)
print("\n위치 반환(index)")
print(num_list.index(5))

# 리스트에 요소 삽입(insert)
print("\n리스트에 요소 삽입(insert)")
num_list.insert(0,14) # 0번째 인덱스에 14를 추가한다.
print(num_list)

# 리스트 요소 제거(remove)
print("\n리스트 요소 제거(remove)")
num_list.remove(2) # 처음나오는 '2'를 제거한다.
print(num_list)

# 리스트 요소 끄집어내기(pop)
print("\n리스트 요소 끄집어내기(pop)")
print(num_list.pop())
print(num_list)

# 리스트에 포함된 요소 x의 개수 세기(count)
print("\n리스트에 포함된 요소 x의 개수 세기(count)")
print(num_list.count(4))
print(num_list.count(53))

# 리스트 확장(extend)
print("\n리스트 확장(extend)")
num_list.extend([3]) # extend는 리스트 형태만 가능하다.
print(num_list)
