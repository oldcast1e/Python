# 문자열에서 특정 단어의 포함 여부 확인
sentence = "The quick brown fox jumps over the lazy dog"
word1 = "quick"
word2 = "slow"

# 포함 여부 확인
is_word1_in_sentence = word1 in sentence
is_word2_in_sentence = word2 in sentence

# 결과 출력
print(f"'{word1}' is in the sentence: {is_word1_in_sentence}")
print(f"'{word2}' is in the sentence: {is_word2_in_sentence}")

# # 조건문을 이용한 예제
# if "fox" in sentence:
#     print("The word 'fox' is in the sentence.")
# else:
#     print("The word 'fox' is not in the sentence.")