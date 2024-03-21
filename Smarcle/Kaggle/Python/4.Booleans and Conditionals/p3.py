'''
자습서에서 저희가 날씨에 대한 준비가 되어 있는지를 결정하는 것에 대해 이야기를 나눴는데요, 저는 오늘 날씨가...

우산이 있는데...
아니면 비가 너무 많이 오지 않고 후드가 있다면...
그렇지 않으면 비가 오고 근무일이 아니면 저는 여전히 괜찮습니다
아래 함수는 이 논리를 파이썬 식으로 바꾸려는 첫 번째 시도입니다. 그 코드에 버그가 있다고 주장했는데 찾을 수 있나요?

preped_for_weather가 버그가 있음을 증명하려면 다음 중 하나에 해당하는 입력 세트를 준비하십시오:

함수가 False를 반환합니다(그러나 True를 반환했어야 함). 또는
함수가 True를 반환했습니다(그러나 False를 반환했어야 함).
이 질문을 완료한 것에 대한 크레딧을 받으려면 코드가 올바른 결과를 반환해야 합니다.
'''
def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    # Don't change this code. Our goal is just to find the bug, not fix it!
    return (have_umbrella or rain_level < 5 and have_hood or not rain_level > 0) and is_workday

# Change the values of these inputs so they represent a case where prepared_for_weather
# returns the wrong answer.
have_umbrella = True
rain_level = 0.0
have_hood = True
is_workday = True

# Check what the function returns given the current values of the variables above
actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
print(actual)

# Check your answer
q3.check()